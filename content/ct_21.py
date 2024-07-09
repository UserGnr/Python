'''
Retorno de funções

- Em Python, quando uma função não retorna nenhum valor, o retorno é None
- Funções Python que retornam valores, devem retornar estes valores com a
palavra reservada 'return'
- Não é necessário criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outras funções.
- Para o retorno de uma função é usado o 'return'
- Quando é executado o 'return', sai automaticamente da função
'''

# Usando o return
'''
Sobre o return:
- Finaliza a função, ou seja, ela sai da execução da função;
- Podemos ter, em uma função, diferentes returns;
- Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
'''

# Exemplo 1
# Usando o "return"
print('Exemplo 1 - Usando o "return"')


def quadrado_de_7():
    return 7 * 7


retorno_da_funcao = quadrado_de_7()


print(f'Retorno direto da função: {quadrado_de_7()}')
print(f'Retorno da função em uma variável: {retorno_da_funcao}')

print('\n\n')

# Exemplo 2
# Avaliando o que acontece com uma linha após o "return"
print('Exemplo 2 - Avaliando o que acontece com uma linha após o "return"')


def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi'
    print('Estou sendo executado depois do retorno...')


print(diz_oi())

print('\n\n')

# Exemplo 3
# Usando vários 'return' em uma função
print('Exemplo 3 - Usando vários "return" em uma função')

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
# Após executar qualquer um dos return da função acima, será feito a saída da função e o restante do código não será executado


print(nova_funcao())

print('\n\n')

# Exemplo 4
# Retornando uma tupla da função
print('Exemplo 4 - Retornando uma tupla da função')


def outra_funcao():
    return 2, 3, 4, 5


print(f'Retorno da função: {outra_funcao()}')
print(f'Tipo da função: {type(outra_funcao())}')

print('\n\n')

# Exemplo 5
# Gerar um número pseudo-randômico entre 0 e 1
print('Exemplo 5 - Gerar um número pseudo-randômico entre 0 e 1')

from random import random

def joga_moeda():
    # Gerar um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
