from typing import Tuple, Dict, Any
from flask import Blueprint, request, jsonify, render_template, url_for
from flask_login import login_required
from werkzeug.utils import redirect
from app.dominios.Saida.controller import Criar as Criar_saida, get as get_saida,\
    get_por_id as get_saida_por_id, atualizar as atualizar_saida
from app.dominios.Produtos.controller import get as get_produtos, get_por_id as get_produto_por_id,\
    atualizar as atualizar_produto
from app.dominios.Cliente.controller import get as get_cliente, get_por_id as get_cliente_por_id
from app.validacoes.validacao import validando_se_dados_sao_numeros

app_saida = Blueprint('app.saida', __name__)


@app_saida.route('/TurtleOrg/Saida-produtos', methods=['POST', 'GET'])
@login_required
def post() -> Tuple[Any]:
    produtos = get_produtos()
    clientes = get_cliente()
    if request.method == 'POST':
        produto = request.form['produto']
        clienteid = request.form['cliente']
        quantidade = request.form['quantidade']
        nome_produto = get_produto_por_id(produto)
        quantidade = int(quantidade)
        nome_cliente = get_cliente_por_id(clienteid)
        data = {'produto_id': produto, 'nome_produto': nome_produto.nome, 'cliente_id': clienteid,
                'nome_cliente': nome_cliente.nome, 'quantidade': quantidade}
        produto = get_produto_por_id(produto)
        prod_atual = atualizar_produto(produto.id, quantidade, 'saida')
        if prod_atual:
            saida = Criar_saida(data)
            if saida:
                return render_template('home.html')
    return render_template('Saida.html', list_client=clientes, list_prod=produtos)


@app_saida.route('/TurtleOrg/Pesquisa-saida', methods=['GET'])
@login_required
def get() -> Tuple[Any]:
    saidas = get_saida()
    if saidas:
        return render_template('MostrarSaida.html', lista_saida=saidas)
    else:
        return render_template('home.html')


#@app_saida.route('/TurtleOrg/Pesquisa-saida/<id>', methods=['GET'])
#@login_required
#def get_by_id(id: str) -> Tuple[Any]:
#    fornecedor = get_fornecedor_por_id(id)
#    return jsonify(fornecedor)
#
#
#@app_saida.route('/TurtleOrg/Alterar-fornecedor/<id>', methods=['PUT'])
#@login_required
#def put(id: str) -> Tuple[Any]:
#    fornecedor = atualizar_fornecedor(id)
#    return jsonify(fornecedor)