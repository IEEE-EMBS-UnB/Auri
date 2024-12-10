from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from winotify import Notification

toast = Notification(app_id="AVISO",
                     title="ALERTA DE INCÊNDIO",
                     msg="O ALARME DE INCÊNDIO ESTÁ TOCANDO!",
                     icon=r"C:\Users\55619\Downloads\sirenes.png")  # Substitua pelo caminho de uma imagem válida
toast.show()

class NotificationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notificação importante")
        self.setGeometry(100, 100, 400, 300)  # Define a posição e tamanho da janela

        # Layout para organizar os elementos na interface
        layout = QVBoxLayout(self)

        # Adiciona o texto à interface com tamanho de fonte maior
        self.text_label = QLabel('ALERTA: O alarme de incêndio está tocando!', self)
        self.text_label.setStyleSheet("font-size: 20px; font-weight: bold;")  # Define o tamanho da fonte
        layout.addWidget(self.text_label, alignment=Qt.AlignCenter)

        # Adiciona o GIF à interface
        self.gif_label = QLabel(self)
        movie = QMovie("C:/Users/55619/Downloads/clideo_editor_098a32e11d2040b8ae59a505a2223769.gif")  # Substitua pelo caminho do seu GIF
        self.gif_label.setMovie(movie)
        layout.addWidget(self.gif_label, alignment=Qt.AlignCenter)
        movie.start()

        # Adiciona o botão "Entendido" com aumento de tamanho
        self.button = QPushButton("Entendido", self)
        self.button.setFixedSize(200, 50)  # Aumenta o tamanho do botão
        self.button.setStyleSheet("font-size: 18px; padding: 10px 20px;")  # Aumenta o tamanho da fonte e do padding
        self.button.clicked.connect(self.close)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)

        # Define o layout na janela
        self.setLayout(layout)

    def center(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        window_geometry = self.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication([])

    window = NotificationApp()
    window.show()

    # Agora chamamos center() depois de window.show()
    window.center()

    app.exec_()
