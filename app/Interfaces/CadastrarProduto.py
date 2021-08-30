from tkinter import *

fields = ('Nome', 'Categoria', 'Peso', 'Preco', 'Qtd')


def criarlinhas(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


class CadastroProdutos:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.grid(row=0, column=1)

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.grid(row=1, column=1)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.grid(row=2, column=1)

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.grid(row=5, column=1)

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 30
        self.quintoContainer.grid(row=3, column=1)

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 40
        self.sextoContainer.grid(row=4, column=1)

        self.titulo = Label(self.primeiroContainer, text="Cadastro de Produtos")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.grid(row=0, column=0)

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.grid(row=0, column=0)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.grid(row=0, column=1)

        self.categoriaLabel = Label(self.terceiroContainer, text="Categoria", font=self.fontePadrao)
        self.categoriaLabel.grid(row=0, column=0)

        self.categoria = Entry(self.terceiroContainer)
        self.categoria["width"] = 30
        self.categoria["font"] = self.fontePadrao
        self.categoria.grid(row=0, column=1)

        self.pesoLabel = Label(self.quintoContainer, text="Peso", font=self.fontePadrao)
        self.pesoLabel.grid(row=0, column=0)

        self.peso = Entry(self.quintoContainer)
        self.peso["width"] = 30
        self.peso["font"] = self.fontePadrao
        self.peso.grid(row=0, column=1)

        self.precoLabel = Label(self.sextoContainer, text="Preço", font=self.fontePadrao)
        self.precoLabel.grid(row=0, column=0)

        self.preco = Entry(self.sextoContainer)
        self.preco["width"] = 30
        self.preco["font"] = self.fontePadrao
        self.preco["show"] = "*"
        self.preco.grid(row=0, column=1)

        self.cadastrar = Button(self.quartoContainer)
        self.cadastrar["text"] = "Cadastrar"
        self.cadastrar["font"] = ("Calibri", "8")
        self.cadastrar["width"] = 10
        self.cadastrar["command"] = self.verificaSenha
        self.cadastrar.grid(row=0, column=1)

        self.cancelar = Button(self.quartoContainer)
        self.cancelar["text"] = "Cancelar"
        self.cancelar["font"] = ("Calibri", "8")
        self.cancelar["width"] = 10
        self.cancelar.grid(row=0, column=2)

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.grid(row=0, column=1)

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


root = Tk()
root.title("Cadastro de Produtos")
root.geometry("300x300")
CadastroProdutos(root)
root.mainloop()
# if __name__ == '__main__':
#    root = Tk()
#    ents = criarlinhas(root, fields)
#    root.bind('<Return>', (lambda event, e = ents: fetch(e)))
#    b1 = Button(root, text='Cadastrar')
#    b1.pack(side=LEFT, padx=5, pady=5)
#    root.mainloop()
