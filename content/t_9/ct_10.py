'''
Len, Abs, Sum e Round

Len
- Retorna o tamanho (ou seja, o número de itens) de um iterável
- Por debaixo dos panos, a função len() o Python faz o seguinte:
    print('Um texto qualquer'.__len__())
    __ é chamado de Dunder

Abs
- Retorna o valor absoluto de um número inteiro ou real
- Basicamente torna o numero negativo em positivo e o pisitivo mantém como positivo

Sum
- retorna a soma total dos elementos, incluindo o valor inicial
- Recebe como parâmetro um iterável, podendo receber um valor inicial
    O valor inicial default é = 0

Round
- Retorna um número arredondado para n digitos de precisão após a casa decimal
- Caso a precisão não seja informada, é retornado o inteiro mais próximo da entrada
'''

# Exemplo 1
# Usando len
print('Exemplo 1 - Usando "len"')

print(len('Um texto qualquer'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
print(len(range(0, 10)))

print('\n\n')

# Exemplo 2
# Usando abs
print('Exemplo 2 - Usando "abs"')

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

print('\n\n')

# Exemplo 3
# Usando sum
print('Exemplo 3 - Usando "sum"')

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([3.145, 5.678]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

print('\n\n')

# Exemplo 4
# Usando round
print('Exemplo 4 - Usando "round"')

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2121212121, 2))
print(round(1.21999999, 2))
print(round(1.2121212121))
