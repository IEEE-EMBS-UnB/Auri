import tkinter as tk
from screen1 import Screen1
from screen2 import Screen2

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Detecção de Eventos Sonoros em Tempo Real")
        self.geometry("1000x500")
        self.show_screen1()

    def show_screen1(self):
        self.clear_window()
        screen1 = Screen1(self)
        screen1.pack(fill="both", expand=True)

    def show_screen2(self):
        self.clear_window()
        screen2 = Screen2(self)
        screen2.pack(fill="both", expand=True)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
