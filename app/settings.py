from pycep_correios import consultar_cep
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash

today = date.today()
data = today.strftime("%d/%m/%Y")

senha = input('Informe sua senha')
confirmacao = input('Informe a confirmação de senha')

psw = generate_password_hash(senha)
if confirmacao != check_password_hash(psw, senha):
    print(f'Deu errado {psw}')