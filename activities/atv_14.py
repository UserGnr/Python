# 14 - Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e imprima ela por extenso como “1 de janeiro de 20204”.

data1: str = str(input('Informe uma data no formato dd/mm/yyyy: '))

meses = {
    '1': 'janeiro',
    '2': 'fevereiro',
    '3': 'março',
    '4': 'abril',
    '5': 'maio',
    '6': 'junho',
    '7': 'julho',
    '8': 'agosto',
    '9': 'setembro',
    '0': 'outubro',
    '11': 'novembro',
    '12': 'dezembro'
}


def converter_data(data: str,**kwarg) -> str:  # Retornaria 'None' se o retorno da função imprimisse (print), por exemplo

    lista_data = list(data.split('/'))

    dia: int = int(lista_data[0])
    mes: int = int(lista_data[1])
    ano: int = int(lista_data[2])
    
    for mes_key in kwarg.keys():
        if int(mes_key) == mes:
            return f'{dia} de {kwarg[mes_key]} de {ano}'
    return 'Mês desconhecido'

print(converter_data(data1, **meses))
