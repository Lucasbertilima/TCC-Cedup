#from typing import Tuple, Any
#from flask import Blueprint, request, jsonify, render_template
#from flask_login import login_required, login_manager
#
#from app.dominios.Usuario.controller import Criar as Criar_usuario, get as get_usuario, \
#    get_por_id as get_usuario_por_id, atualizar as atualizar_usuario, get_by_name as get_nome_usuario
#
#from app.dominios.Usuario.modelo import Usuario
#
#app_usuario = Blueprint('app_usuario', __name__)
#
#
#@app_usuario.route('/home')
#@login_required
#def home():
#    return render_template('home.html')
#
#
#@login_manager.user_loader
#def get_user(user_id):
#    return Usuario.query.filter_by(id=user_id).first()
#
#
#@app_usuario.route('/', methods=['GET', 'POST'])
#def register():
#    from app.dominios.Usuario.controller import get_by_name as get_nome_usuario
#    if request.method == 'POST':
#        nome = request.form['nome']
#        senha = request.form['senha']
#        confirm = request.form['confirm']
#        if senha != confirm:
#            return 'As senhas tem que ser iguais'
#        dict_user = {'Nome': nome, 'senha': senha, 'confirm': confirm}
#        usuario = Criar_usuario(dict_user)
#        return redirect(url_for('login'))
#
#    return render_template('CadastroUsuario.html')
#
#
#@app_usuario.route('/login', methods=['GET', 'POST'])
#def login():
#    from app.dominios.Usuario.controller import get_by_name as get_nome_usuario
#    if request.method == 'POST':
#        nome = request.form['nome']
#        senha = request.form['senha']
#
#        user = get_nome_usuario(nome)
#        if not user:
#            redirect(url_for('login'))
#        else:
#            login_user(user)
#        return redirect(url_for('home'))
#
#    return render_template('Login.html')
#
#
#@app_usuario.route('/logout')
#@login_required
#def logout():
#    logout_user()
#    return redirect(url_for('login'))