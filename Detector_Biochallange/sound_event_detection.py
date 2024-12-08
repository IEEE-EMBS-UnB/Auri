import subprocess
import sys

# Verificar e instalar o win10toast se necessário
try:
    from win10toast import ToastNotifier
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "win10toast"])
    from win10toast import ToastNotifier

import numpy as np
import pyaudio
from matplotlib import pyplot as plt
import pandas as pd
import sounddevice as sd
from collections import deque
import threading

from keras_yamnet import params
from keras_yamnet.yamnet import YAMNet, class_names
from keras_yamnet.preprocessing import preprocess_input

from plot import Plotter

def carregar_categorias(filename="selected_numbers.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            # Verificar se o arquivo tem pelo menos 2 linhas com números
            if len(lines) < 2 or not all(line.strip().isdigit() for line in lines):
                raise ValueError("Arquivo não tem pelo menos 2 linhas válidas.")
            categories = [int(line.strip()) for line in lines]
            return categories
    except (FileNotFoundError, ValueError):
        print(f"Arquivo {filename} não encontrado ou inválido. Usando categorias padrão.")
        return [0, 349, 5, 10]


def ler_configuracao(filename="config.txt"):
    try:
        with open(filename, "r") as f:
            config = f.readline().strip()
            return config == "notifications=on"
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado. Usando configuração padrão (notificações ativadas).")
        return True

def fechar(event=None):
    print("Fechando a janela...")
    try:
        stream.stop_stream()
        stream.close()
    except Exception as e:
        print(f"Erro ao fechar o stream: {e}")
    try:
        audio.terminate()
    except Exception as e:
        print(f"Erro ao terminar o PyAudio: {e}")
    plt.close('all')
    exit(0)

# Lock para sincronização de notificações
notification_lock = threading.Lock()

def notificar(titulo, mensagem):
    with notification_lock:
        print(f"Enviando notificação: {mensagem}")  # Log da notificação no terminal
        toast = ToastNotifier()
        toast.show_toast(
            titulo,
            mensagem,
            duration=10,
            icon_path=None,
            threaded=True,
        )

if __name__ == "__main__":

    ################### SETTINGS ###################
    plt_classes = carregar_categorias()  # Carregar categorias selecionadas do arquivo
    notifications_enabled = ler_configuracao()  # Ler configuração de notificações
    class_labels = True
    FORMAT = pyaudio.paFloat32
    CHANNELS = 1
    RATE = params.SAMPLE_RATE
    WIN_SIZE_SEC = 0.975
    CHUNK = int(WIN_SIZE_SEC * RATE)
    CONFIDENCE_THRESHOLD = 0.4  # Limite de confiança para considerar uma detecção válida
    HISTORY_LENGTH = 4  # Número de detecções anteriores a serem avaliadas

    print(sd.query_devices())
    MIC = None

    #################### MODEL #####################
    
    model = YAMNet(weights='keras_yamnet/yamnet.h5')
    yamnet_classes = class_names('keras_yamnet/yamnet_class_map.csv')

    #################### STREAM ####################
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT,
                        input_device_index=MIC,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")

    if plt_classes is not None:
        plt_classes_lab = [yamnet_classes[i] for i in plt_classes]
        n_classes = len(plt_classes)
    else:
        plt_classes = [k for k in range(len(yamnet_classes))]
        plt_classes_lab = yamnet_classes if class_labels else None
        n_classes = len(yamnet_classes)

    monitor = Plotter(n_classes=n_classes, FIG_SIZE=(12, 6), msd_labels=plt_classes_lab)

    # Conectar o evento de fechamento do Matplotlib à função fechar
    monitor.fig.canvas.mpl_connect('close_event', fechar)

    # Dicionário para armazenar histórico de detecções
    detection_history = {classe: deque(maxlen=HISTORY_LENGTH) for classe in plt_classes}

    try:
        while True:  # Loop infinito para execução contínua
            # Waveform
            data = preprocess_input(np.frombuffer(
                stream.read(CHUNK), dtype=np.float32), RATE)
            prediction = model.predict(np.expand_dims(data, 0))[0]

            # Atualização do histórico para cada classe
            for i, classe in enumerate(plt_classes):
                detection_history[classe].append(prediction[classe])
                if len(detection_history[classe]) == HISTORY_LENGTH:
                    average_confidence = np.mean(detection_history[classe])
                    if average_confidence >= CONFIDENCE_THRESHOLD:
                        mensagem = f"Evento '{yamnet_classes[classe]}' detectado com confiança média de {average_confidence:.2f} nas últimas {HISTORY_LENGTH} detecções."
                        if notifications_enabled:
                            notificar("AVISO DE NOTIFICAÇÃO", mensagem)
                        else:
                            print(mensagem)  # Log da notificação no terminal se desativada
                        detection_history[classe].clear()  # Limpar o histórico após notificação

            monitor(data.transpose(), np.expand_dims(prediction[plt_classes], -1))

    except KeyboardInterrupt:
        # Parar a gravação ao interromper com o teclado (Ctrl+C)
        print("Interrupção de teclado detectada. Finalizando gravação...")
        fechar()
    except Exception as e:
        print(f"Erro inesperado: {e}")
        fechar()
