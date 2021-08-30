from flask import Flask, render_template, url_for, request
from flask_login import login_user, logout_user, LoginManager, login_required
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash

from app.dominios.Endereco.view import app_endereco
from app.dominios.Categoria.view import app_categoria
from app.dominios.Cliente.views import app_destinatario
from app.dominios.Entrada.views import app_entrada
from app.dominios.Fornecedores.view import app_fornecedor
from app.dominios.Produtos.view import app_produtos
from app.dominios.Saida.views import app_saida


from app.dominios.Usuario.modelo import Usuario
from app.dominios.Usuario.controller import Criar as criar_usuario
from app import app


login_manager = LoginManager(app)

@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@login_manager.user_loader
def get_user(user_id):
    return Usuario.query.filter_by(id=user_id).first()


@app.route('/', methods=['GET', 'POST'])
def register():
    from app.dominios.Usuario.controller import get_by_name as get_nome_usuario
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        confirm = request.form['confirm']
        if senha != confirm:
            return 'As senhas tem que ser iguais'
        dict_user = {'Nome': nome, 'senha': senha, 'confirm': confirm}
        usuario = criar_usuario(dict_user)
        return redirect(url_for('login'))

    return render_template('CadastroUsuario.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    from app.dominios.Usuario.controller import get_by_name as get_nome_usuario
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        user = get_nome_usuario(nome)
        print(user.nome)
        print(senha)
        print(check_password_hash(user.senha, senha))
        if not user:
            return render_template('Login.html')
        else:
            if user.verificar_senha(senha):
                login_user(user)
                return render_template('home.html')
            else:
                return render_template('Login.html')

    return render_template('Login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.register_blueprint(app_produtos)
    app.register_blueprint(app_saida)
    app.register_blueprint(app_fornecedor)
    app.register_blueprint(app_endereco)
    app.register_blueprint(app_entrada)
    app.register_blueprint(app_destinatario)
    app.register_blueprint(app_categoria)
    app.run(debug=True)