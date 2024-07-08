# 12 - Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele possui.

lista: list[int] = []

while len(lista) < 10:
    valor: int = int(input(f'Informe um número inteiro ({len(lista)+1} de 10): '))
    lista.append(valor)


par: list[int] = []

for valor in lista:
    if valor % 2 == 0:
        par.append(valor)

print(f'Os valores informados são: {lista}')
print(f'Os valores pares são: {par}')
print(f'O total de números pares são: {len(par)}')
