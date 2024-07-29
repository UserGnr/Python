'''
Any e all

- all(): retorna True se todos os elementos do iterável são verdadeiros ou se o iterável está vazio
    Normalmente, um iterável vazio convertido em boolean é False, mas no all() é retornado como True
- any(): tetorna True se qualquer elemento do iterável for verdadeiro. 
    Caso o iterável esteja vazio é retornado False
'''

# Exemplo 1
# Usando all
print('Exemplo 1 - Usando "all"')

print(f'Referência 1: {all([0, 1, 2, 3, 4])}')  # Todos os números são verdadeirso? False
print(f'Ref 2: {all([1, 2, 3, 4])}')  # Todos os números são verdadeiros? True
print(f'Ref 3: {all([])}')  # Todos os números são verdadeiros? True
print(f'Ref 4: {all((1, 2, 3, 4))}')  # Todos os números são verdadeiros? True
print(f'Ref 5: {all({1, 2, 3, 4})}')  # Todos os números são verdadeiros? True
print(f'Ref 6: {all('Um nome qualquer')}')  # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(f'Ref 7: {all([nome[0] == 'C' for nome in nomes])}')  # Todos os nomes começam com a letra 'c'? True

print(f'Ref 8: {all([letra in 'aeiou' for letra in 'eio'])}')  # Cada letra de 'eio' está dentro de 'aeiou'? True
print(f'Ref 9: {all([letra for letra in 'eio' if letra in 'aeiou'])}')  # Retorna True pois é avaliado o tipo de dado de 'letra' no retorno, alterar os dados para analisar
print(f'Ref 10: {all([num % 2 == 0 for num in [4, 2, 10, 6, 8]])}')   # Todos os número são pares? True
print(f'Ref 11: {all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])}')   # Retorna True pois é avaliado o tipo de dado de 'num' no retorno, alterar os dados para analisar. Mesmo colocando todos os números da lista como ímpar, o retorno é True, pois no 'all' um iterável vazio convertido em boolean é True

print('\n\n')

# Exemplo 2
# Usando any
print('Exemplo 2 - Usando "any"')

print(f'Ref 12: {any([0, 1, 2, 3, 4])}')  # True, pois tem pelo menos 1 valor considerado True
print(f'Ref 13: {any([0, False, {}, (), []])}')  # False, pois todos os valores são considerados False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(f'Ref 14: {any([nome[0] == 'C' for nome in nomes])}') # 'nome' na posição 0 tem o 'C'? True

print(f'Ref 15: {any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0])}')   # Retorna True pois tem pelo menos 1 valor que é True
