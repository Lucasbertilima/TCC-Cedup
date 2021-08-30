from typing import List
from database.database import salvar
from app.dominios.Saida.modelo import Saida
from datetime import date


def Criar(dados: dict) -> Saida:
    saida = Saida(produto_fk=dados['produto_id'],
                    nome_produto=dados['nome_produto'],
                    quantidade=dados['quantidade'],
                    cliente_fk=dados['cliente_id'],
                    nomecliente=dados['nome_cliente'])
    return salvar(saida)


def get() -> List[Saida]:
    return Saida.query.all()


def get_por_id(id: str) -> Saida:
    return Saida.query.get(id)


def atualizar(id_saida: str, dados: dict) -> Saida:
    saida = get_por_id(id_saida)
    saida.nome = dados.get('nome')
    return salvar(saida)
