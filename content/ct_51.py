'''

Iterator é diferente de iterable

Iterator (iterador):
    - Um objeto que pode ser iterado
    - Um objeto que retorna um dado, sendo um elmento por vez quando uma função next() é chamada

Iterable (iterável):
    - Um objeto que irá retornar um iterator quando a função iter() for chamada

'''

nome = 'Um texto'  # É um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable mas não é um iterator

it1 = iter(nome)    # Convertendo para um iterator
it2 = iter(numeros)
print(type(it2))

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))