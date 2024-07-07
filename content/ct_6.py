'''
Booleano
True    Verdadeiro
False   Falso
Obs: em Python é errado que o True e False fiquem com as letras minúsculas 
'''

print('Booleano')

# Fazer testes nos valores e nos operadores abaixo
ativo = False

if ativo:
    print('Verdadeiro')
else:
    print('Falso')

print(ativo)
print(not ativo)

print('\n\n')

'''
None

O tipo de dado None em Python representa o tipo sem tipo, poderia ser conhecido como tipo vazio, porém dizer que é um tipo sem tipo é mais apropriado

O tipo None é SEMPRE com o 'N' em maiúsculo e as demais em minúsculo
O tipo None é considerado como False

None pode ser utilizado para inicializar uma variável, antes de receber um valor final 
'''

print('None')

numeros = None

print(f'Valor da variável numeros: {numeros}')
print(f'Tipo da variável numeros: {type(numeros)}')

numeros = 1.44, 1.34, 5.67

print(f'Valor da variável numeros: {numeros}')
print(f'Tipo da variável numeros: {type(numeros)}')
