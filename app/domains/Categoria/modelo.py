from database import db    


class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    nome = db.Column(db.String(55), nullable=False)