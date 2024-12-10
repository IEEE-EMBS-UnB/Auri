import time
import os
from winotify import Notification

# Caminho para o arquivo que controla o encerramento
stop_file = "stop_notification.txt"

def send_notification():
    toast = Notification(app_id="AVISO",
                         title="ALARME DE INCÊNDIO",
                         msg="O ALARME DE INCÊNDIO ESTÁ TOCANDO",
                         icon=r"C:\Users\55619\Downloads\sirenes.png")
    toast.add_actions(label="Entendido", launch=f"file:///{os.getcwd()}/{stop_file}")
    toast.show()

# Loop para enviar notificações até o arquivo ser criado
while not os.path.exists(stop_file):
    send_notification()
    time.sleep(10)  # Envia a notificação a cada 10 segundos

# Remove o arquivo de controle ao encerrar
os.remove(stop_file)
print("Aviso Recebido!")
