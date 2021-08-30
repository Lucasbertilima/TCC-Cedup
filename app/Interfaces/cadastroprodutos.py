from tkinter import *
from app.dominios.Produtos.controller import Criar

class CadastroProduto():
    def __init__(self, master=None):
        self.nome = Label(window, text='Nome', width=10)
        self.nome.grid(row=0, column=0)
        self.descricao = Label(window, text='Descrição', width=10)
        self.descricao.grid(row=1, column=0)
        self.peso = Label(window, text='Peso', width=10)
        self.peso.grid(row=2, column=0)
        self.preco = Label(window, text='Preço', width=10)
        self.preco.grid(row=3, column=0)
        self.qtd = Label(window, text='Quantidade', width=10)
        self.qtd.grid(row=4, column=0)
        self.n1 = Entry(window, width=20)
        self.n1.grid(row=0, column=1)
        self.d1 = Entry(window, width=20)
        self.d1.grid(row=1, column=1)
        self.p1 = Entry(window, width=20)
        self.p1.grid(row=2, column=1)
        self.p2 = Entry(window, width=20)
        self.p2.grid(row=3, column=1)
        self.q1 = Entry(window, width=20)
        self.q1.grid(row=4, column=1)
        self.btn = Button(window, text="Cadastrar", width=20)
        self.btn.grid(row=5, column=1)

    def cadastrar(self):
        nome = self.n1.get()
        descricao = self.d1.get()
        peso = self.p1.get()
        preco = self.p2.get()
        quantidade = self.q1.get()
        dict_produto = {'nome': nome, 'descricao': descricao, 'peso': peso,
                        'preco': preco, 'quantidade': quantidade}
        Criar(dict_produto)


if __name__ == '__main__':
    window = Tk()
    CadastroProduto(window)
    window.title("TurtleOrg")
    window.geometry("400x400")
    window.configure(background="green");
    window.mainloop()
