from typing import Tuple, Dict, Any
from flask import Blueprint, request, jsonify, url_for, render_template
from flask_login import login_required
from werkzeug.utils import redirect
from app.dominios.Fornecedores.controller import Criar as Criar_fornecedor, get as get_fornecedor,\
    get_por_id as get_fornecedor_por_id, atualizar as atualizar_fornecedor
from app.dominios.Endereco.controller import Criar as Criar_endereco, get_por_id as get_end_id,\
    atualizar as atualizar_end

app_fornecedor = Blueprint('app.fornecedor', __name__)


@app_fornecedor.route('/TurtleOrg/Cadastro-fornecedor', methods=['POST', 'GET'])
@login_required
def post() -> Tuple[Any]:
    from flask import render_template
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        cep = request.form['cep']
        complemento = request.form['complemento']
        numero = request.form['numero']
        endereco = Criar_endereco({'cep': cep, 'complemento': complemento, 'numero': numero})
        if endereco:
            fornecedor = Criar_fornecedor(nome, telefone, email, endereco.id)
            if fornecedor:
                return render_template('home.html')
            return render_template('CadastroFornecedor.html')

    return render_template('CadastroFornecedor.html')


@app_fornecedor.route('/TurtleOrg/Pesquisa-fornecedor', methods=['GET'])
@login_required
def get() -> Tuple[Any]:
    lista = get_fornecedor()
    return render_template('PesquisaFornecedor.html', lista=lista)


@app_fornecedor.route('/TurtleOrg/Pesquisa-fornecedor/<id>', methods=['GET'])
@login_required
def get_by_id(id: str) -> Tuple[Any]:
    fornecedor = get_fornecedor_por_id(id)
    lista = [fornecedor]
    return render_template('PesquisaFornecedor.html', lista=lista)


@app_fornecedor.route('/TurtleOrg/Alterar-fornecedor/<id>', methods=['POST', 'GET'])
@login_required
def put(id: int) -> Tuple[Any]:
    id_p = id
    fornecedor = get_fornecedor_por_id(id_p)
    end = get_end_id(fornecedor.endereco_fk)
    if request.method == 'POST':
        id_fornecedor = request.form['id_for']
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        cep = request.form['cep']
        complem = request.form['complemento']
        num = request.form['numero']
        if end.cep == cep:
            novo_forn = atualizar_fornecedor(id_fornecedor, nome, telefone, email, end.id)
            end = atualizar_end(end.id, end.rua, num, end.cidade, end.bairro, complem, end.cep, end.estado)
            if novo_forn:
                fornecedores = get_fornecedor()
                return render_template('PesquisaFornecedor.html', lista=fornecedores)
            else:
                return render_template('AlterarFornecedor.html', fornecedor=fornecedor)
        else:
            dados = {'cep': cep, 'complemento': complem, 'numero': num}
            new_end = Criar_endereco(dados)
            novo_forn = atualizar_fornecedor(id_fornecedor, nome, telefone, email, new_end.id)
            if novo_forn:
                fornecedores = get_fornecedor()
                return render_template('PesquisaFornecedor.html', fornecedores=fornecedores)
            else:
                return render_template('AlterarFornecedor.html', fornecedor=fornecedor)
    return render_template('AlterarFornecedor.html', fornecedor=fornecedor, endereco=end)
