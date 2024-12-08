import tkinter as tk
from tkinter import PhotoImage
import subprocess

class Screen1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg="white")

        # Carregar e redimensionar a imagem
        imagem_original = PhotoImage(file="logo.png")  # Substitua pelo caminho correto da sua imagem
        imagem = imagem_original.subsample(2, 2)  # Reduz o tamanho da imagem pela metade

        # Frame para a imagem
        frame_imagem = tk.Frame(self)  # Define o fundo como branco
        frame_imagem.pack(side="left", padx=20, pady=20)  # Posiciona o frame da imagem à esquerda

        # Widget de imagem
        label_imagem = tk.Label(frame_imagem, image=imagem, bg="white")  # Define o fundo como branco
        label_imagem.image = imagem  # Necessário para manter a referência
        label_imagem.pack()

        # Frame para os botões
        frame_botoes = tk.Frame(self)  # Define o fundo como branco
        frame_botoes.pack(side="right", padx=20, pady=20)  # Posiciona o frame dos botões à direita

        # Nomes dos botões
        nomes_botao = ["Detector", "Configurações", "Ajuda"]
        # Função chamada quando o primeiro botão é pressionado
        def executar_script():
            master.destroy()  # Fechar a janela principal
            subprocess.run(["python", "./sound_event_detection.py"])  # Executar o script
        # Criar e posicionar os botões dentro do frame_botoes com estilo aprimorado
        for i in range(3):
            if i == 0:
                command = executar_script
            elif i == 1:
                command = master.show_screen2
            else:
                command = lambda: print("Botão clicado!")
        

            botao = tk.Button(frame_botoes, 
                              text=f" {nomes_botao[i]}", 
                              command=command, 
                              borderwidth=2, 
                              relief="flat", 
                              bg="#2a84c3", 
                              fg="white", 
                              activebackground="#45a049",
                              activeforeground="white",
                              font=("Helvetica", 12, "bold"),
                              padx=20, pady=10)
            botao.pack(pady=10, padx=20, ipadx=10, ipady=5)