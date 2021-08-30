from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database.database import db


class Produto(db.Model):
    __tablename__ = 'produto'

    id = Column(Integer(), primary_key=True)
    nome = Column(String(80), nullable=False)
    descricao = Column(String(200), nullable= True)
    preco = Column(Float(), nullable= False)
    peso = Column(Float())
    categoria_fk = Column(Integer(), ForeignKey("categoria.id"))
    categoria = relationship('Categoria', back_populates="produto")
    nome_categoria = Column(String(100))
    quantidade = Column(Integer())
    quantidademinima = Column(Integer(), nullable=False)
    validade = Column(Date())
    saida = relationship('Saida', back_populates="produto")
    entrada = relationship('Entrada', back_populates="produto")

    def serialize(self):
        return {'id': self.id,
                'nome': self.nome,
                'descricao': self.descricao,
                'peso': self.peso,
                'preco': self.preco,
                'categoria': self.categoria.nome,
                'quantidade': self.quantidade,
                'quantidademinima': self.quantidademinima}
