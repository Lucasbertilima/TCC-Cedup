from typing import List
from datetime import date

from app.dominios.Entrada.modelo import Entrada
from database.database import salvar


def Criar(dados: dict) -> Entrada:
    entrada = Entrada(produto_fk=dados['produto_id'],
                      nome_produto=dados['nome_produto'],
                      quantidade=dados['quantidade'],
                      fornecedor_fk=dados['fornecedor_id'],
                      )
    return salvar(entrada)


def get() -> List[Entrada]:
    return Entrada.query.all()


def get_por_id(id: str) -> Entrada:
    return Entrada.query.get(id)


def atualizar(id_entrada: str, dados: dict) -> Entrada:
    entrada = get_por_id(id_entrada)
    entrada.nome = dados.get('nome')
    return salvar(entrada)