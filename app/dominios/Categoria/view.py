from typing import Tuple, Dict, Any
from flask import Blueprint, request, jsonify, render_template, url_for
from werkzeug.utils import redirect

from app.dominios.Categoria.controller import Criar as Criar_categoria, get as get_categoria,\
    get_por_id as get_categoria_por_id, atualizar as atualizar_categoria

app_categoria = Blueprint('app.categoria', __name__)


@app_categoria.route('/TurtleOrg/Cadastro-categoria', methods=['POST', 'GET'])
def post() -> Tuple[Any, int]:
    if request.method == 'POST':
        nome = request.form['nome']
        destinatario = Criar_categoria(nome)
        if destinatario:
            render_template('home.html')
    return render_template('CadastroCategoria.html')


@app_categoria.route('/TurtleOrg/Pesquisa-categoria', methods=['GET'])
def get() -> Tuple[Any]:
    return jsonify(categoria.serialize() for categoria in get_categoria())


@app_categoria.route('/TurtleOrg/Pesquisa-categoria/<id>', methods=['GET'])
def get_by_id(id: str) -> Tuple[Any]:
    categoria = get_categoria_por_id(id)
    return jsonify(categoria.serialize())


@app_categoria.route('/TurtleOrg/Alterar-categoria/<id>', methods=['PUT'])
def put(id: str) -> Tuple[Any]:
    categoria = atualizar_categoria(id)
    return jsonify(categoria.serialize())