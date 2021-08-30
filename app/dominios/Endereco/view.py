from typing import Tuple, Dict, Any
from flask import Blueprint, request, jsonify
from app.dominios.Endereco.controller import Criar as Criar_endereco, get as get_endereco,\
    get_por_id as get_endereco_por_id, atualizar as atualizar_endereco

app_endereco = Blueprint('app.endereco', __name__)


@app_endereco.route('/TurtleOrg/Cadatro-endereco', methods=['POST'])
def post() -> Tuple[Any]:
    payload = request.get_json()
    endereco = Criar_endereco(payload)
    return jsonify(endereco), 200


@app_endereco.route('/TurtleOrg/Pesquisa-endereco', methods=['GET'])
def get() -> Tuple[Any]:
    endereco = get_endereco()
    return jsonify(endereco)


@app_endereco.route('/TurtleOrg/Pesquisa-endereco/<id>', methods=['GET'])
def get_by_id(id: str) -> Tuple[Any]:
    endereco = get_endereco_por_id(id)
    return jsonify(endereco)


@app_endereco.route('/TurtleOrg/Alterar-endereco/<id>', methods=['PUT'])
def put(id: str) -> Tuple[Any]:
    endereco = atualizar_endereco(id)
    return jsonify(endereco)