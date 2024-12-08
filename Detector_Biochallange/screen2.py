import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('keras_yamnet/yamnet_class_map.csv')
categories = df['display_name'].tolist()
category_dict = dict(zip(df['display_name'], df['index']))

def carregar_selecoes_preconfiguradas(filename="selected_numbers.txt"):
    try:
        with open(filename, "r") as f:
            selected_numbers = [int(line.strip()) for line in f if line.strip().isdigit()]
            return selected_numbers
    except FileNotFoundError:
        return []

class Screen2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg="white")

        # Inicializa a lista para armazenar os números das categorias selecionadas
        self.selected_numbers = []

        # Carregar seleções preconfiguradas
        preconfigured_selections = carregar_selecoes_preconfiguradas()

        # Função para salvar os números correspondentes às categorias selecionadas
        def salvar_selecoes():
            self.selected_numbers.clear()
            for combobox in comboboxes:
                categoria = combobox.get()
                if categoria in category_dict:
                    self.selected_numbers.append(category_dict[categoria])
            with open("selected_numbers.txt", "w") as f:
                for number in self.selected_numbers:
                    f.write(f"{number}\n")
            # Salvar a configuração de notificações
            notifications_enabled = notifications_var.get()
            with open("config.txt", "w") as f:
                f.write(f"notifications={'on' if notifications_enabled else 'off'}\n")
            messagebox.showinfo("Salvo", "Configurações salvas com sucesso.")
            master.show_screen1()  # Voltar para a tela Screen1 após salvar

        # Título e texto instrutivo
        titulo = tk.Label(self, text="Seleção de Categorias", font=("Helvetica", 16, "bold"), bg="white")
        titulo.pack(pady=10)
        
        instrucao = tk.Label(self, text="Por favor, selecione as categorias desejadas e clique em 'Salvar Seleções'.", bg="white")
        instrucao.pack(pady=10)

        # Criação dos seletores de categoria
        comboboxes = []
        for i in range(5):
            combobox = ttk.Combobox(self, values=categories, font=("Helvetica", 12))
            combobox.pack(pady=5, padx=10, fill="x")
            if i < len(preconfigured_selections):
                selected_category = next((key for key, value in category_dict.items() if value == preconfigured_selections[i]), None)
                if selected_category:
                    combobox.set(selected_category)
            comboboxes.append(combobox)

        # Checkbox para ativar/desativar notificações
        notifications_var = tk.BooleanVar(value=True)
        checkbox = tk.Checkbutton(self, text="Ativar Notificações", variable=notifications_var, bg="white", font=("Helvetica", 12))
        checkbox.pack(pady=10)

        # Botão para salvar as seleções
        btn_salvar = tk.Button(self, text="Salvar Seleções", command=salvar_selecoes, font=("Helvetica", 12), bg="#2a84c3", fg="white")
        btn_salvar.pack(pady=10)

        # Botão para retornar à tela 1
        btn_voltar = tk.Button(self, text="Voltar", command=master.show_screen1, font=("Helvetica", 12), bg="#2a84c3", fg="white")
        btn_voltar.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Seleção de Categorias")
    root.configure(bg="white")
    app = Screen2(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
