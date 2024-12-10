import time
from winotify import Notification

def send_notification():
    toast = Notification(app_id="AVISO",
                         title="ALARME DE INCÊNDIO",
                         msg="O ALARME DE INCÊNDIO ESTÁ TOCANDO!",
                         icon=r"C:\Users\55619\Downloads\sirenes.png")
    toast.add_actions(label="Entendido", launch="https://comando-para-encerrar")
    toast.show()

while True:
    send_notification()
    time.sleep(10)  # Reenvia a notificação a cada 10 segundos
