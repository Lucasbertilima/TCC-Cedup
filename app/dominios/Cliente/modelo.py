from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.database import db
from app.dominios.Endereco.modelo import Endereco


class Cliente(db.Model):
    __tablename__ = 'cliente'

    id = Column(Integer(), primary_key=True)
    nome = Column(String(80), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    endereco_fk = Column(Integer(), ForeignKey("endereco.id"))
    endereco = relationship("Endereco", back_populates="cliente")
    saida = relationship('Saida', back_populates="cliente")

    def serialize(self):
        return {'id': self.id,
                'nome': self.nome,
                'telefone': self.telefone,
                'email':self.email,
                'endereco': self.endereco}
