'''
Dictionary comprehension

Sintaxe:
{chave:valor for valor in iterável}

'''

# Exemplo 1
# Usando dictionary comprehension
print('Exemplo 1 - Usando dictionary comprehension')

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(f'Dictionary comprehension 1: {numeros}')
print(f'Dictionary comprehension 2 (quadrado dos valores): {quadrado}')

print('\n\n')

# Exemplo 2
# Usando dictionary comprehension 2
print('Exemplo 2 - Usando dictionary comprehension 2')

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(f'Dictionary comprehension 1: {mistura}')

print('\n\n')

# Exemplo 3
# Usando dictionary comprehension com if
print(f'Exemplo 3 - Usando dictionary comprehension com "if"')

lista_ex3 = [1, 2, 3, 4, 5]

pares = {i: ('Par' if not i % 2 else 'ímpar') for i in lista_ex3}

print(pares)