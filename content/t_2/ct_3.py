'''
Usando = no f-strings

Usar o igual no final antes da chave de fechamento faz com que seja impresso o nome da variável e o valor da variável
'''

soma = 1 + 2

print(f'Soma = {soma}')
print(f'{soma=}')
print(f'{soma = }')
print(f'{soma:.2f}')
print(f'{soma=:.2f}')


texto: str = 'Um texto qualquer'
print(f'{texto}')
print(f'{texto = }')
print(f'{texto.upper() = }')
print(f'{texto.upper()[::-1] = }')
