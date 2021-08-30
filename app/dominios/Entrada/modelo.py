from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from database.database import db


class Entrada(db.Model):
    __tablename__ = 'entrada'

    id = Column(db.Integer(), primary_key=True)
    produto = relationship('Produto', back_populates="entrada")
    produto_fk = Column(db.Integer(), ForeignKey('produto.id'))
    nome_produto = Column(db.String(), nullable=False)
    quantidade = Column(db.Integer(), nullable=False)
    dataEntrada = Column(db.DateTime, default=datetime.now)
    fornecedor_fk = Column(db.Integer(), ForeignKey('fornecedor.id'))
    fornecedor = relationship('Fornecedor', back_populates="entrada")

    def serialize(self):
        return {
                'nome_produto': self.nome_produto,
                'quantidade':self.quantidade,
                'dataEntrada': self.dataEntrada,
                'fornecedor':self.fornecedor.serialize}