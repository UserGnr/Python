'''
Funções com Parâmetro Padrão (Default Paramters)

- São funções que tem o parâmetro opcional
- Em funções Python, os parâmetros com valores default (padrão), auqeles que são opcionais, DEVEM sempre estar ao final da declaração

Por quê utilizar parâmetros com valor default?
- Nos permite ser mais flexíveis nas funções
- Evita erros com parâmetros incorretos
- Nos permite trabalhar com exemplos mais legíveis de código

Quais tipos de dados podemos utilizar como valores default para parâmetros?
- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;

'''

# Exemplo 1
# Parâmetro obrigatorio
print('Exemplo 1 - Parâmetro obrigatorio')


def quadrado(numero):
    return numero ** 2


print(f'Quadrado de 4: {quadrado(4)}')
# print(f'Quadrado de nada: {quadrado()}')    # Retorna um erro

print('\n\n')

# Exemplo 2
# Parâmetro opcional
print('Exemplo 2 - Parâmetro opcional')


def quadrado2(numero = 2):
    return numero ** 2


print(f'Quadrado de 4: {quadrado2(4)}')
print(f'Quadrado de nada: {quadrado2()}')    # Se não for informado, a operação será realizado com o 2

print('\n\n')

# Exemplo 3
# Parametro obrigatório e opcional


def potencia(numero, expoente = 2):
    return numero ** expoente


print(f'Potência do valor 2 com expoente 2: {potencia(2, 2)}')
print(f'Potência do valor 3 com expoente 3: {potencia(numero = 3, expoente =3)}')
print(f'Potência do valor 2 com expoente 3: {potencia(expoente =3, numero = 2)}')
print(f'Potência do valor 4 com expoente 2: {potencia(4, 2)}')
print(f'Potência do valor 4 com expoente padrão: {potencia(4, 2)}')
# print(f'Potência sem valor com expoente padrão: {exponencial()}')    # O valor foi colocado como obrigatório, portanto retorna um erro


print('\n\n')
