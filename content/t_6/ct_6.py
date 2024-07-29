'''
Conjuntos (sets)

- Conjunto em qualquer linguagem de programação, é uma referência à Teoria dos Conjuntos da Matemática
- Os conjuntos são chamados de Sets no Python
- Desse modo:
    - Sets (conjuntos) não possuem valores duplicados;
    - Sets (conjuntos) não possuem valores ordenados;
    - Elementos não são acessados via índice, ou seja, conjuntos não são indexados.
- Conjuntos são utilizados quando é necessário armazenar elementos que não sejam necessários ter ordenação.
- Também é usado quando não é necessário se preocupar com as chaves, valores e itens duplicados
- Os conjuntos (sets) são referenciados em Python com, chaves {}
- Diferenças entre conjuntos (set) e mapas (dicionários) em Python:
    - Um dicionário tem chave/valor
    - Um conjunto tem apenas valor
- Ao criar um set com um valor repetido, o mesmo será ignorado e não fará parte do conjunto
- Os conjuntos não possuem ordem
- Os conjuntos podem ter tipos de dados misturados
'''

# Exemplo 1
# Criação de conjuntos (sets)
print('Exemplo 1 - Criação de conjuntos (sets)')
set1_ex1 = set({1, 2, 3, 4, 5, 6, 7, 1, 2, 3})
set2_ex1 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}   # Forma mais comum
set3_ex1 = {1, 'b', True, 34.22, 44}

print(f'Set 1: {set1_ex1} | tipo {type(set1_ex1)}') # Não irá aparecer os valores repetidos
print(f'Set 2: {set2_ex1} | tipo {type(set2_ex1)}') # Não irá aparecer os valores repetidos
print(f'Set 3: {set3_ex1} | tipo {type(set3_ex1)}') # Não irá aparecer os valores repetidos

print('\n\n')

# Exemplo 2
# Verificar um valor dentro do set
print('Exemplo 2 - Verificar um valor dentro do set')

set1_ex2 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}   # Forma mais comum

print(f'Set 1: {set1_ex2}')

if 3 in set1_ex2:
    print(f'Tem o 3')
else:
    print('Não tem o 3')

print('\n\n')

# Exemplo 3
# Diferença listas, tuplas, dicionários, conjuntos
print('Exemplo 3 - Diferença listas, tuplas, dicionários, conjuntos')

lista1_ex3 = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
tupla1_ex3 = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
dicionario1_ex3 = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34])
set1_ex3 = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}

print(f'Lista 1: {lista1_ex3} | tipo: {type(lista1_ex3)}')
print(f'Lista 1 tamanho: {len(lista1_ex3)}')

print(f'Tupla 1: {tupla1_ex3} | tipo: {type(tupla1_ex3)}')
print(f'Tupla 1 tamanho: {len(tupla1_ex3)}')

print(f'Dicionário 1: {dicionario1_ex3} | tipo: {type(dicionario1_ex3)}')
print(f'Dicionário 1 tamanho: {len(dicionario1_ex3)}')

print(f'Set 1: {set1_ex3} | tipo: {type(set1_ex3)}')
print(f'Set 1 tamanho: {len(set1_ex3)}')

# Exemplo 4
# Iterar em um set
print('Exemplo 4 - Iterar em um set')

set1_ex4 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}

print(f'Set 1: {set1_ex4}')

for valor in set1_ex4:
    print(valor)

# Exemplo 5
# Converter uma lista em um set
print('Exemplo 5 - Converter uma lista em um set')

lista1_ex5 = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3]
set1_ex5 = set(lista1_ex5)

print(f'Lista 1: {lista1_ex5} | Tamanho: {len(lista1_ex5)}')
print(f'Set 1: {set1_ex5} | Tamanho: {len(set1_ex5)}')

print('\n\n')

# Exemplo 6
# Adicionar elementos no set com add
# Duplicidade não gera erro
print('Exemplo 6 - Adicionar elementos no set com "add"')

set1_ex6 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}

print(f'Set 1: {set1_ex6}')

set1_ex6.add('True')
set1_ex6.add('Oi')
set1_ex6.add(555)

print(f'Set 1 (adicionando elementos): {set1_ex6}')

print('\n\n')

