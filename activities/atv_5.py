# 5 - Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import math

numero: int = int(input('Digite um número: '))

if numero == 0:
    print('O número informado é zero')
elif numero > 0:
    raiz = math.sqrt(numero)
    print(f'A raíz quadrada de {numero} é {raiz}')
else:
    print('O número informado é inválido')