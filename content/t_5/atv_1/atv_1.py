# 7 - Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.

numero: int = 0
contador: int = 0

while contador < 5:
    numero += 1
    if numero % 3 == 0:
        contador += 1
        print(f'O número {numero} é multiplo de 3')
