from datetime import datetime

from sqlalchemy.orm import relationship
from database.database import db

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Date


class Saida(db.Model):
    __tablename__ = "saida"

    id = Column(Integer(), default=lambda: str(), primary_key=True)
    produto_fk = Column(Integer(), ForeignKey('produto.id'))
    produto = relationship('Produto', back_populates="saida")
    nome_produto = Column(String(), nullable=False)
    quantidade = Column(Integer(), nullable=False)
    dataSaida = Column(Date(), default=datetime.now)
    cliente = relationship('Cliente', back_populates='saida')
    cliente_fk = Column(Integer(), ForeignKey('cliente.id'))
    nomecliente = Column(String(100), nullable=False)

    def serialize(self):
        return {'nome_produto': self.nome_produto,
                'quantidade':self.quantidade,
                'dataSaida': self.dataSaida,
                'cliente':self.nomecliente,
                'rua_destinatario': self.cliente.endereco.rua}
