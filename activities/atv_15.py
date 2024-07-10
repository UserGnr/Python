# 15 - Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor

repetir: int = 1

while repetir:
    numero:int = []
    numero.append(int(input('Informe um número inteiro: ')))

    repetir = int(input('Deseja digitar outro número? [0] - Não [1] - Sim: '))

def maior_numero(*args):
    return max(args)

print(f'O maior número é: {maior_numero(*numero)}')
