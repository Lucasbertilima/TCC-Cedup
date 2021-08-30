from typing import List

from app.dominios.Fornecedores.modelo import Fornecedor
from database.database import salvar
from app.validacoes.validacao import validando_se_dados_estao_corretos
from app.excessoes.excecoes import DadosInvalidos


def Criar(nome: str, telefone: int, email: str, endereco_id: int) -> Fornecedor:

    dados = {'nome': nome, 'telefone': telefone, 'email': email}
    fornecedor = Fornecedor(nome=nome,
                            telefone=telefone,
                            email=email,
                            endereco_fk=endereco_id)
    return salvar(fornecedor)
    #except Exception:
    #    return 'ocorreu um erro'


def get() -> List[Fornecedor]:
    return Fornecedor.query.all()


def get_por_id(id: str) -> Fornecedor:
    return Fornecedor.query.get(id)


def atualizar(id_fornecedor: int, nome, telefone, email, end_fk) -> Fornecedor:
    fornecedor = get_por_id(id_fornecedor)
    fornecedor.nome =nome
    fornecedor.telefone =telefone
    fornecedor.email =email
    fornecedor.endereco_fk = end_fk
    return salvar(fornecedor)
