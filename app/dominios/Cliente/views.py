from typing import Tuple, Dict, Any
from flask import Blueprint, request, jsonify, render_template, url_for
from flask_login import login_required
from werkzeug.utils import redirect
from app.dominios.Cliente.controller import Criar as Criar_destinatario, get as get_destinatario,\
    get_por_id as get_destinatario_por_id, atualizar as atualizar_destinatario
from app.dominios.Endereco.controller import Criar as criar_end, get_por_id as get_end_id, \
    atualizar as atualizar_end

app_destinatario = Blueprint('app.destinatario', __name__)


@app_destinatario.route('/TurtleOrg/Cadastro-destinatario', methods=['POST', 'GET'])
@login_required
def post() -> Tuple[Any, int]:
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        cep = request.form['cep']
        complemento = request.form['complemento']
        numero = request.form['numero']
        end = criar_end({'cep': cep, 'complemento': complemento, 'numero': numero})
        if end:
            destinatario = Criar_destinatario(nome, telefone, email, end.id)
            if destinatario:
                render_template('home.html')
            render_template('CadastroCliente.html')
    return render_template('CadastroCliente.html')


@app_destinatario.route('/TurtleOrg/Pesquisa-destinatario', methods=['GET'])
@login_required
def get() -> Tuple[Any]:
    clientes = get_destinatario()
    return render_template('PesquisaCliente.html', clientes=clientes)


@app_destinatario.route('/TurtleOrg/Pesquisa-destinatario/<id>', methods=['GET'])
@login_required
def get_by_id(id: str) -> Tuple[Any]:
    cliente = get_destinatario_por_id(id)
    clientes = [cliente]
    return render_template('PesquisaCliente.html', clientes=clientes)


@app_destinatario.route('/TurtleOrg/Alterar-destinatario/<id>', methods=['POST', 'GET'])
@login_required
def put(id: int) -> Tuple[Any]:
    id_d = id
    cliente = get_destinatario_por_id(id_d)
    end = get_end_id(cliente.endereco_fk)
    if request.method == 'POST':
        id_cliente = request.form['id_for']
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        cep = request.form['cep']
        complem = request.form['complemento']
        num = request.form['numero']
        if end.cep == cep:
            novo_cli = atualizar_destinatario(id_cliente, nome, telefone, email, end.id)
            end = atualizar_end(end.id, end.rua, num, end.cidade, end.bairro, complem, end.cep, end.estado)
            if novo_cli:
                destinatarios = get_destinatario()
                return render_template('PesquisaCliente.html', clientes=destinatarios)
            else:
                return render_template('AlterarCliente.html', fornecedor=cliente)
        else:
            dados = {'cep': cep, 'complemento': complem, 'numero': num}
            new_end = criar_end(dados)
            novo_cli = atualizar_destinatario(id_cliente, nome, telefone, email, new_end.id)
            if novo_cli:
                destinatarios = get_destinatario()
                return render_template('PesquisaCliente.html', lista=destinatarios)
            else:
                return render_template('AlterarCliente.html', fornecedor=cliente, endereco=end)
    return render_template('AlterarCliente.html', cliente=cliente, endereco=end)
