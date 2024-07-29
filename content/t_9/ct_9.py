'''
Reversed

- A função reversed() é diferente da reverse()
- A função reverse() só funciona em listas
- A função reversed() funciona com qualquer iterável
- Sua função é inverter o iterável
- A função reversed() retorna um iterável chamado List Reverse Iterator
- É possível converter o elemento retornado para uma Lista, Tupla ou Conjunto
'''

# Exemplo 1
# Usando reversed
print('Exemplo 1 - Usando "reversed"')

lista1 = [1, 2, 3, 4, 5]
print(f'Lista 1: {lista1}')
revers = reversed(lista1)

print(f'Reversed 1: {revers}')
print(f'Reversed 1 (tipo): {type(revers)}')

# Lista
print(f'Lista (reversed): {list(reversed(lista1))}')

# Tupla
print(f'Tupla (reversed): {tuple(reversed(lista1))}')

# Conjunto
print(f'Tupla (reversed): {set(reversed(lista1))}')

print('\n\n')

# Exemplo 2
# Iterando com o "reversed"
print('Exemplo 2 - Iterando com o "reversed"')

print('Teste 1: usando o "for":')
for letra in reversed('Um valor qualquer'):
    print(letra, end='')

print('Teste 2: fazer o mesmo sem o uso do "for":')
print(''.join(list(reversed('Um valor qualquer'))))

print('Teste 3: fazer o mesmo com o slice de strings:')
print('Um valor qualquer'[::-1])

print('Teste 4: utilizar o reversed() para fazer um loop for reverso:')
for n in reversed(range(0, 10)):
    print(n)

#  Fazer o mesmo utilizando o range()
# for n in range(9, -1, -1):
#     print(n)
