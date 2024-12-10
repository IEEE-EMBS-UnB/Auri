import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from winotify import Notification, audio
import threading  # Para rodar a notificação em paralelo com a interface

class NotificationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.notifying = True  
        

    def init_ui(self):
        # Configurações da janela
        self.setWindowTitle("Notificação Importante")
        self.resize(400, 300)
        self.center_window()

        # Layout principal
        layout = QVBoxLayout()

        # Texto
        text_label = QLabel("ALERTA: O alarme de incêndio está tocando!")
        text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(text_label)

        # GIF
        gif_label = QLabel()
        movie = QMovie("C:/Users/55619/Downloads/clideo_editor_098a32e11d2040b8ae59a505a2223769.gif")  # Substitua pelo caminho do seu GIF
        gif_label.setMovie(movie)
        movie.start()
        layout.addWidget(gif_label)

        # Botão
        close_button = QPushButton("Entendido")
        close_button.clicked.connect(self.stop_notifications)
        layout.addWidget(close_button)

        # Configuração do layout
        self.setLayout(layout)

        # Inicia o envio das notificações em paralelo
        threading.Thread(target=self.send_notifications, daemon=True).start()

    def center_window(self):
        # Centralizar a janela
        frame_geometry = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        center_point = QApplication.desktop().screenGeometry(screen).center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def send_notifications(self):
        # Envia notificações persistentes enquanto self.notifying for True
        toast = Notification(
            app_id="AVISO",
            title="ALARME DE INCÊNDIO",
            msg="O alarme de incêndio está tocando",
            icon="C:/Users/55619/Downloads/sirenes.png"  # Substitua pelo caminho do ícone (ou deixe vazio para nenhum)
        )
        toast.set_audio(audio.Default, loop=False)

        while self.notifying:
            toast.show()
            threading.Event().wait(5)  # Intervalo de 5 segundos entre notificações

    def stop_notifications(self):
        # Para as notificações e fecha a interface
        self.notifying = False
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotificationApp()
    window.show()
    sys.exit(app.exec_())
