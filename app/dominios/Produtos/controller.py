from typing import List
from database.database import salvar
from app.dominios.Produtos.modelo import Produto


def Criar(nome, desc, cat_id, nome_categoria, peso, preco, qtd, qtdm) -> Produto:
    #categoria = criar_categoria(dados['categoria'])
    produto = Produto(nome=nome,
                      descricao=desc,
                      categoria_fk=cat_id,
                      nome_categoria=nome_categoria,
                      peso=peso,
                      preco=preco,
                      quantidade=qtd,
                      quantidademinima=qtdm,
                      )
    return salvar(produto)


def get() -> List[Produto]:
    return Produto.query.all()


def get_por_id(id: str) -> Produto:
    return Produto.query.get(id)


def atualizar(id_produto: str, quantidade: str, operacao) -> Produto:
    produto = get_por_id(id_produto)
    if operacao == 'entrada':
        qtdatual = produto.quantidade
        novaqtd = qtdatual + int(quantidade)
    elif operacao == 'saida':
        qtdatual = produto.quantidade
        novaqtd = qtdatual - quantidade
    produto.quantidade = novaqtd
    return salvar(produto)


def atualizar_campos(id_produto: str, nome, descricao, preco, quantidademinima) -> Produto:
    produto = get_por_id(id_produto)
    produto.nome = nome
    produto.descricao = descricao
    produto.preco = preco
    produto.quantidademinima = quantidademinima
    return salvar(produto)


#def relatorio() -> list:
#    lista_estoque_minimo = []
#    lista_pouco_estoque = []
#    lista_produtos = get()
#    for i in lista_produtos:
#        if i.quantidade < i.quantidademinima:
#            lista_pouco_estoque.append(i)
#        else if i.quantidade == i.quantidademinima:
#            lista_estoque_minimo.append(i)
#
#    if lista_pouco_estoque.lenght > 0 and  lista_estoque_minimo.lenght ==0:
#        return lista_pouco_estoque
#    else if lista_estoque_minimo.lenght > 0 and lista_pouco_estoque.lenght == 0:
#        return lista_estoque_minimo
#    else if lista_estoque_minimo.lenght > 0 and lista_pouco_estoque.lenght > 0:
#        lista_produtos_alerta = [lista_estoque_minimo, lista_pouco_estoque]
#        return lista_produtos_alerta
#    else:
#        return 'Não há produtos no limite ou abaixo do estoque'