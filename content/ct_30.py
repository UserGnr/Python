'''
List comprehension (parte 2)

Pose-se adicionar estruturas condicionais lógicas às list comprehension
'''

# Exemplo 1
# Usando list comprehension com if
print('Exemplo 1 - Usando list comprehension com "if"')

numeros_ex1 = list(range(10))

print(f'Lista 1: {numeros_ex1}')

pares_ex1 = [numero for numero in numeros_ex1 if numero % 2 == 0]
impares_ex1 = [numero for numero in numeros_ex1 if numero % 2 != 0]

print(f'Lista 2 (números pares): {pares_ex1}')
print(f'Lista 3 (números ímpares): {impares_ex1}')

print('\n\n')

# Exemplo 2
# Refatorando o exemplo 1
print('Exemplo 2 - Refatorando o exemplo 1')

numeros_ex2 = list(range(10))

# Qualquer número par quando dividido por 2 tem como resto 0. Em Python, '0' é False e 'not False' = True
pares_ex2 = [numero for numero in numeros_ex2 if not numero % 2]

# Qualquer número ímpar quando dividido por 2 tem o resto diferente de 0. Em Python, qualquer número diferente de 0 é True
impares_ex2 = [numero for numero in numeros_ex2 if numero % 2]

print(f'Lista 1: {numeros_ex2}')
print(f'Lista 2 (números pares): {pares_ex2}')
print(f'Lista 3 (números ímpares): {impares_ex2}')

print('\n\n')

# Exemplo 3
# Outra forma de utilização do if em uma list comprehension
print('Exemplo 3 - Outra forma de utilização do if em uma list comprehension')

numeros_ex3 = list(range(10))

calculo = [numero * 2 if not numero % 2 else numero / 2 for numero in numeros_ex3]

print('Se os números forem pares dobra, se forem ímpares divide pela metade')
print(f'Lista 1: {numeros_ex2}')
print(f'Lista 2 (calculada): {calculo}')

