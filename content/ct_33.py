'''
Set comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}
'''

# Exemplo 1
# Usando set comprehension
print('Exemplo 1 - Usando set comprehension')

numeros = {num for num in range(6)}
quadrado = {num ** 2 for num in range(6)}
texto = {letra for letra in 'Um texto qualquer'}

print(f'Números: {numeros}')
print(f'Quadrado: {quadrado}')
print(f'Texto: {texto}')    # Lembrando que os sets não possuem ordem e também não possuem duplicadas