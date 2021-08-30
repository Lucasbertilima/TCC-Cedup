from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from database.database import db
from app.dominios.Endereco.modelo import Endereco
from app.dominios.Entrada.modelo import Entrada


class Fornecedor(db.Model):
    __tablename__ = 'fornecedor'

    id = Column(Integer(), primary_key=True)
    nome = Column(String(55), nullable=False)
    telefone = Column(Integer(), nullable=False)
    email = Column(String(55), nullable=False)
    endereco_fk = Column(Integer(), ForeignKey('endereco.id'))
    endereco = relationship('Endereco', back_populates='fornecedor')
    entrada = relationship('Entrada', back_populates='fornecedor')

    def serialize(self):
        return {'id': self.id,
                'nome': self.nome,
                'telefone': self.telefone,
                'email':self.email,
                'endereco_id': self.endereco.id}

