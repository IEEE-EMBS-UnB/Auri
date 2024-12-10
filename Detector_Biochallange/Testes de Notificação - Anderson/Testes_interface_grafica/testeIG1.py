import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações básicas da janela
        self.setWindowTitle("Alerta")
        self.setGeometry(300, 300, 500, 400)

        # Criação do botão
        self.button = QPushButton("Clique Aqui", self)
        self.button.setGeometry(200, 180, 200, 140)  # Posição e tamanho do botão
        self.button.clicked.connect(self.mostrar_mensagem)

    def mostrar_mensagem(self):
        QMessageBox.information(self, "Mensagem", "O cachorro está latindo")

# Função principal para rodar o aplicativo
def main():
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

