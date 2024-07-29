'''
Argumentos posicionais

São os argumentos usados para definição
/
- Todos os parâmetros a direita não podem ser chamados pelo nome
- Não permite que o usuário infome o parâmetro ao fazer uso da função
*
- Todos os parâmetros a esquerda devem ser informados ao usar a função
- Obriga o usuário a informar o nome dos parâmetros ao fazer uso da função

Obs.: o que estiver entre o / e * são opcionais, ou seja, o usuário decide se informa ou não o nome do parâmetro ao usar a função
'''

# Exemplo 1
# Uma função nomal
def cumprimentar1(nome):
    return f'Olá {nome}'


print(cumprimentar1('Ana1'))
print(cumprimentar1(nome='Ana1'))


# Exemplo 2
# Argumento posicional com /


def cumprimentar2(nome, /):
    return f'Olá {nome}'


print(cumprimentar2('Ana2'))
# print(cumprimentar2(nome='Ana2'))    # Retorna um erro, pois está a esqueda da barra /

#  Exemplo 3
# Argumento posicional com *


def cumprimentar3(*, nome):
    return f'Olá {nome}'


print(cumprimentar3(nome='Ana3'))
# print(cumprimentar3('Ana3'))  # Retorna um erro com essa sintaxe

# Exemplo 4
# Mais complexo


def cumprimentar4(nome, /, outra_coisa = 'Lálá'):
    return f'Olá {nome} {outra_coisa}'


print(cumprimentar4('Ana4','Texto'))
print(cumprimentar4('Ana4'))
print(cumprimentar4('Ana4', outra_coisa='Texto'))

# Exemplo 5
# Mais complexo


def cumprimentar5_1(nome, /, outra_coisa):
    return f'Olá {nome} {outra_coisa}'


print(cumprimentar5_1('Ana5','Texto'))
print(cumprimentar5_1('Ana5', outra_coisa='Texto'))


def cumprimentar5_2(nome, outra_coisa, /):
    return f'Olá {nome} {outra_coisa}'


print(cumprimentar5_2('Ana5_2','Texto'))
# print(cumprimentar5_2('Ana5_2'))  # Retorna erro pois não foi definido um valor padrão
# print(cumprimentar5_2('Ana5_2', outra_coisa='Texto')) # Retorna erro

# Exemplo 6
# Mais complexo


def cumprimentar6(nome, sobrenome, /, idade, *, comentario, algo_mais='Nada mais a declarar'):
    return f'Olá {nome} {sobrenome}, você tem {idade} anos e que falar que: {comentario}. {algo_mais}.'


# print(cumprimentar6('Ana','Fulana','25','o dia está lindo','Não quero dizer mais nada'))    # Retorna erro pois não foi explicitado
print(cumprimentar6('Ana','Fulana','25', comentario='o dia está lindo', algo_mais='Não quero dizer mais nada'))
print(cumprimentar6('Ana','Fulana','25', comentario='o dia está lindo'))
