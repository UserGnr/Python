# 4 - Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

texto = 'Digite um número inteiro: '

numero_1, numero_2 = int(input(texto)), int(input(texto))

if numero_1 is numero_2:
    print('O número 1 é igual ao número 2')
elif numero_1 > numero_2:
    print('O número 1 é maior que o número 2')
elif numero_1 < numero_2:
    print('O número 1 é menor que o número 2')
