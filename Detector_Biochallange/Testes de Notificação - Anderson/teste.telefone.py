from winotify import Notification

toast = Notification(app_id="AVISO",
                     title="ALERTA DE TELEFONE",
                     msg="O TELEFONE ESTÁ TOCANDO!",
                     icon=r"C:\Users\55619\Downloads\telefone-fixo.png")  # Substitua pelo caminho de uma imagem válida
toast.show()
