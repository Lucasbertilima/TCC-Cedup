from database.database import db
from sqlalchemy import Column, String, Integer
from werkzeug.security import check_password_hash
from flask_login import UserMixin


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'

    id = Column(Integer(),autoincrement=True, primary_key=True)
    nome = Column(String(80), nullable=False)
    senha = Column(String(100), nullable=False)

    def verificar_senha(self, psw):
        return check_password_hash(self.senha, psw)
