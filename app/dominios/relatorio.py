from app.dominios.Entrada.controller import get as get_entrada
from app.dominios.Saida.controller import get as get_saida

from flask import Blueprint, request, render_template

app_relatorio = Blueprint('app.relatorio', __name__)


@app_relatorio.route('/TurtleOrg/relatorio', methods=['GET', 'POST'])
def gerar_relatorio():
    if request.method == 'POST':
        opcao = request.form['opcao']
        if opcao == 'entrada':
            entradas = get_entrada()
            render_template('PesquisaEntrada.html', lista=entradas)
        elif opcao == 'saida':
            saidas = get_saida()
            render_template('PesquisaSaida.html', lista=saidas)
    render_template('Relatorio.html')