from winotify import Notification

toast = Notification(app_id="AVISO",
                     title="ALERTA DE LATIDO",
                     msg="O CACHORRO ESTÁ LATINDO!",
                     icon=r"C:\Users\55619\Downloads\retriever-dourado.png")  # Substitua pelo caminho de uma imagem válida
toast.show()
