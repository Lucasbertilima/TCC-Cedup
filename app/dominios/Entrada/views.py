from typing import Tuple, Dict, Any
from flask import Blueprint, request, jsonify, render_template, url_for
from flask_login import login_required
from werkzeug.utils import redirect
from app.dominios.Entrada.controller import Criar as Criar_entrada, get as get_entrada,\
    get_por_id as get_entrada_por_id, atualizar as atualizar_entrada
from app.dominios.Produtos.controller import get as get_produtos, get_por_id as get_produto_por_id,\
    atualizar as atualizar_produto
from app.dominios.Fornecedores.controller import get as get_fornecedores

app_entrada = Blueprint('app.entrada', __name__)


@app_entrada.route('/TurtleOrg/Entrada-produtos', methods=['POST', 'GET'])
@login_required
def post() -> Tuple[Any]:
    produtos = get_produtos()
    fornecedores = get_fornecedores()
    if request.method == 'POST':
        produto = request.form['produto']
        fornecedor = request.form['fornecedor']
        quantidade = request.form['quantidade']
        nome_produto = get_produto_por_id(produto)
        data = {'produto_id': produto, 'nome_produto': nome_produto.nome, 'fornecedor_id': fornecedor,
                'quantidade': quantidade}
        produto = get_produto_por_id(produto)
        prod_atual = atualizar_produto(produto.id, quantidade, 'entrada')
        if prod_atual:
            entrada = Criar_entrada(data)
            if entrada:
                return render_template('home.html')
    return render_template('Entrada.html', list_forn=fornecedores, list_prod=produtos)


@app_entrada.route('/TurtleOrg/Pesquisa-entrada', methods=['GET'])
@login_required
def get() -> Tuple[Any]:
    entradas = get_entrada()
    if entradas:
        return render_template('MostrarEntrada.html', lista_entrada=entradas)
    else:
        return render_template('home.html')


#@app_entrada.route('/TurtleOrg/Pesquisa-entrada/<id>', methods=['GET'])
#@login_required
#def get_by_id(id: str) -> Tuple[Any]:
#    entrada = get_endereco_por_id(id)
#    return jsonify(entrada)
#
#
#@app_entrada.route('/TurtleOrg/Alterar-entrada/<id>', methods=['PUT'])
#@login_required
#def put(id: str) -> Tuple[Any]:
#    entrada = atualizar_endereco(id)
#    return jsonify(entrada)