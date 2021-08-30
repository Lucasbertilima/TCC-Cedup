from typing import List, Dict, Union, NoReturn


def validando_se_dados_estao_corretos(campos_permitidos: List[str], data: Dict[str, Union[bool, str]]) -> NoReturn:
    count = 0
    for key, value in data.items():
        if value and key in campos_permitidos:
            count += 1
    if count < len(campos_permitidos):
        return False
    else:
        return True

def validando_se_dados_sao_string( data: Dict[str, Union[bool, str]]) -> NoReturn:
    count = 0
    for key, value in data.items():
        if value is str:
            count += 1
    if count != len(data):
        return False
    else:
        return True


def validando_se_dados_sao_numeros(data: Dict[str, Union[bool, str]]) -> NoReturn:
    count = 0
    for key, value in data.items():
        if value is int:
            count += 1
    if count != len(data):
        return False
    else:
        return True