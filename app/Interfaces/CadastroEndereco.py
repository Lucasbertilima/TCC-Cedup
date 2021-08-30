from tkinter import *
from tkinter.ttk import *
from app.dominios.Endereco.controller import Criar

style = Style()
style.configure('W.TButton', font=('Arial', 10, 'underline'), foreground='Green')


class CadastroEndereco():
    def __init__(self, master=None):
        self.frame = Frame(master).grid()
        self.cep = Label(window, text='Cep', width=10)
        self.cep.grid(row=0, column=0)
        self.complemento = Label(window, text='Complemento', width=10)
        self.complemento.grid(row=1, column=0)
        self.numero = Label(window, text='Número', width=10)
        self.numero.grid(row=2, column=0)
        self.n1 = Entry(window, width=20)
        self.n1.grid(row=0, column=1)
        self.d1 = Entry(window, width=20)
        self.d1.grid(row=1, column=1)
        self.p1 = Entry(window, width=20)
        self.p1.grid(row=2, column=1)
        self.btn = Button(window, text="Cadastrar", width=20, style='W.TButton')
        self.btn.grid(row=3, column=1)

    def cadastrar(self):
        cep = self.n1.get()
        complemento = self.d1.get()
        numero = self.p1.get()
        dicionario_endereco = {'cep': cep, 'complemento': complemento, 'numero': numero}
        Criar(dicionario_endereco)


if __name__ == '__main__':
    window = Tk()
    CadastroEndereco(window)
    window.title("TurtleOrg")
    window.geometry("400x400")
    window.configure(background="green");
    window.mainloop()
