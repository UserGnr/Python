'''
Dicionários ou mapas (parte 2)
'''

# Exemplo 13
# Iterar sobre dicionários
print('Exemplo 13 - Iterar sobre dicionários')

dicionario1_ex13 = {'jan': 100, 'fev': 120, 'mar': 300}

print(F'Dicionário 1: {dicionario1_ex13}')

for chave in dicionario1_ex13:
    print(f'Chave: {chave} | valor: {dicionario1_ex13[chave]}')

print('\n\n')

# Exemplo 14
# Acessando/iterando as chaves com keys (recomendado)
print('Exemplo 14 - Acessando/iterando as chaves com keys (recomendado)')

dicionario1_ex14 = {'jan': 100, 'fev': 120, 'mar': 300}

print(F'Dicionário 1 (sem "keys"): {dicionario1_ex14}')
print(F'Dicionário 1 (com "keys"): {dicionario1_ex14.keys()}')

for chave in dicionario1_ex13.keys():
    print(f'Chave: {chave} | valor: {dicionario1_ex13[chave]}')

print('\n\n')

# Exemplo 15
# Acessando/iterando os valores com values (recomendado)
print('Exemplo 15 - Acessando/iterando os valores com values (recomendado)')

dicionario1_ex15 = {'jan': 100, 'fev': 120, 'mar': 300}

print(F'Dicionário 1 (sem "values"): {dicionario1_ex15.keys()}')
print(F'Dicionário 1 (com "values"): {dicionario1_ex15.values()}')

for valor in dicionario1_ex15.values():
    print(f'Valor: {valor}')

print('\n\n')

# Exemplo 16
# Desempacotamento de dicionários com items
# Retorna uma lista contendo tuplas
print('Exemplo 16 - Desempacotamento de dicionários com "items"')

dicionario1_ex16 = {'jan': 100, 'fev': 120, 'mar': 300}

print(f'Dicionário 1: {dicionario1_ex16}')
print(f'Dicionário 1 (com items): {dicionario1_ex16.items()}')  

for chave, valor in dicionario1_ex16.items():
    print(f'Chave: {chave} | valor {valor}')

print('\n\n')

# Exemplo 17
# Soma*, valor máximo*, valor mínimo*, tamanho
# * Se os valores forem todos inteiros ou reais
print('Exemplo 17 - Soma, valor máximo, valor mínimo, tamanho')

dicionario1_ex17 = {'jan': 100, 'fev': 120, 'mar': 300}

print(f'Lista 1: {dicionario1_ex17}')

print(f'Soma: {sum(dicionario1_ex17.values())}')
print(f'Valor máximo: {max(dicionario1_ex17.values())}')
print(f'Valor mínimo: {min(dicionario1_ex17.values())}')
print(f'Tamanho: {len(dicionario1_ex17)}')
