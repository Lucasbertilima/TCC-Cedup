from app.dominios.Endereco.modelo import Endereco
from database.database import salvar
from typing import List
from pycep_correios import consultar_cep, CEPInvalido


def Criar(dados: dict) -> Endereco:
    try:
        dict_cep = consultar_cep(dados['cep'])
        endereco = Endereco(rua=dict_cep['end'],
                            numero=dados['numero'],
                            bairro=dict_cep['bairro'],
                            complemento=dados['complemento'],
                            cep=dados['cep'],
                            cidade=dict_cep['cidade'],
                            estado=dict_cep['uf'])
        return salvar(endereco)
    except CEPInvalido:
        return  ('O CEP inserido não existe. Digite outro valido')


def get() -> List[Endereco]:
    return Endereco.query.all()


def get_por_id(id: str) -> Endereco:
    return Endereco.query.get(id)


def atualizar(id_endereco: int, rua, numero, cidade, bairro, complemento, cep, estado) -> Endereco:
    endereco = get_por_id(id_endereco)
    endereco.rua = rua
    endereco.numero = numero
    endereco.bairro = bairro
    endereco.complemento = complemento
    endereco.cep = cep
    endereco.cidade = cidade
    endereco.estado = estado
    return salvar(endereco)
