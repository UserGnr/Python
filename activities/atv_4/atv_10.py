# 10 - Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores da lista.

lista: list[int] = []

while len(lista) < 6:
    valor: int  = int(input(f"Informe um valor inteiro ({len(lista)+1} de 6): "))
    lista.append(valor)

print(f'Os valores informados são: {lista}')
