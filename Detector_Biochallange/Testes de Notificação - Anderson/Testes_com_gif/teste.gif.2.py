import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QDesktopWidget
from winotify import Notification


class NotificationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Inicializa a variável notifying
        self.notifying = True
        self.setup_ui()

        # Iniciar notificação em background
        self.send_notifications()

    def setup_ui(self):
        self.setWindowTitle("Notificação com GIF")
        self.setFixedSize(600, 400)
        self.centralize_window()

        # Criando o texto
        self.label = QLabel("ALERTA: o alarme de incêndio está tocando!", self)
        self.label.setAlignment(Qt.AlignCenter)

        # Adicionando o GIF
        movie = QMovie("C:/Users/55619/Downloads/clideo_editor_098a32e11d2040b8ae59a505a2223769.gif")  # Substitua pelo caminho do seu GIF
        gif_label = QLabel(self)
        gif_label.setMovie(movie)
        movie.start()

        # Botão de "Entendido"
        button = QPushButton("Entendido", self)
        button.clicked.connect(self.stop_notifications)

        # Layout da interface
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(gif_label)
        layout.addWidget(button)

        # Definindo o widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def centralize_window(self):
        # Centraliza a janela na tela
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def stop_notifications(self):
        self.notifying = False  # Atualiza para parar as notificações
        self.close()

    def send_notifications(self):
        # Envia a notificação utilizando a biblioteca winotify
    
        while self.notifying:  # Verifica o status de notifying
            notification = Notification(
                app_id="AVISO",
                title="ALERTA DE INCÊNDIO",
                msg="O alarme de incêndio está tocando!"
            )
            notification.set_audio("default", loop=False)
            notification.show()

            # Intervalo entre as notificações
            QTimer.singleShot(5000, self.send_notifications)  # Envia uma nova notificação após 5 segundos
            break  # Quebra para evitar loop infinito de notificações


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotificationApp()
    window.show()
    sys.exit(app.exec_())
