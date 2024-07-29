'''
HOF - Higher Order Functions (Funções de Maior Grandeza)

- Uma linguagem de programação com suporte HOF pode-se ter funções que retornam outras funções como resultado ou pode-se passar funções como argumentos para outras funções e até mesmo criar variáveis do tipo de funções nos programas

- Em Python, as funções são First Class Citizen (Cidadões de Primeira Classe)

'''

# Exemplo 1
# Função que tem como parâmetro outras funções
print('Exemplo 1 - Função que tem como parâmetro outras funções')


def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return(funcao(num1, num2))


print(calcular(3, 4, somar))
print(calcular(3, 4, subtrair))
print(calcular(3, 4, multiplicar))
print(calcular(3, 4, dividir))

print('\n\n')

# Exemplo 2
# Nested Functions (funções aninhadas)
# Inner Functions ou Nested Functions são funções dentro de funções
print('Exemplo 2 - Nested Functions (funções aninhadas)')

from random import choice


def cumprimentar(nome):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + nome   # Note que aqui o retorno é a execução da função humor


print(cumprimentar('Maria'))

print('\n\n')

# Exemplo 3
# Retornando funções de outras funções
print('Exemplo 3 - Retornando funções de outras funções')

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahah', 'kkk', 'yayaya'))
    return rir  # Note que aqui o retorno é a própria função rir


rindo = faz_me_rir()
print(rindo())

print('\n\n')

# Exemplo 4
# Acessando o escopo de funções mais externas
# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas
print('Exemplo 4 - Acessando o escopo de funções mais externas')

from random import choice


def faz_me_rir_novamente(nome):
    def dando_risada():
        risada = choice(('hahah', 'lololo', 'kkk'))
        return f'{risada} {nome}'
    return dando_risada


rindo = faz_me_rir_novamente('Mariazinha')

print(rindo())
