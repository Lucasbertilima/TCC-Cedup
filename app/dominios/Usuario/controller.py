
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from database.database import salvar
from app.dominios.Usuario.modelo import Usuario


def Criar(dados: dict) -> Usuario:
    if dados['senha'] != dados['confirm']:
        return 'A confirmação de senha está diferente. Informe a mesma senha nos dois campos'
    senha = generate_password_hash(dados['senha'])
    produto = Usuario(nome=dados['Nome'],
                      senha=senha)
    return salvar(produto)


def get() -> List[Usuario]:
    return Usuario.query.all()


def get_by_name(nome: str) -> Usuario:
    usuario = Usuario.query.filter_by(nome=nome).first()
    return usuario


def get_por_id(id: str) -> Usuario:
    return Usuario.query.get(id)


def atualizar(id_produto: str, dados: dict) -> Usuario:
    usuario = get_por_id(id_produto)
    usuario.nome = dados.get('nome')

    return salvar(usuario)