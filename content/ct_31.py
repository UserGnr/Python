'''
Listas aninhadas (nested lists)

- Em outras linguagens de programação, como C e Java, possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);
Em Python existe as Listas
    numeros = [1, 'b', 3.234, True, 5]  Unidimensional
    numeros = [1, 2, 3]  Unidimensional
    numeros = [[1, 2, 3], [1, 2, 3], [1, 2, 3]] Multidimensional
    - Lista dentro de lista
'''

# Exemplo 1
# Usando listas aninhadas
print('Exemplo 1 - Usando listas aninhadas')

numeros_ex1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f'Listas aninhada 1: {numeros_ex1}')
print(f'Valor [0][1]: {numeros_ex1[0][1]}') # 2
print(f'Valor [2][1]: {numeros_ex1[2][1]}') # 8

print('\n\n')

# Exemplo 2
# Iterando em listas aninhadas com "for"
print('Exemplo 2 - Iterando em listas aninhadas com "for"')

numeros_ex2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f'Listas aninhada 1: {numeros_ex2}')

print('Apenas os números:')
for lista in numeros_ex2:
    for numero in lista:
        print(numero)

print('\n\n')

# Exemplo 3
# Iterando em listas aninhadas com list comprehension
print('Exemplo 3 - Iterando em listas aninhadas com list comprehension')
# Exemplo do funcionamento:
# [[print(valor) for valor in lista] for lista in listas]

numeros_ex3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f'Listas aninhada 1: {numeros_ex3}')
print('Apenas os números:')
[[print(numero) for numero in lista] for lista in numeros_ex3]

print('\n\n')

# Exemplo 4
# Criando uma lista aninhada com list comprehension e com for
print('Exemplo 4 - Criando uma lista aninhada com "sfor"')

# Com list comprehension
numeros_ex4 = [[numero for numero in range(3)] for valor in range(3)]
print(numeros_ex4)

# Com for
a = []
b =[]

for valor in range(3):
    for numero in range(3):
        b.append(numero)
    a.append(b.copy())
    b.clear()

print(a)
