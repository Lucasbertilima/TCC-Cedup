#Base = declarative_base()
#engine = db.create_engine("mysql+mysqlconnector://root:@localhost:3306/almoxarifado", echo=True)
#Session = sessionmaker(bind=engine)
#session = Session()
#db = SQLAlchemy(app)
from flask_sqlalchemy import SQLAlchemy

from app import  app

db = SQLAlchemy(app)
_session = db.session


def salvar(modelo: db.Model):
    _session.add(modelo)
    commit()
    return modelo


def commit():
    _session.commit()
