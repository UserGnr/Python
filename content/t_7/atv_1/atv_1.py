# 13 - Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.

def dobro(valor: int) -> int:   # '-> int' refere-se ao tipo de retorno
    return valor * 2

numero: int = int(input('Informe um número inteiro: '))

print(f'O dobro de {numero} é {dobro(numero)}')
