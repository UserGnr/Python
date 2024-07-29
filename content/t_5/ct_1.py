'''
Loop for

Loop:
- É uma estrutura de repetição
- É usado para iterar sobre sequências ou valores iteráveis
Exemplos:
    String:
        nome = "Um nome qualquer"
    Lista:
        lista = [1, 2, 3, 4]
    Range:
        numeros = range(1, 10)
'''

# Exemplo 1 - String
print('Exemplo 1 - String')

nome = 'Um nome qualquer'

for letra in nome:
    print(letra)

print('\n\n')

# Exemplo 2 - Lista
print('Exemplo 2 - Lista')

lista = [1, 3, 5, 7, 9]

for letra in lista:
    print(letra)

print('\n\n')

# Exemplo 3 - range
# range(valor_inicial, valor_final, step)
# O valor_final não é inclusivo, ou seja, é necessário acrescentar +1
# O step é opcional, por padrão é +1, ou seja, passa de 1 em 1
# Se colocado apenas um valor, range(5), por exemplo, o 5 será o valor final e o valor inicial considerado é o 0
print('Exemplo 3 - range()')

numeros = range(1, 10)

print("Exemplo 3, parte 1")
for numero in range(1, 10+1):
    print(numero)

print('\n')

print("Exemplo 3, parte 2")
for numero in range(10, 1, -1):
    print(numero)

print('\n')

print("Exemplo 3, parte 3")
for numero in range(10):
    print(numero)

print('\n')

print("Exemplo 3, parte 4")
for numero in range(10, 1, -5):
    print(numero)

print('\n')

print("Exemplo 3, parte 5")

lista = list(range(10))
print(lista)


print('\n\n')


# Exemplo 4 - enumerate
# O enumerate gera uma tupla: ((chave_0, valor_0),(chave_1, valor_1),...,(chave_x, valor_x))
print('Exemplo 4 - enumerate')

nome = 'Um nome qualquer'

print("Exemplo 4, parte 1")
for indice, valor in enumerate(nome):
    print(indice , valor)

print('\n')

# Quando tem 2 valor, em Python, pode descartar 1 deles usando o underline
print("Exemplo 4, parte 2")
for _, valor in enumerate(nome):
    print(valor)

print('\n')

print("Exemplo 4, parte 3")
for valor in enumerate(nome):
    print(valor)

print('\n')

print("Exemplo 4, parte 4")
for valor in enumerate(nome):
    print(valor[0]) # Usa apenas os valores do índice

print('\n')

print("Exemplo 4, parte 5")
for valor in enumerate(nome):
    print(valor[1]) # Usa apenas os valores do valor

print('\n\n')

# Exemplo 5
print("Exemplo 5 - for dentro do for")

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
