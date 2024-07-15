'''
Sorted

- A função sort() usada apenas em listas é diferente de sorted()
- Podemos utilizar o sorted() com qualquer iterável
- Sorted() serve para ordenar
- Retorna uma Lista com os elementos do iterável ordenados
'''

# Exmeplo 1
# Usando sorted
print('Exeplo 1 - Usando "sorted"')

conjunto1 = {6, 1, 8, 2}
print(f'Números: {conjunto1}')

print(f'Conjunto | Odenando (maior para o menor): {sorted(conjunto1)}')


lista1 = [6, 1, 8, 2]
print(f'Lista | Ordenando (maior para o menor): {sorted(lista1)}')

print('\n\n')

# Exemplo 2
# Invertendo a ordem com sorted()
print('Exemplo 2 - Invertendo a ordem com "sorted"')

lista2 = [6, 1, 8, 2]

print(f'Lista 2: {lista2}')
print(f'Lista 2 (crescente): {sorted(lista2)}')  # Ordena do menor para o menor
print(f'Lista 2 (decrescente): {sorted(lista2, reverse=True)}')  # Ordena do maior para o menor

print('\n\n')

# Exemplo 3
# Adicionando parâmetros ao sorted()
print('Exemplo 3 - Adicionando parâmetros ao "sorted"')


lista3 = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(f"Lista 3: {lista3}")

# Ordenando por username - Ordem Alfabética
print('Odenando por username em ordem alfabética:')
print(sorted(lista3, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print('Odenando pelo número de tweets')
print(sorted(lista3, key=lambda usuario: len(usuario["tweets"])))

print('\n\n')

# Exemplo 4
# Adicionando parâmetros ao sorted() 2
print('Exemplo 4 - Adicionando parâmetros ao "sorted" 2')

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
]

# Ordena da menos tocada para a mais tocada
print('Ordena da menos tocada para a mais tocada:')
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print('Ordena da menos tocada para a mais tocada:')
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
