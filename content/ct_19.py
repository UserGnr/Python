'''
Collections -> High-performance Container Datetypes

Counter:
- Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento
 - Podemos usar qualquer tipo de iterável

 Default Dict
 - É um dicionário, porém com algumas diferenças (vide abaixo).
 - Ao criar um dicionário "Default Dict" é possível definir um valor default (padrão) usando o lambda
 - Esse valor será usado sempre que não houver um valor definido
 - Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído. Em um dicionário normal, resultaria em erro
 - Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores
 
 OrderedDict
 - É um dicionário que garante a ordem de inserção dos elementos, visto que um dicionário normal não garante a ordem de inserção
 - Desse modo, para o OrderedDict a ordem importa

 Named Tuple
 - Tupla nomeada
 - São tuplas que tem o um nome e parâmetros

 Deque
 - O deque é uma lista de alta performance

'''

# Realizar o import
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

# Exemplo 1
# Utilizando o Counter
print('Exemplo 1: Utilizando o "Counter"')
lista1_ex1 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]
string1_exe1 = 'Um texto qualquer para Análise'
string3_exe1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(f'Lista 1: {lista1_ex1} | Tipo: {type(lista1_ex1)}')
print(f'String 1: {string1_exe1} | Tipo: {type(string1_exe1)}')
print(f'String 3: {string3_exe1} | Tipo: {type(string3_exe1)}')
print('\n')

# Utilizando o Counter
counter1_ex1 = Counter(lista1_ex1)
counter2_ex1 = Counter(string1_exe1)

string3_exe1_split = string3_exe1.split()
counter3_ex1 = Counter(string3_exe1_split)

# Para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências
print(f'Counter 1 (da lista 1): {counter1_ex1} | Tipo: {type(lista1_ex1)}')
print(f'Counter 2 (da string 1): {counter2_ex1} | Tipo: {type(counter2_ex1)}')
print(f'Counter 3 (da string 2 com split): {counter3_ex1} | Tipo: {type(counter3_ex1)}')
print(f'As 5 palavras com maior ocorrência do Counter 3: {counter3_ex1.most_common(5)}')

print('\n\n')

# Exemplo 2
# Usando o Default Dict
print('Exemplo 2 - Usando o Default Dict')

dicionario1_ex2 = defaultdict(lambda: 0)

print(f'Dicionário 1: {dicionario1_ex2}')

dicionario1_ex2['Chave do texto'] = 'Esse é o texto'

print(f'Dicionário 1 (nova chave/valor da maneira comum): {dicionario1_ex2}')
print(f'Dicionário 1 (pesquisando uma chave que não existe "Nchave"): {dicionario1_ex2['Nchave']}')
print(f'Dicionário 1 (final): {dicionario1_ex2}')   # Aqui é possível ver que a chave 'Nchave' foi criada com o valor padrão 0 dentro do dicionário dicionario1_ex2 apenas por ter sido feito a consulta que em um dicionário comum teria retornado um erro

print('\n\n')

# Exemplo 3
# Usando o OrderedDict
print('Exemplo 3 - Usando o "OrderedDict"')

dicionario1_ex3 = {'a': 1, 'b': 2, 'c': 3}
dicionario2_ex3 = {'a': 1, 'c': 3, 'b': 2}
ordered_dict1_ex3 = OrderedDict({'a': 1, 'b': 2, 'c': 3})
ordered_dict2_ex3 = OrderedDict({'a': 1, 'c': 3, 'b': 2})

print(f'Dicionário 1: {dicionario1_ex3}')
print(f'Dicionário 2 (mudando a ordem): {dicionario2_ex3}')
print(f'OrderedDict 1: {ordered_dict1_ex3}')
print(f'OrderedDict 2 (mudando a ordem): {ordered_dict2_ex3}')

print(f'Comparando o dicionário 1 com o dicionário 2: {dicionario1_ex3==dicionario2_ex3}')
print(f'Comparando o OrderedDict 1 com o OrderedDict 2: {ordered_dict1_ex3==ordered_dict2_ex3}')    # Para o OrderedDict, a ordem importa!

# Exemplo 4
# Usando o namedtuple
print('Exemplo 4 - Usando o namedtuple')

# Formas de declarar a tupla nomeada
namedtuple1_ex4 = namedtuple('namedtuple1_ex4', 'idade raca nome')
namedtuple2_ex4 = namedtuple('namedtuple2_ex4', 'idade, raca, nome')
namedtuple3_ex4 = namedtuple('namedtuple3_ex4', ['idade', 'raca', 'nome'])

print(f'Tupla nomeada 1: {namedtuple1_ex4} | tipo: {type(namedtuple1_ex4)}')
print(f'Tupla nomeada 2: {namedtuple2_ex4} | tipo: {type(namedtuple2_ex4)}')
print(f'Tupla nomeada 3: {namedtuple3_ex4} | tipo: {type(namedtuple3_ex4)}')

# Atribuindo o tipo tupla
tupla_nome = namedtuple3_ex4(idade= 2, raca='Chow-Chow', nome= 'Ray')

print(f'Tupla nome (tupla_nome): {tupla_nome} | tipo: {type(tupla_nome)}')

# Acessando os dados
print('Forma 1 -Acessando os dados')
print(f'Idade: {tupla_nome[0]}')
print(f'Raça: {tupla_nome[1]}')
print(f'Nome: {tupla_nome[2]}')

print('Forma 2 -Acessando os dados')
print(f'Idade: {tupla_nome.idade}')
print(f'Raça: {tupla_nome.raca}')
print(f'Nome: {tupla_nome.nome}')

print('\n\n')

# Exemplo 5
# Usando o deque
print('Exemplo 5 - Usando o "deque')

deque1_ex5 = deque('Um texto qualquer')

print(f'Deque 1: {deque1_ex5} | Tipo: {type(deque1_ex5)}')

# Adicionando elemento no deque
deque1_ex5.append('y')  # Adiciona no final
deque1_ex5.appendleft('x')  # Adiciona no começo

print(f'Deque 1 (adicionando elemento à esquerda e direita): {deque1_ex5} | Tipo: {type(deque1_ex5)}')

pop_valor = deque1_ex5.pop()    # Remove e retorna o último elemento
popleft_valor = deque1_ex5.popleft()    # Remove e retorna o primeiro elemento

print(f'Deque 1 (removendo elemento à esquerda e direita): {deque1_ex5} | Tipo: {type(deque1_ex5)}')
