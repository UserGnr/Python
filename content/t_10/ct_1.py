'''
Erros mais comuns em Python

- É EXTREMAMENTE importante prestar atenção e entender as saídas de erros gerados pela execução do código
- Exceptions e Erros são sinônimos na programação
'''

'''
# Erros mais comumns:

# Exemplo 1
# SyntaxError
# Ocorre quando o Python encontra um erro de sintaxe. Ou seja, foi escrito algo que o Python não reconhece como parte da linguagem.
print('Exemplo 1 - SyntaxError')
# a)
def funcao:
    print('Um texto qualquer')

# b)
 def = 1

# c)
return
'''

'''
# Exemplo 2
# NameError
# Ocorre quando uma variável ou função não foi definida
print('Exemplo 2 - NameError')

# a)
print(texto)

# b)
texto()
'''

'''
# Exemplo 3
# TypeError
# Ocorre quando uma função/operação/ação é aplicada a um tipo errado
print('Exemplo 3 - TypeError')

# a)
print(len(5))

# b)
print('Texto' + [])
'''

'''
# Exemplo 4
# IndexError
# Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice inválido
print('Exemplo 4 - IndexError')

# a)
lista = ['Texto']
print(lista[8])

# b)
lista = ['Texto']
print(lista[0][10])

# c)
tupla = ('Texto',)
print(tupla[0][10])
'''

'''
# Exemplo 5
# ValueError
# Ocorre quando uma função/operação built-in (integrada) recebe um argumento com o tipo correto mas um valor inapropriado
print('Exemplo 5 - ValueError')

# a)
print(int('Texto'))
'''

'''
# Exemplo 6
# KeyError
# Ocorre quando tentamos acessar um dicionário com uma chave que não existe
print('Exemplo 6 - KeyError')

# a)
dic = {'linguagem': 'qualquer'}
print(dic['texto'])
'''

'''
# Exemplo 7
# AttributeError
# Ocorre quando uma variável não tem um atributo/função
print('Exemplo 7 - AttributeError')

# a)
tupla = (11, 2, 31, 4)
print(tupla.sort())
'''

'''
# Exemplo 8
# IndentationError
# Ocorre quando não respeitamos a indentação do Python (4 espaços)
print('Exemplo 8 - IndentationError')

a)
def nova():
print('Texto')

b)
for i in range(10):
i + 1
'''
