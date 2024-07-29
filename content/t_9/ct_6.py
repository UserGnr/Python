'''
Generator Expression

- Não há o Tuple Comprehension pois ela é chamda de Generator
- Tem uma eficiência maior em comparação as Comprehension em alguns aspectos, por exemplo em questão da memória ocupada
'''

# Exemplo 1
# Usando o generator
print('Exemplo 1 - Usando o generator')

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(f'Lista: {nomes}')
print('\n')

print('Exemplo com List Comprehension')
res = [nome[0] == 'C' for nome in nomes]
print(f'List Comprehension: {res}')
print(f'Tipo: {type(res)}')

print(f'Exemplo usando o "any": {any([nome[0] == 'C' for nome in nomes])}')

print('\n')

print('Exemplo com generator')

res = (nome[0] == 'C' for nome in nomes)
print(f'Generator: {res}')
print(f'Tipo: {type(res)}')

print(f'Exemplo usando o "any": {any(nome[0] == 'C' for nome in nomes)}')

print('\n\n')

# Exemplo 2
# Usando "getsizeof"
# Retorna a quantidade de bytes em memória do elemento
print('Exemplo 2 - Usando "getsizeof"')

from sys import getsizeof

print('Usando o "getsizeof"')
print(getsizeof('Nome'))
print(getsizeof('Um nome qualquer'))
print(getsizeof(5))
print(getsizeof(97))
print(getsizeof(9354165668823))
print(getsizeof(True))

print('\n')

print('Comparando os tipos a alocação de memória para tiferentes tipos de dados')
# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para a mesma tarefa tem em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

print('\n\n')

# Exemplo 3
# Iterando em um generator
print('Exemplo 4 - Iterando em um generator')

gen = (x * 10 for x in range(1000))
print(f'Imprimindo o generator:{gen}')
print(f'Tipo: {type(gen)}')

for num in gen:
    print(num, end=', ')
