'''
Map object
- Fazer mapeamentoòde valores para função
- É uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável
- Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função para os elementos do iterável
- Retorna um Map Object
- Após a primeira utilização do resultado do map(), ele zera.
'''

import math

# Exemplo 1
# Usando o "map"
print('Exemplo 1 - Usando o "map"')


# Criando a função
def area(r):
    '''Calcula a área de um circulo com raio "r"'''
    return math.pi * (r ** 2)


print('Usando a função com valores separadamente')
print(f'Raio 2: {area(2)}')
print(f'Raio 5.3: {area(5.3)}')

print('\n')

# Criando uma lista com os valores
lista_raios = [1, 2, 3 , 5.1, 0.3, 10, 44]
print(f'Lista dos raios: {lista_raios}')

print('\n')

print('Usando a função com valores separadamente (usando o "for") - forma comum')

areas = []
for r in lista_raios:
    areas.append((area(r)))

print(f'Lista das áreas: {areas}') 
print(f'Tipo de dado: {type(areas)}') 

print('\n')

# Usando map
print('Usando o "map"')

areas = map(area, lista_raios)

print(f'Retorno do "map": {areas}')
print(f'Tipo do retorno do "map": {type(areas)}')
print(f'Convertendo para uma lista (1° uso): {list(areas)}')  #Convertendo para uma lista o valor do map
print(f'Convertendo para uma lista (2° uso): {list(areas)}')  # Retorna vazio pois com o map o valor é usado apenas uma vez

print('\n')

# Map com lambda
print(f'Lambda com "map"')
print(f'Usando o lambda: {list(map(lambda raio: math.pi * (raio ** 2), lista_raios))}')

print('\n\n')

# Exemplo 2 
# Para fixar map
print('Exemplo 2 - Para fixar o "map"')
cidades = [('Berlim', 25), ('Cairo', 42), ('Buenos Aires', 16), ('Los Angeles', 32), ('Tokio', 21), ('Nova York', 29), ('Londes', 23)]

print(f'Lista (uma lista com tuplas dentro): {cidades}')

# Conversão para Fahrenheit: 
# fahrenheit = 9/5 * celsius + 32

celsius_para_fahrenheit = lambda graus_celsius: (graus_celsius[0], (9/5) * graus_celsius[1] + 32)

print(list(map(celsius_para_fahrenheit, cidades)))
