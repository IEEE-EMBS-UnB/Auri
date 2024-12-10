import os

def criar_arquivo_parada():
    """Cria o arquivo para sinalizar a parada."""
    with open("stop_notification.txt", "w") as f:
        f.write("Notificação encerrada.")
    print("Arquivo de parada criado.")

if __name__ == "__main__":
    criar_arquivo_parada()
