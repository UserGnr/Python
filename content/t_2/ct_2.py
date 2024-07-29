'''
Operador walrus

- Permite fazer a atribuição e retorno do valor em uma única expressão
- Operador walrus :=
'''

# Exemplo 1
# Sem walrus
nome = 'Texto'

# Com walrus
print(nome := 'Texto')

# Exemplo 2
# Sem walrus
cesta = []
fruta = input('Digite uma fruta: ')
while fruta != 'maça':
    cesta.append(fruta)
    fruta = input('Digite uma fruta: ')

# Com walrus
cesta2 = []
while (fruta := input('Digite uma fruta: ')) != 'maça':
    cesta2.append(fruta)