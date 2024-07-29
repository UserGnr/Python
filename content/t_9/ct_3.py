'''
Filter

- filter() serve para filtrar dados de uma determinada coleção
- Assim como a funcão map(), a filter() recebe dois parâmetros: uma função e um iterável
- Assim como na função map(), após serem utilizados os dados de filter(), eles são excluídos da memória.

Diferença entre map() e filter() é:
- map(): Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável
- filter(): Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função
'''

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Exemplo 1
# Usando filter
print('Exemplo 1 - Usando "filter"')

# Dados coletados de algum sensor
dados = [1.2, 5.3, 0.4, 6.3, 2.5, -0.8]
print(f'Lista de dados: {dados}')

print('\n')

# Calculando a média dos dados com mean()
print('Calculando a média com "mean"')
media = statistics.mean(dados)
print(f'Média (com "mean"): {media}')

print('Usando filter')
retorno = filter(lambda valor: valor > media, dados)
print(f"Valores que estão acima da média: {list(retorno)}")

print('\n\n')

# Exemplo 2
# Usando filter
print('Exemplo 2 - Usando "filter"')

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(f'Países: {paises}')

res = filter(None, paises)  # Faz com que os dados vazios filtrados não sejam utilizados
# Outras formas de fazer:
# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)

print(f'Retirando so vazios com "filter": {list(res)}')

print('\n\n')

# Exemplo 3
# Usando filter
print('Exemplo 3 - Usando "filter"')

usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(f'Lista de usuários: {usuarios}')

# Filtrar os usuários que estão inativos no Twitter
# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print('Usuários inativos: {inativos}')

print('\n\n')

# Exemplo 4
# Usando filter() e map()
print('Exemplo 4 - Usando "filter" e "map"')

nomes = ['Vanessa', 'Ana', 'Maria']

print(f'Lista de nomes: {nomes}')

# Uma lista contendo 'Sua instrutrura é' + nome, se cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(f'Lista de nomes com menos de 5 caracteres: {lista}')
