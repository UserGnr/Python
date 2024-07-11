'''
List comprehension (parte 1)

- Utilizando o List comprehension torna possível criar novas listas com dados a partir de outro iterável
- Sintaxe:
    [ dado for dado in iterável ]
'''

# Exemplo 1
# Usando list comprehension
print('Exemplo 1 - Usando list comprehension')

numeros = [1, 2, 3, 4, 5]

dobro = [numero * 2 for numero in numeros]
metade = [numero / 2 for numero in numeros]


def numero_ao2(valor):
    return valor ** 2


quadrado = [numero_ao2(numero) for numero in numeros]

print(f'Lista 1: {numeros}')
print(f'Lista 2 (usando list comprehension): {dobro}')
print(f'Lista 3 (usando list comprehension): {metade}')
print(f'Lista 4 (usando list comprehension e uma função): {quadrado}')
print(f'Lista 5 (usando list mais simplificado): {[numero ** 2 for numero in [1, 2, 3, 4, 5]]}')

print('\n\n')

# Exemplo 2
# Usando list comprehension em uma linha
print('Exemplo 2 - Usando list comprehension em uma linha')

nome = 'Um nome qualquer'

print(f'Letras em maiúculo: {[letra.upper() for letra in nome]}')   # Não é necessário usar um loop para deixar as letras em maiúsculo, da maneira como foi feito é criado uma lista com cada letra em maiúsculo

print('\n\n')

# Exemplo 3
# Usando list comprehension e def (função)
print('Exemplo 3 - Usando list comprehension e "def" (função)')

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

nomes = ['joão', 'pedro', 'maria', 'júlia']

print([caixa_alta(pessoa) for pessoa in nomes])

print('\n\n')

# Exemplo 4
# Usando list comprehension com range e outros tipos de dados

print([numero for numero in range(1,10)])
print([numero + numero for numero in range(1,10)])
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
print([str(valor) for valor in [0, 1, 2, 3, 4]])    # Convertendo os valores inteiros para uma string
