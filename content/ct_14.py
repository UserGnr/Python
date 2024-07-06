'''
Listas (parte 2)
'''

# Exemplo 14
# Converter uma string para uma lista com split
# Por padrão o split separa as strings pelo espaço
print('Exemplo 14 - Converter uma string para uma lista com "split"')

texto1_ex14 = 'Um texto qualquer'

print(f'Texto 1: {texto1_ex14}')
lista1_ex14 = texto1_ex14.split()
print(f'Lista 1 (separação padrão): {lista1_ex14}')

texto2_ex14 = 'Um,texto,qualquer'

print(f'Texto 3: {texto2_ex14}')
lista2_ex14 = texto2_ex14.split(',')
print(f'Lista 2 (separado por vírgula): {lista2_ex14}')

print('\n\n')

# Exemplo 15
# Converter uma string para uma lista com list
print('Exemplo 15 - Converter uma string para uma lista com "list"')

texto1_ex15 = 'Um nome qualquer'
lista1_ex15 = list(texto1_ex15)

print(f'Texto 1: {texto1_ex15}')
print(f'Lista 1: {lista1_ex15}')

print('\n\n')

# Exemplo 16
# Converter uma lista em uma string com join
print('Exemplo 16 - Converter uma lista em uma string com "join"')

lista1_ex16 = ['Testando', 'o', 'uso', 'do', 'join']

texto1_ex15 = ' '.join(lista1_ex16) # O espaço será colocado entre cada elemento para formar a string

print(f'Lista 1: {lista1_ex16}')
print(f'Texto 1: {texto1_ex15}')

print('\n\n')

# Exemplo 17
# Juntar duas listas com +
print('Exemplo 17 - Juntar duas listas com "+"')

lista1_ex16= [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2_ex16 = ['U', 'm', ' ', 'n', 'o', 'm', 'e', ' ', 'q', 'u', 'a', 'l', 'q', 'u', 'e', 'r']

lista3_ex16 = lista1_ex16 + lista2_ex16

print(f'Lista 1: {lista1_ex16}')
print(f'Lista 2: {lista2_ex16}')
print(f'Lista 3 (união da lista 1 e 2): {lista3_ex16}')

print('\n\n')

# Exemplo 18
# Repetir elementos da lista com *
print('Exemplo 18 - Repetir elementos da lista com "*"')

lista1_ex18 = [1, 2, 3, 4]

print(f'Lista 1: {lista1_ex18}')
lista1_ex18 = lista1_ex18 * 3
print(f'Lista 1 (*3): {lista1_ex18}')

print('\n\n')

# Exemplo 19
# Iterando sobre listas
print('Exemplo 19 - Iterando sobre listas')

lista1_ex19 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'Lista 1: {lista1_ex19}')

print('Elementos da lista 1:')
for elemento in lista1_ex19:
    print(elemento)

print('\n\n')

lista2_ex19 = [1 ,2, 3, 4]

print(f'Lista 2: {lista2_ex19}')

print('Elementos da lista 2 com a somando +2:')
soma = 2
for elemento in lista2_ex19:
    print(elemento)
    soma = soma + elemento

print('\n\n')


# Exemplo para analisar:
# print('Exemplo 2')

# carrinho = []
# produto = ''

# while produto != 'sair':
#     print('Adicione um produto na lista ou digite "sair" para sair: ')
#     produto = input()
#     if produto != 'sair':
#         carrinho.append(produto)

# print('Seu produtos:')
# for produto in carrinho:
#     print(produto)

# print('\n\n')

# Exemplo 20
# Adicionando variáveis nas listas
print('Exemplo 20 - Adicionando variáveis nas listas')

num1 =1
num2 =2
num3 =3
num4 =4
num5 =5

lista1_ex20 = [num1, num2, num3, num4, num5]

print(f'Valores das variáveis: {num1, num2, num3, num4, num5}')
print(f'Lista 1: {lista1_ex20}')

print('\n\n')

# Exemplo 21
# Acessar valores da lista
print('Exemplo 21 - Acessar valores da lista')

lista1_ex21 = ['verde', 'amarelo', 'azul', 'branco']

print(f'Lista 1: {lista1_ex21}')

print('Acessando os valores da lista 1 com o índice positivo:')
print(f'Índice: 0 valor:{lista1_ex21[0]}')
print(f'Índice: 1 valor:{lista1_ex21[1]}')
print(f'Índice: 2 valor:{lista1_ex21[2]}')
print(f'Índice: 3 valor:{lista1_ex21[3]}')

print('Acessando os valores da lista 1 com o índice negativo:')
print(f'Índice: -1 valor: {lista1_ex21[-1]}')
print(f'Índice: -2 valor: {lista1_ex21[-2]}')
print(f'Índice: -3 valor: {lista1_ex21[-3]}')
print(f'Índice: -4 valor: {lista1_ex21[-4]}')
print(f'Índice: -4 valor: {lista1_ex21[-4]}')
# print(f'Índice: -5 valor: {lista1_ex21[-5]}')   # Retorna um erro por que não existe

