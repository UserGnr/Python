# 2 - Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.

texto = 'Digite um número inteiro: '
numero1, numero2, numero3 = int(input(texto)), int(input(texto)), int(input(texto))
soma: int = numero1 + numero2 + numero3

print(f'A soma dos números digitados {numero1,numero2,numero3} é {soma}')
