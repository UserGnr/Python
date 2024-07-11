'''
Lambdas

As expressões lambdas, são funções sem nome, ou seja, funções anônimas

Função em Python:
def funcao(x):
    return 3 * x + 1

Expressão Lambda:
lambda x: 3 * x + 1
Como utilizar a expressão lambda:
calc = lambda x: 3 * x + 1

print(calc(4))

'''

# Exemplo 1
# Usando lambda
print('Exemplo 1 - Usando lambda')
calculo = lambda x: 3 * x + 1

print(calculo(5))
print(calculo(1))

print('\n\n')

# Exemplo 2
# Expressões lambdas com múltiplas entradas
print('Exemplo 2 - Expressões lambdas com múltiplas entradas')

# Nome e sobrenoome são os parâmetros de entrada
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('   Joao   ', 'silVa      '))
print(nome_completo(sobrenome='silVa      ', nome='FELICITY   ', ))

print('\n\n')

# Exemplo 3
# Expressões lambdas sem parâmetros e com vários parâmetros
# Se for informado mais argumentos do que parâmetros, retornará erro
print('Exemplo 3 - Expressões lambdas sem parâmetros e com vários parâmetros')

texto = lambda: 'Um texto qualquer'
um = lambda x: 3 * x + 1
dois = lambda x, y: x + y
tres = lambda x, y, z: x + y + z
print(texto())
print(f'Um: {um(1)}')
print(f'Dois: {dois(1, 2)}')
print(f'Tres: {tres(1, 2, 3)}')

print('\n\n')

# Exemplo 4
# Usando uma lista
print('Exemplo 4 - Usando uma lista')

nomes = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(nomes)

nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print('Apenas o sobrenome ordenado em oudem alfabética')
print(nomes)

print('\n\n')

# Exemplo 5
# Usando uma função quadrática
# f(x) = a * x ** 2 + b * x + c
print('Exemplo 5 - Usando uma função quadrática')


def funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a*x**2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = funcao_quadratica(1, 2, 3)

print(teste(0))
print(teste(1))
print(teste(2))
print(teste(3))

print(funcao_quadratica(1, 2, 3)(2))
