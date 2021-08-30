from typing import Tuple, Dict, Any
from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required
from app.dominios.Produtos.controller import Criar as Criar_produto, get as get_produto,\
    get_por_id as get_produto_por_id, atualizar as atualizar_produto, atualizar_campos as atualizar_campos_produto
from app.dominios.Categoria.controller import get as get_categorias, get_por_id as get_categoria_por_id

app_produtos = Blueprint('app.produtos', __name__)


@app_produtos.route('/TurtleOrg/Cadastro-produtos', methods=['POST', 'GET'])
@login_required
def post() -> Tuple[Any]:
    list_cat = get_categorias()
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        categoria_id = request.form['categoria']
        categoria = get_categoria_por_id(categoria_id)
        Peso = request.form['peso']
        Preco = request.form['preco']
        quantidade = request.form['quantidade']
        quantidademinima = request.form['quantidademinima']
        produto = Criar_produto(nome, descricao, categoria_id, categoria.nome, Peso, Preco, quantidade, quantidademinima)
        if produto:
            return render_template('home.html')
        else:
            return render_template('CadastroProduto.html', list_cat=list_cat)
    return render_template('CadastroProduto.html', list_cat=list_cat)


@app_produtos.route('/TurtleOrg/Pesquisa-produtos', methods=['GET'])
@login_required
def get() -> Tuple[Any]:
    produtos = get_produto()
    return render_template('PesquisaProduto.html', produtos=produtos)


@app_produtos.route('/TurtleOrg/Pesquisa-produtos-falta', methods=['GET'])
@login_required
def get_falta() -> Tuple[Any]:
    lista_produtos_em_falta = []
    produtos = get_produto()
    for produto in produtos:
        if produto.quantidade < produto.quantidademinima:
            lista_produtos_em_falta.append(produto)
    return render_template('PesquisaProdutofalta.html', lista=lista_produtos_em_falta)


@app_produtos.route('/TurtleOrg/Pesquisa-produtos/<id>', methods=['GET'])
@login_required
def get_by_id(id: int) -> Tuple[Any]:
    produto = get_produto_por_id(id)
    produtos = [produto]
    return render_template('PesquisaProduto.html', produtos=produtos)


@app_produtos.route('/TurtleOrg/Alterar-produto/<id>', methods=['POST', 'GET'])
@login_required
def put(id: int) -> Tuple[Any]:
    id_p = id
    produto = get_produto_por_id(id_p)
    if request.method == 'POST':
        id_produto = request.form['id_pro']
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        quantidademinima = request.form['quantidademinima']
        novo_prod = atualizar_campos_produto(id_produto, nome, descricao, preco, quantidademinima)
        if novo_prod:
            produtos = get_produto()
            return render_template('PesquisaProduto.html', produtos=produtos)
    return render_template('AlterarProduto.html', produto=produto)