'''
Zip

- Cria um iterável (Zip Object) que agrega elementos em pares de cada um dos iteráveis de entrada
- O zip() utiliza como parâmetro o iterável com menor quantidade de elementos. Isso significa que se estiver trabalhando com iteráveis de tamanhos diferentes, o zip irá parar quando os elementos do menor iterável acarbar
- Após o primeiro uso, é apagado da memória
- É possível utilizar com diferentes iteráveis
'''

# Exemplo 1
# Usando o zip
print('Exemplo 1 - Usando o zip')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 12]

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print('\n')

zip1 = zip(lista1, lista2, 'abc')

print(f'Zip 1: {zip1}')
print(f'Zip 1 (tipo): {type(zip1)}')
print('\n')

print('Convertendo para uma lista')
print(list(zip1))

print('Convertendo para uma tupla')
zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

print('Convertendo para um conjunto')
zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))

print('Convertendo para um dicionário')
zip1 = zip(lista1, lista2)
print(dict(zip1))

print('\n\n')

# Exemplo 2
# Usando diferentes tipos de iteráveis para compor o zip
print('Exemplo 2 - Usando diferentes tipos de iteráveis para compor o "zip"')

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista com tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*dados)))

print('\n\n')

# Exemplo 3
# Exemplos mais complexos
print('Exemplo 3 - Exemplo mais complexo')

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

print('Usando o map')
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
