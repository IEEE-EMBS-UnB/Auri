import time
import os
from threading import Thread
from winotify import Notification

# Variável de controle para parar as notificações
stop_notifications = False

def send_notification():
    """Envia notificações recorrentes com botão para encerrar."""
    global stop_notifications
    toast = Notification(app_id="AVIDO",
                         title="ALARME DE INCÊNDIO",
                         msg="O ALARME DE INCÊNDIO ESTÁ TOCANDO. BUSQUE AJUDA!",
                         icon=r"C:\Users\55619\Downloads\sirenes.png")
    toast.add_actions(label="Entendido", launch="notepad.exe")
    toast.show()

def monitor_stop_signal():
    """Monitora o arquivo de controle para interromper o loop."""
    global stop_notifications
    while not stop_notifications:
        # Verifica se o arquivo foi criado
        if os.path.exists("stop_notification.txt"):
            stop_notifications = True
            print("Notificações encerradas.")
        time.sleep(1)

# Cria uma thread para monitorar o arquivo
monitor_thread = Thread(target=monitor_stop_signal)
monitor_thread.start()

# Loop de envio de notificações
try:
    while not stop_notifications:
        send_notification()
        time.sleep(7)  # Intervalo de 7s entre notificações
finally:
    # Limpeza do arquivo e encerramento
    if os.path.exists("stop_notification.txt"):
        os.remove("stop_notification.txt")
    print("Encerramento concluído.")
