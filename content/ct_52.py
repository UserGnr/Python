'''
Criando a própria versão de loop


# For comumente utilizado
for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Um nome qualquer':
    print(letra)

# Dentro de um loop for, o Python usa o iter 
iter([1, 2, 3, 4, 5])
iter('Um nome qualquer')
'''


def meu_for(interavel):
    it = iter(interavel)    # Transformando o iterável em um item que pode iterar
    while True:
        try:
            print(next(it))
        except StopIteration:   # Quando não tiver mais nenhum item, é levantado a exceção 'StopIteration'
            break   # Sai do loop


meu_for('Um nome qualquer')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)