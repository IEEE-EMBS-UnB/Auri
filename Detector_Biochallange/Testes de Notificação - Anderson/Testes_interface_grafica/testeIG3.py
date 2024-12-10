import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget, QMainWindow
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
                title="ALERTA DE LATIDO",
                msg="ATENÇÃO! O CACHORRO ESTÁ LATINDO. CLIQUE EM ENTENDIDO PARA CONFIRMAR.",
                icon=r"C:\Users\55619\Downloads\retriever-dourado.png"  # Opcional
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

        self.label = QLabel("Notificação importante ativa!", self)
        layout.addWidget(self.label)

        self.ack_button = QPushButton("Entendido", self)
        self.ack_button.clicked.connect(self.stop_notifications)
        layout.addWidget(self.ack_button)

        # Configurar o layout no widget principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def stop_notifications(self):
        """Interrompe as notificações e atualiza a interface."""
        self.manager.stop_notifications()
        self.label.setText("Notificações encerradas.")
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
