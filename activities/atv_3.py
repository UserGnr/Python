# 3 - Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.

texto = "Digite um número inteiro: "

numero1, numero2, numero3 = int(input(texto)), int(input(texto)), int(input(texto))
quadrado1: int = numero1 ** numero1
quadrado2: int = numero2 ** numero2
quadrado3: int = numero3 ** numero3
soma_quadrado: int = quadrado1 + quadrado2 + quadrado3

print(f'O primeiro número digitado é {numero1} e seu quadrado é {quadrado1}')
print(f'O segundo número digitado é {numero3} e seu quadrado é {quadrado2}')
print(f'O terceiro número digitado é {numero3} e seu quadrado é {quadrado3}')
print(f'A soma de todos os números quadrados é {soma_quadrado}')
