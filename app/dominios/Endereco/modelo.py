from sqlalchemy.orm import relationship
from sqlalchemy import *
from database.database import db


class Endereco(db.Model):
    __tablename__ = "endereco"

    id = Column(Integer(), primary_key=True)
    rua = Column(String(100), nullable=False)
    numero = Column(String(50), nullable=True)
    bairro = Column(String(50), nullable=True)
    complemento = Column(String(300), nullable=True)
    cep = Column(String(11), nullable=False)
    cidade = Column(String(50), nullable=False)
    estado = Column(String(50), nullable=False)
    fornecedor = relationship('Fornecedor', uselist=False, back_populates='endereco')
    cliente = relationship('Cliente', uselist=False, back_populates='endereco')

    def serialize(self):
        return {'rua': self.rua,
                'numero': self.numero,
                'bairro': self.bairro,
                'complemento': self.complemento,
                'cep': self.cep,
                'cidade': self.cidade,
                'estado': self.estado}