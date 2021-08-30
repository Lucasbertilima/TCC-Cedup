from flask import Flask
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy


def _register_blueprint(app):
    from app.dominios.Categoria.view import app_categoria
    from app.dominios.Fornecedores.view import app_fornecedor
    from app.dominios.Produtos.view import app_produtos
    from app.dominios.Cliente.views import app_destinatario
    #app.register_blueprint(app_usuario)
    app.register_blueprint(app_categoria)
    app.register_blueprint(app_fornecedor)
    app.register_blueprint(app_produtos)
    app.register_blueprint(app_destinatario)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'almoxarifado'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:@localhost:3306/almoxarifado"
#_register_blueprint(app)
login_manager = LoginManager(app)
#db = SQLAlchemy(app)
