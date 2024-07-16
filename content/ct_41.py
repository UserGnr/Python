'''
Min e max

max(): retorna o maior valor em um iterável ou o maior valor de dois ou mais elemento.
min(): retorna o menor valor em um iterável ou o menor valor de dois ou mais elemento.
'''

# Exemplo 1
# Usando o max e min
print('Exemplo 1 -')

lista = [1, 8, 4, 99, 34, 129]
print(f'Lista 1: {lista}')  # 129
print(f'Lista 1 (max): {max(lista)}')  # 129
print(f'Lista 1 (min): {min(lista)}')  # 129

tupla = (1, 8, 4, 99, 34, 129)
print(f'Tupla 1: {tupla}')  # 129
print(f'Tupla 1 (max): {max(tupla)}')  # 129
print(f'Tupla 1 (min): {min(tupla)}')  # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(f'Conjunto 1: {conjunto}')  # 129
print(f'Conjunto 1 (max): {max(conjunto)}')  # 129
print(f'Conjunto 1 (min): {min(conjunto)}')  # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(f'Dicionário 1 (chave): {dicionario}')  # f
print(f'Dicionário 1 (max): {max(dicionario)}')  # f
print(f'Dicionário 1 (min): {min(dicionario)}')  # f

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(f'Dicionário 2 (valor): {dicionario}')  # 129
print(f'Dicionário 2 (max): {max(dicionario.values())}')  # 129
print(f'Dicionário 2 (min): {min(dicionario.values())}')  # 129

# val1 = int(input('Informe o primeiro valor: '))
# val2 = int(input('Informe o segundo valor: '))
# print('Valores inputados:')
# print(f'Max: {max(val1, val2)}')
# print(f'Min: {min(val1, val2)}')

print('Valores: 4, 67, 54')
print(f'Max: {max(4, 67, 54)}')
print(f'Min: {min(4, 67, 54)}')


print("Valores: 'a', 'ab', 'abc'")
print(f"Max: {max('a', 'ab', 'abc')}")
print(f"Min: {min('a', 'ab', 'abc')}")

print("Valores: 'a', 'b', 'c', 'g'")
print(f"Max: {max('a', 'b', 'c', 'g')}")
print(f"Min: {min('a', 'b', 'c', 'g')}")

print("Valores: 3.145, 5.789")
print(f'Max: {max(3.145, 5.789)}')
print(f'Min: {min(3.145, 5.789)}')

print("Valores: 'Um texto qualquer'")
print(f"Max: {max('Um texto qualquer')}")
print(f"Min: {min('Um texto qualquer')}")    # É considerado o espaço como o menor para essa string

lista2 = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(f'Lista 2: {lista2}')

print(f'Max (pela primeira letra): {max(lista2)}')  # Tim
print(f'Min (pela primeira letra):{min(lista2)}')  # Arya
print(f'Max (pela qtd de caracteres): {max(lista2, key=lambda nome: len(nome))}')  # Ollivander
print(f'Min (pela qtd de caracteres){min(lista2, key=lambda nome: len(nome))}')  # Tim

print('\n\n')

# Exemplo 2
# Exemplo mais complexo
print('Exemplo 2 - Exemplo mais complexo')

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
]

print(f'Musicas: {musicas}')

print('Quantidade de vezes tocadas')
print(f'Max: {max(musicas, key=lambda musica: musica['tocou'])}')
print(f'Min: {min(musicas, key=lambda musica: musica['tocou'])}')

print('O título da música mais e menos tocada')
print(f'Max: {max(musicas, key=lambda musica: musica['tocou'])['titulo']}')
print(f'Min: {min(musicas, key=lambda musica: musica['tocou'])['titulo']}')

print('\n\n')

print('Música mais e menos tocada sem usar max(), min() e lambda')

print('Max:')
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])


print('Min:')
min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
