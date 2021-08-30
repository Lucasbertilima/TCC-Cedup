from tkinter import *

from app.dominios.Categoria.controller import Criar

class CadastroCategoria():
    def __init__(self, master=None):
        self.frame = Frame(master).grid()
        self.nomelabel = Label(self.frame, text='Nome', width=10)
        self.nomelabel.grid(row=0, column=0)
        self.nome = Entry(self.frame, width=20)
        self.nome.grid(row=0, column=1)
        self.btn = Button(self.frame, text="Cadastrar", width=20, command=self.cadastro)
        self.btn.grid(row=1, column=1)

    def cadastro(self):
        nome = self.nome.get()
        Criar(nome)

if __name__ == '__main__':
    window = Tk()
    CadastroCategoria(window)
    window.title("TurtleOrg")
    window.geometry("400x400")
    window.configure(background="green");
    window.mainloop()