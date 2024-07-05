# 4 - Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

texto = 'Digite um número inteiro: '

numero_1, numero_2 = int(input(texto)), int(input(texto))

if numero_1 is numero_2:
    print(f'{numero_1} é igual ao {numero_2}')
elif numero_1 > numero_2:
    print(f'{numero_1} é maior que o {numero_2}')
elif numero_1 < numero_2:
    print(f'{numero_1} é menor que o {numero_2}')
