import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QVBoxLayout, QWidget
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
                app_id="Notificador",
                title="Alerta Persistente",
                msg="Esta é uma notificação persistente.",
                icon=r"C:\path\to\icon.ico"  # Opcional
            )
            toast.set_audio(audio.Default, loop=False)
            toast.show()
            time.sleep(5)  # Intervalo entre notificações

    def stop_notifications(self):
        """Interrompe as notificações."""
        self.running = False

class MainWindow(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

        # Configurações básicas da janela
        self.setWindowTitle("Gerenciador de Notificações")
        self.setGeometry(100, 100, 300, 150)

        # Layout e widgets
        layout = QVBoxLayout()

        self.label = QLabel("Gerencie as notificações abaixo:", self)
        layout.addWidget(self.label)

        self.start_button = QPushButton("Iniciar Notificações", self)
        self.start_button.clicked.connect(self.start_notifications)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Parar Notificações", self)
        self.stop_button.clicked.connect(self.stop_notifications)
        layout.addWidget(self.stop_button)

        # Configurar o layout no widget principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_notifications(self):
        self.manager.running = True
        threading.Thread(target=self.manager.send_notifications, daemon=True).start()

    def stop_notifications(self):
        self.manager.stop_notifications()

def main():
    app = QApplication(sys.argv)
    manager = NotificationManager()
    window = MainWindow(manager)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
