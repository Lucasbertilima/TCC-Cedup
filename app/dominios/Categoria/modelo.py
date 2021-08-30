from sqlalchemy.orm import relationship
from database.database import db

from sqlalchemy import Column, String, Integer


class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = Column(Integer(), primary_key=True)
    nome = Column(String(55), nullable=False)
    produto = relationship("Produto", back_populates="categoria")

    def serialize(self):
        return {'nome': self.nome}