# Exemplo 7
# Remover elementos no set com remove
# É informado o valor que quer remover
# Se não tiver o valor, retornado erro
# Nenhum valor é retornado
print('Exemplo 7 - Remover elementos no set com "remove"')

set1_ex7 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}

print(f'Set 1: {set1_ex7}')

set1_ex7.remove(1)
set1_ex7.remove(2)
set1_ex7.remove(3)

print(f'Set 1 (removendo elementos): {set1_ex7}')

print('\n\n')

# Exemplo 8
# Remover elementos no set com discard
# É informado o valor que quer remover
# Se não tiver o valor informado NÃO retorna erro
# Nenhum valor é retornado
print('Exemplo 8 - Remover elementos no set com "discard"')

set1_ex8 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}

print(f'Set 1: {set1_ex8}')

set1_ex8.discard(1)
set1_ex8.discard(2)
set1_ex8.discard(3)
set1_ex8.discard("abc")

print(f'Set 1 (removendo elementos): {set1_ex8}')

print('\n\n')

# Exemplo 9
# Copiar com copy (deep copy)
# Os conjuntos são independentes
print('Exemplo - Copiar com "copy" (deep copy)')

set1_ex9 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}

set2_ex9 = set1_ex9.copy()

print(f'Set 1: {set1_ex9}')
print(f'Set 2 (cópia): {set2_ex9}')

print('\n\n')

# Exemplo 10
# Copiar (shallow copy)
# Os conjuntos não são independentes
print('Exemplo 10 - Copiar (shallow copy)')

set1_ex10 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}

set2_ex10 = set1_ex10

print(f'Set 1: {set1_ex10}')
print(f'Set 2 (cópia): {set2_ex10}')

print('\n\n')

# Exemplo 11
# Remover todos os elementos com clear
print('Exemplo - Remover todos os elementos com "clear"')

set1_ex11 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}

print(f'Set 1: {set1_ex11}')

set1_ex11.clear()

print(f'Set 1: {set1_ex11}')

print('\n\n')

# Exemplo 12
# União, intersecção e diferença
print('Exemplo 12 - União, intersecção e diferença')
set1_ex12_turma1 = {'Maria', 'Patricia', 'Pedro', 'Guilherme', 'Julia', 'Ana'}
set2_ex12_turma2 = {'Ellen', 'Maria', 'Gustavo', 'Pedro', 'Fernando'}

print(f'Set 1: {set1_ex12_turma1} | Tamanho: {len(set1_ex12_turma1)}')
print(f'Set 2: {set2_ex12_turma2} | Tamanho: {len(set2_ex12_turma2)}')
print('\n')

# União entre conjuntos
print('Unindo dois conjuntos')
# Forma 1
uniao1 = set1_ex12_turma1.union(set2_ex12_turma2)
# Forma 2 - O caracter '|' chama pipe
uniao2 = set1_ex12_turma1 | set2_ex12_turma2

print(f'União 1 (union): {uniao1}')
print(f'União 2 ( | ): {uniao2}')
print('\n')

# Intersecção entre conjuntos
# A intersecção é o que tem em comum
print('Intersecção entre dois conjuntos')

# Forma 1
interseccao1 = set1_ex12_turma1.intersection(set2_ex12_turma2)
# Forma 2
interseccao2 = set1_ex12_turma1 & set2_ex12_turma2

print(f'Intersecção 1 (intersection): {interseccao1}')
print(f'Intersecção 2 ( & ): {interseccao2}')
print('\n')

# Diferença entre conjuntos
# A diferença é que só tem em um, mas não tem no outro
print('Diferença entre conjuntos')

# Forma 1
diferenca1 = set1_ex12_turma1.difference(set2_ex12_turma2)
diferenca2 = set2_ex12_turma2.difference(set1_ex12_turma1)

print(f'Diferença 1 (): {diferenca1}')
print(f'Diferença 2 (): {diferenca2}')
print('\n')

# Exemplo 13
# Soma*, valor máximo*, valor mínimo*, tamanho
# * Se os valores forem todos inteiros ou reais

set1_ex13 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}

print(f'Lista 1: {set1_ex13}')

print(f'Soma: {sum(set1_ex13)}')
print(f'Valor máximo: {max(set1_ex13)}')
print(f'Valor mínimo: {min(set1_ex13)}')
print(f'Tamanho: {len(set1_ex13)}')
