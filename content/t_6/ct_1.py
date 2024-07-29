'''
Listas (parte 1)

Listas em Python funcionam como v etores/matrizes (arrays) em outras linguagens, 
com a diferença das listas serem DINÂMICAS e também ser possível colocar QUALQUER tipo de dado.

- Dinâmico: não possuem tamanho fixo, pode ser criado a lista e ir adicionando elementos. Ou seja, são mutáveis
- Qualquer tipo de dado: não possuem tipo de dado fixo, ou seja, pode ser colocado qualquer tipo de dado

As listas em Python são representadas por colchetes: []
'''

# Exemplo 1
# Exemplos de listas
print('Exemplo 1')
print('Exemplos de listas')

lista1= [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['U', 'm', ' ', 'n', 'o', 'm', 'e', ' ', 'q', 'u', 'a', 'l', 'q', 'u', 'e', 'r']
lista3 = []
lista4 = list(range(11))
lista5 = list('Um nome qualquer')
lista6 = [1, 2.34, True, 'Texto', 'd', [1, 2, 3], 46548987894]

print(f'Lista 1: {lista1}')
print(f'Lista 1: {lista2}')
print(f'Lista 1: {lista3}')
print(f'Lista 1: {lista4}')
print(f'Lista 1: {lista5}')
print(f'Lista 1: {lista6}')

print('\n\n')

# Exemplo 2
# Checar se um número está na lista com in
print('Exemplo 2 - Checar se um número está na lista com "in"')

lista1_ex2 = list(range(11))
lista2_ex2 = ['U', 'm', ' ', 'n', 'o', 'm', 'e', ' ', 'q', 'u', 'a', 'l', 'q', 'u', 'e', 'r']

print(f'Lista 1: {lista1_ex2}')

numero = 7
if numero in lista1_ex2:
    print(f'A lista 1 possui o numero {numero}')
else:
    print(f'A lista 1 não possui o numero {numero}')

print(f'Lista 2: {lista2_ex2}')

letra = 'a'
if letra in lista2_ex2:
    print(f'A lista 2 possui a letra {letra}')
else:
    print(f'A lista 2 não possui a letra {letra}')

print('\n\n')

# Exemplo 3
# Contar um número de ocorrências de um valor com count
print('Exemplo 3 - Contar um número de ocorrências de um valor com "count"')

lista1_ex3= [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2_ex3= ['U', 'm', ' ', 'n', 'o', 'm', 'e', ' ', 'q', 'u', 'a', 'l', 'q', 'u', 'e', 'r']

numero = 1
letra = 'a'

print(f'Lista 1: {lista1_ex3}')
print(f'Lista 2: {lista1_ex3}')

print(f'O número "{numero}" foi encontrado {lista1_ex3.count(numero)} vez(es) na lista 1')
print(f'A letra "{letra}" foi encontrada {lista2_ex3.count(letra)} vez(es) na lista 2')

print('\n\n')

# Exemplo 4
#  Ordenar uma lista com sort
print('Exemplo 4 - Ordenar uma lista com "sort"')

lista1_ex4= [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2_ex4= ['U', 'm', ' ', 'n', 'o', 'm', 'e', ' ', 'q', 'u', 'a', 'l', 'q', 'u', 'e', 'r']

print(f'Lista 1 sem ordenar: {lista1_ex4}')
lista1_ex4.sort()
print(f'Lista 1 ordenada: {lista1_ex4}')

print(f'Lista 2 sem ordenar: {lista2_ex4}')
lista2_ex4.sort()
print(f'Lista 2 ordenada: {lista2_ex4}')

print('\n\n')

# Exemplo 5
# Adicionar um elemento com append
# O append só adiciona um elemento por vez, é possível colocar uma lista dentro de outra com o append
print('Exemplo 5 - Adicionar um elemento com "append"')

lista1_ex5= [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

print(f'Lista 1: {lista1_ex5}')

lista1_ex5.append(42)
lista1_ex5.append([55, 42, 37])

print(f'Lista 1 com a adição dos elementos "42" e "[55, 42, 37]": {lista1_ex5}')

print('\n\n')

# Exemplo 6
# Adicionar elementos com extend
# O extend só aceita o formato de iteráveis, como uma lista, por exemplo
print('Exemplo 6 - Adicionar elementos com "extend"')

lista1_ex6= [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

print(f'Lista 1: {lista1_ex6}')
lista1_ex6.extend([123,44,67])  # Adiciona vários elementos de uma unica vez na lista
print(f'Lista 1 com a adição do "[123,44,67]": {lista1_ex6}')

print('\n\n')

# Exemplo 7
# Adicionar um novo elemento na lista informando a posição do índice com insert
# O insert permite que seja adicionado um novo elemento em qualquer local da lista, deslocando os dados para a direita
print('Exemplo 7 - Adicionar um novo elemento com base no índice com "insert"')

lista1_ex7= [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

print(f'Lista 1: {lista1_ex7}')
lista1_ex7.insert(2, 'Novo valor')  # Na posição 2 adiciona o valor 'Novo valor'
print(f'Lista 1 modificada: {lista1_ex7}')

print('\n\n')

# Exemplo 8
# Invertendo a ordem da lista com o reverse
print('Exemplo 8 - Invertendo a ordem da lista com o "reverse"')

lista1_ex8= [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2_ex8 = ['U', 'm', ' ', 'n', 'o', 'm', 'e', ' ', 'q', 'u', 'a', 'l', 'q', 'u', 'e', 'r']

print(f'Lista 1: {lista1_ex8}')
print(f'Lista 2: {lista2_ex8}')

lista1_ex8.reverse()
lista2_ex8.reverse()

print(f'Lista 1 modificada: {lista1_ex8}')
print(f'Lista 2 modificada: {lista2_ex8}')

print('\n\n')

# Exemplo 9
# Tamanho da lista com len
print('Exemplo 9 - Tamanho da lista com "len"')

lista1_ex9= [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(f'Lista 1: {lista1_ex9}')

print(f'O tamanho da lista 1 é: {lista1_ex9.__len__()}')
# Ou
print(f'O tamanho da lista 1 é: {len(lista1_ex9)}')

print('\n\n')

# Exemplo 10
# Remover o último elemento da lista com pop
# Com o pop, também é possível remover um elemento pelo índice
# O pop além de remover, ele também retorna o valor apagado
# Os elementos apagados são deslocados para a esquerda
# Se o índice especificado não existir, será retornado um erro
print('Exemplo 10 - Remover o último elemento da lista com "pop"')

lista1_ex10 = list(range(11))

print(f'Lista 1: {lista1_ex10}')

lista1_ex10.pop()   # Removendo o último item da lista
print(f'Lista 1, removendo o último item: {lista1_ex10}')

lista1_ex10.pop(1)  # Removendo o elemento do índice 1
print(f'Lista 1, removendo o elemento do índice 1: {lista1_ex10}')

valor = lista1_ex10.pop(1)  # Removendo e atribuindo o valor retirado em uma variável
print(f'Lista 1, o valor retirado é {valor} e era o novo índice 1: {lista1_ex10}')

print('\n\n')

# Exemplo 11
# Remover todos os elementos de uma lista com clear
print('Exemplo 11 - Remover todos os elementos de uma lista com "clear"')

lista1_ex11 = list(range(11))

print(f'Lista 1: {lista1_ex11}')
lista1_ex11.clear()
print(f'Lista 1 modificada: {lista1_ex11}')

print('\n\n')

# Exemplo 12
# Copiando uma lista com o copy (deep copy)
# Ao usar o copy() é feito uma cópia da lista para uma nova, mantendo cada uma deslas, a cópia e a copiada, totalmente independentes.
# Desse modo, qualquer edição, em qualquer uma delas, não terá efeito de uma na outra.
# Isso em Python é chamado de Deep Copy (copia profunda)
print('Exemplo 12 - Copiando uma lista com o "copy" (deep copy)')

lista1_ex12 = [1, 2, 3]
print(f'Lista 1: {lista1_ex12}')

Lista2_ex12 = lista1_ex12.copy()

print(f'Lista 2 (cópia da lista 1): {Lista2_ex12}')

print('Adicionando um novo elemento na lista 1')
lista1_ex12.append(4)   # Adicionando um novo elemento na lista 1

print(f'Lista 1: {lista1_ex12}')
print(f'Lista 2 (cópia): {Lista2_ex12}')

print('Adicionando um novo elemento na lista 2 (cópia)')
Lista2_ex12.append(5)

print(f'Lista 1: {lista1_ex12}')
print(f'Lista 2 (cópia): {Lista2_ex12}')

print('\n\n')

# Exemplo 13
# Copiando uma lista com o = (shallow copy)
# Shallow copy (Cópia superficial), é quando a cópia da lista é feita sem o .copy, usando apenas a atribuição para uma nova variável.
# Fazendo a cópia dessa forma, qualquer mudança, tanto na lista copiada quanto na cópia, em ambas surtiram efeito.
print('Exemplo 13 - Copiando uma lista com o "=" (shallow copy)')

lista1_ex13 = [1, 2, 3]
print(f'Lista 1: {lista1_ex13}')

Lista2_ex13 = lista1_ex13
print(f'Lista 2 (cópia da lista 1): {Lista2_ex13}')

print('Adicionando um novo elemento na lista 1')
lista1_ex13.append(4)   # Adicionando um novo elemento na lista 1

print(f'Lista 1: {lista1_ex13}')
print(f'Lista 2 (cópia): {Lista2_ex13}')

print('Adicionando um novo elemento na lista 2 (cópia)')
Lista2_ex13.append(5)

print(f'Lista 1: {lista1_ex13}')
print(f'Lista 2 (cópia): {Lista2_ex13}')
