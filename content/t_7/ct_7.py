'''
*args

- *args é um parâmetro, como qualquer outro. Isso significa que é possível chama-lo de qualquer coisa, desde que começe com asterisco, porém, por convenção, os args devem ser nomeados como 'args'
- o parâmetro *args utilizado em uma função serve para colocar valores extras como entrada
- Esses valores extras que podem ser colocados são inseridos como uma tupla (as tuplas são imutáveis)
- Os parâmetros *args não são obrigatórios
'''

# Exemplo 1
# Entendendo o *args
print('Exemplo 1 - Entendendo o *args')

def soma_todos_numero(*args):
    print(type(args), args)
    return args

soma_todos_numero()
soma_todos_numero(1)
soma_todos_numero(1, 2)
soma_todos_numero(1, 2, 3)
soma_todos_numero(1, 2, 3, 4)

print('\n\n')

# Exemplo 2
# Acrescentando parâmetros nomeados
# Os parâmtros nomeados devem vir antes dos args 
print('Exemplo 2 - Acrescentando parâmetros nomeados')

def soma_todos_numeros(nome, email, *args):
    return sum(args)

print('Parte 1')
print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3, 4))
print(soma_todos_numeros('Angelina', 'Jolie', 3, 4, 5, 6))
print(soma_todos_numeros('Angelina', 'Jolie', 23.4, 12.5))


def verifica_info(*args):
    if 'teste' in args and 'texto' in args:
        return 'Bem-vindo'
    return 'Eu não tenho ...'


print('\n')

print('Parte 2')
print(verifica_info())
print(verifica_info(1, True, 'teste', 'texto'))
print(verifica_info(1, 'Uni', 3.145))

print('\n\n')

# Exemplo 3
# Desempacotar
# O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados para a função. Desta forma, ele saberá que precisará desempacotar estes dados antes.
print('Exemplo 3 - Desempacotar')


def soma(*args):
    print(args)
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]

# print(f'Soma dos numeros empacotados: {soma(numeros)}')  # Retorna um erro para a função, pq não consegue somar os dados de uma lista dentro de uma tupla
print(f'Soma dos números desempacotados: {soma(1, 2, 3, 5)}')
print(f'Soma dos números desempacotados: {soma(*numeros)}')  # Funciona pois desempacota os dados e os deixa apenas como uma tupla
