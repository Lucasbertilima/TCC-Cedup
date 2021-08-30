from typing import List
from database.database import salvar
from app.dominios.Categoria.modelo import Categoria


def Criar(dados: str) -> Categoria:
    categoria = Categoria(nome=dados)
    return salvar(categoria)


def get() -> List[Categoria]:
    return Categoria.query.all()


def get_por_id(id: str) -> Categoria:
    return Categoria.query.get(id)


def atualizar(id_categoria: str, dados: dict) -> Categoria:
    categoria = get_por_id(id_categoria)
    categoria.nome = dados.get('nome')
    return salvar(categoria)
