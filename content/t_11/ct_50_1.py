'''
Módulos

- Em Python, módulos são arquivos Python
- A importação dos módulos, preferencialmente, devem ser usados topo do arquivo
- Os módulos Builtin (módulos integrados) são os módulos que já vem instalados no Python
- https://docs.python.org/3/py-modindex.html
'''

# Exemplo 1
# Importando todo o módulo (não recomendado)
# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem dentro do módulo ficarão disponíveis (em memória). Caso você saiba quais funções você precisa utilizar deste módulo, então está não seria a forma ideal de utilização.
print('Exemplo 1 - Importando todo o módulo (não recomendado)')

import random

# No módulo random possui várias funções para geração de números pseudo-aleatório

print(random.random())  
# Como foi importado o módulo completo é necessário utilizar a função random() do pacote random com o nome do pacote e o nome da função separados por ponto
# random() é uma função do módulo random que gera um número real pseudo-aleatório entre 0 e 1
# A função random() é apenas uma função dentro do módulo random.

print('\n\n')

# Exemplo 2
# Importando uma função específica do módulo (recomendado)
# Um problema é declarar uma variável que tenha o mesmo nome de alguma função do módulo
print('Exemplo 2 - Importando uma função específica do módulo (recomendado)')

from random import random
# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())
# Note que ao importar apenas a função random() do módulo ramdom, basta colocar a função ramdom() sem o nome do módulo e, também, sem o ponto

print('\n\n')

# Exemplo 3
# Importar todas as funções de um módulo utilizando o *
print('Exemplo 3 - Importar todas as funções de um módulo utilizando o *')

from random import *

print(random())
# Observe que dessa forma não é necessário colocar o nome do módulo e nem o ponto
# É preciso ter cuidado ao usar, visto que pode ser criado pelo usuário uma variável que tenha o mesmo nome de algo do módulo

print('\n\n')

# Exemplo 4
# Utilizando alias (apelidos) para módulos/funções
print('Exemplo 4 - Utilizando alias (apelidos) para módulos/funções')

from random import randint as rdi

print(rdi(5, 89))

print('\n\n')

# Exemplo 5
# Utilizando alias (apelidos) para vários módulos/funções
print('Exemplo 5 - Utilizando alias (apelidos) para vários módulos/funções')

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

print('\n\n')

# Exemplo 6
# Tuplas para colocar múltiplos imports de um mesmo módulo (recomendável)
print('Exemplo 6 - Tuplas para colocar múltiplos imports de um mesmo módulo (recomendável)')

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Texto', 'Programação', 'Python']
shuffle(lista)
print(lista)

print(choice('Python'))