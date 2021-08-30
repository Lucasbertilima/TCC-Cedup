from typing import List
from database.database import salvar
from app.dominios.Cliente.modelo import Cliente


def Criar(nome: str, telefone: int, email: str, endereco_id: int) -> Cliente:
    cliente = Cliente(nome=nome,
                          telefone=telefone,
                          email=email,
                          endereco_fk=endereco_id)
    return salvar(cliente)


def get() -> List[Cliente]:
    return Cliente.query.all()


def get_por_id(id: str) -> Cliente:
    return Cliente.query.get(id)


def atualizar(id_cliente: int, nome, telefone, email, end_fk) -> Cliente:
    cliente = get_por_id(id_cliente)
    cliente.nome = nome
    cliente.telefone = telefone
    cliente.email = email
    cliente.endereco_fk = end_fk
    return salvar(cliente)
