'''
**kwargs

- É possível nomear um kwarg como um parâmetro de uma função com o nome de **xis, mas por convenção chamamos de **kwargs
- Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário
- Os parâmetros **kwargs não são obrigatórios
'''

# Exemplo 1
# Usando **kwargs
print('Exemplo 1 - Usando **kwargs')


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

print('\n\n')

# Exemplo 2
# Outro exemplo usando **kwargs
print('Exemplo 2 - Outro exemplo usando **kwargs')


def cumprimento_especial(**kwargs):
    if 'cor' in kwargs and kwargs['cor'] == 'vermelho':
        return 'Sua cor é vermelha! Igual a minha'
    elif 'cor' in kwargs:
        return f"Sua cor é {kwargs['cor']}!"
    return 'Não tenho certeza se você tem cor ...'


print(cumprimento_especial())
print(cumprimento_especial(cor='azul'))
print(cumprimento_especial(cor='amarelo'))
print(cumprimento_especial(cor='vermelho'))
print(cumprimento_especial(abc='vermelho'))

print('\n\n')

# Exemplo 3
# Desempacotar kwargs
# Um pouco diferente do args, para desempacotar um kwargs é usado 2 asterísticos (**)
print('Exemplo 3 - Desempacotar kwargs')


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

print('\n\n')

# Exemplo 4
# Usando um dicionário para passar os argumentos obrigatórios com o desempacotamento
# Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função
print('Exemplo 4 - Usando um dicionário para passar os argumentos obrigatórios com o desempacotamento')

def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

# dicionario = dict(d=1, e=2, f=3)  #  Retorna erro pois os argumentos nomeados não são os mesmos dos parâmetros da função
# soma_multiplos_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='Felicity')
soma_multiplos_numeros(**dicionario, lang='Python')

print('\n\n')

# Exemplo 5
# Desempacotando argumentos obrigatórios


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
# Note que a lista, tupla e conjunto possui apenas 3 argumentos, que corresponde aos obrigatórios da função, como o kwargs não é obrigatório, não retornará erro

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)