from winotify import Notification

toast = Notification(app_id="AVISO",
                     title="ALERTA DE INCÊNDIO",
                     msg="O ALARME DE INCÊNDIO ESTÁ TOCANDO!",
                     icon=r"C:\Users\55619\Downloads\sirenes.png")  # Substitua pelo caminho de uma imagem válida
toast.show()