print('\n\n')

# Exemplo 22
#  Gerar pares chave e valor com "enumerate"
print('Exemplo 22 - Gerar pares chave e valor com enumerate')

lista1_ex22 = ['verde', 'amarelo', 'azul', 'branco']

print(f'Lista 1: {lista1_ex22}')

print('Elementos da lista 1:')
for indice, cor in enumerate(lista1_ex22):
    print(indice, cor)

print('\n\n')

# Exemplo 23
# Encontrar o índice de um elemento na lista com index
# Se o valor não for encontrado retorna um erro
# Se tiver mais de 1 elemento, retornará o primeiro encontrado
print('Exemplo 23 - Encontrar o índice de um elemento na lista com "index"')

lista1_ex23 = [5, 6, 7, 8, 5, 9, 10, 5]

print(f'Lista 1: {lista1_ex23}')

print(f'Valor: 6 índice: {lista1_ex23.index(6)}') # Retorna a posição em que está o valor 6
print(f'Valor: 9 índice: {lista1_ex23.index(9)}') # Retorna a posição em que está o valor 9
print(f'Valor: 5 índice: {lista1_ex23.index(5)}') # Retorna a posição em que está o valor 5

# Pode usar o index para fazer busca dentro de um range, ou seja, qual o índice deve começar a buscar
print(f'Busca o valor 5 a partir do índice 0 | resultado: {lista1_ex23.index(5, 0)}')  # Busca a partir do índice 0
print(f'Busca o valor 5 a partir do índice 1 | resultado: {lista1_ex23.index(5, 1)}')  # Busca a partir do índice 1
print(f'Busca o valor 5 a partir do índice 2 | resultado: {lista1_ex23.index(5, 2)}')  # Busca a partir do índice 2

#  Fazer busca dentro de um range, início/fim
print(f'Busca o valor 5 do índice 5 ao 7 | Resultado: {lista1_ex23.index(5, 5, 8)}')   # Busca entre o índice 5 ao 7 o valor 5, lembrando que o valor 8 não é considerado (8-1=7), ou seja, a busca é feita até o índice 7

print('\n\n')

# Exemplo 24
# Usando o slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]
print('Exemplo 24 - Usando o "slicing"')

lista1_ex24 = [1, 2, 3, 4]

print(f'Lista 1: {lista1_ex24}')

print(lista1_ex24[1])
print(lista1_ex24[1:])
print(lista1_ex24[-1])
print(lista1_ex24[-1:])

print(lista1_ex24[:2])    # Começa em 0 e vai até o índice 2-1

print(lista1_ex24[1:3])   # Começa em 1 e vai até o índice 3-1

print(lista1_ex24[:-1])
print(lista1_ex24[:-3])

print(lista1_ex24[1::2])  # Começa em 1 e vai até o final, pulando de 2 em 2
print(lista1_ex24[::2])  # Começa em 0 e vai até o final, pulando de 2 em 2

print(lista1_ex24[-1::-1])  # Começa do último e vai até o primeiro

print(lista1_ex24[::-1])    # Invertendo a ordem da lista

print('\n\n')

# Exeplo 25
# Invertendo valores em uma lista
print('Exeplo 25 - Invertendo valores em uma lista')
lista1_ex25 = ['nome1', 'nome2']

print(f"Lista 1: {lista1_ex25}")

lista1_ex25[0], lista1_ex25[1] = lista1_ex25[1], lista1_ex25[0]

print(f"Lista 1 (invertida): {lista1_ex25}")

lista1_ex25.reverse()
print(f"Lista 1 (usando o reverse): {lista1_ex25}")

print('\n\n')

# Exeplo 26
# Soma* , Valor Måximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais.
print('Exemplo 26 - Soma, valor máximo, valor mínimo, tamanho')

lista1_ex26 = [1, 2, 3, 4, 5]

print(f'Soma: {sum(lista1_ex26)}')   # Soma
print(f'Valor máximo: {max(lista1_ex26)}')   # Valor máximo
print(f'Valor mínimo {min(lista1_ex26)}')   # Valor mínimo
print(f'Tamanho da lista: {len(lista1_ex26)}')   # Tamanho da lista

print('\n\n')

# Exemplo 27
# Transformar lista em tupla
print('Exemplo 27 - Transformar lista em tupla')

lista1_ex27 = [1, 2, 3, 4, 5]
print(f'Lista 1: {lista1_ex27}')
print(f'Tipo da lista 1: {type(lista1_ex27)}')

tupla1_ex27 = tuple(lista1_ex27)

print(f'Tupla 1: {tupla1_ex27}')
print(f'Tipo da tupla 1: {type(tupla1_ex27)}')

print('\n\n')

# Exemplo 28
# Desempacotamento de listas
# Apresenta erro se tiver uma quantidade elementos diferente da quantidade de variáveis para receber
print('Exemplo 28 - Desempacotamento de listas')

lista1_ex28 = [1, 2, 3]

num1, num2, num3 = lista1_ex28

print('Valores da lista 1:')
print(num1)
print(num2)
print(num3)
