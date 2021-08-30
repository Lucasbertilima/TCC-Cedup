class DadosInvalidos(Exception):
    def __init__(self, msg: str = 'Os dados inseridos são invalidos. Tente novamente'):
        super().__init__(description=msg)
