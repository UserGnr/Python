'''
Módulo random

- Possui várias funções para geração de números pseudo-aleatório
- pseudo-aleatório: pode repetir um número aleatório
- Esse módulo é um Builtin, pois já vem por padrão na linguagem Python
'''

# Exemplo 1
# Gerando números pseudo-aleatórios entre 0 e 1 com "random"
print('Exemplo 1 - Gerando números aleatórios entre 0 e 1 com "random"')

from random import random

for i in range(10):
    print(random())

print('\n\n')

# Exemplo 2
# Gerar um número real pseudo-aleatório entre os valores estabelecidos com uniform
print('Exemplo 2 - Gerar um número real pseudo-aleatório entre os valores estabelecidos com "uniform"')

from random import uniform

for i in range(10):
    print(uniform(5, 10))  # 10 não é incluído.

print('\n\n')

# Exemplo 3
# Gerar valores inteiros pseudo-aleatórios entre os valores estabelecidos com randint
print('Exemplo 3 - Gerar valores inteiros pseudo-aleatórios entre os valores estabelecidos com "randint"')

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')  # começa em 1 e vai até 60

print('\n\n')

# Exemplo 4
# Mostra um valor aleatório entre um iterável com choice
print('Exemplo 4 - Mostra um valor aleatório entre um iterável com "choice"')

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(f'Lista: {jogadas}')
print(choice(jogadas))

print('\n\n')

# Exemplo 5
# Embaralhar dados com shuffle
print('Embaralhar dados com "shuffle"')

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(f'Lista de cartas: {cartas}')

shuffle(cartas)
print(f'Lista de cartas (embaralhado): {cartas}')
print(f'Removendo um item: {cartas.pop()}')
print(f'Lista de cartas (embaralhado sem um item): {cartas}')
