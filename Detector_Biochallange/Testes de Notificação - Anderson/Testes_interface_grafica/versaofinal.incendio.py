import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget, QMainWindow
from PyQt5.QtCore import Qt
from winotify import Notification, audio
import threading
import time

class NotificationManager:
    def __init__(self):
        self.running = True  # Controle para as notificações

    def send_notifications(self):
        """Envia notificações enquanto 'running' for True."""
        while self.running:
            toast = Notification(
                app_id="AVISO",
                title="ALERTA DE INCÊNDIO",
                msg="O ALARME DE INCÊNDIO ESTÁ TOCANDO!",
                icon=r"C:\Users\55619\Downloads\sirenes.png"  # Opcional
            )
            toast.set_audio(audio.Default, loop=False)
            toast.show()
            time.sleep(3)  # Intervalo entre notificações

            
            toast.set_audio(audio.Default, loop=False)
            toast.show()
            time.sleep(3)  # Intervalo entre notificações

    def stop_notifications(self):
        """Interrompe as notificações."""
        self.running = False

class MainWindow(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

        # Configurações básicas da janela
        self.setWindowTitle("Gerenciador de Notificações")
        self.resize(500, 300)  # Aumenta o tamanho da janela
        self.center_window()  # Centraliza a janela na tela

        # Layout e widgets
        layout = QVBoxLayout()

        self.label = QLabel("Notificação importante ativa!", self)
        self.label.setAlignment(Qt.AlignCenter)  # Centraliza o texto no QLabel
        layout.addWidget(self.label)

        self.ack_button = QPushButton("Entendido", self)
        self.ack_button.clicked.connect(self.stop_notifications)
        layout.addWidget(self.ack_button)

        # Configurar o layout no widget principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def center_window(self):
        """Centraliza a janela na tela."""
        screen = QApplication.primaryScreen().geometry()
        window = self.geometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2
        self.move(x, y)

    def stop_notifications(self):
        """Interrompe as notificações e atualiza a interface."""
        self.manager.stop_notifications()
        self.label.setText("Aviso Recebido. Notificações encerradas.")
        self.ack_button.setEnabled(False)  # Desativa o botão após clicar

def main():
    app = QApplication(sys.argv)
    manager = NotificationManager()

    # Iniciar notificações em uma thread separada
    threading.Thread(target=manager.send_notifications, daemon=True).start()

    # Criar a interface gráfica
    window = MainWindow(manager)
    window.show()

    # Executar o loop do aplicativo
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
