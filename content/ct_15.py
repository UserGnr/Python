'''
Tuplas

As tuplas são parecidas com listas. Basicamente há 2 diferenças básicas:
1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis, ou seja, ela não muda. Toda operação em uma tupla gera uma nova tupla

Obs.: de certo modo, as tuplas são definidas pela vírgula (,) e não pelo uso dos parênteses

Assim como nas listas, as tuplas aceitam qualquer tipo de valor

Métodos para adição e remoção de elementos nas tuplas não existem, porque as tuplas são imutáveis
As duplas devem ser utilizadas sempre que não precisarmos modificar os dados contidos em uma coloção, por exemplo:
- Para os Meses do ano:
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

Por que utilizar tuplas?
- Tuplas são mais rápidas que listas
- sTuplas deixam seu código mais seguro, porque são imutáveis
'''

# Exemplo 1
# Algumas análises
print('Exemplo 1 - Algumas análises')
tupla1_ex1 = (1, 2, 3, 4, 5)
tupla2_ex1 = 1, 2, 3, 4, 5      # As tuplas também podem ser criadas dessa forma
tupla3_ex1 = (3)    # 1 valor não é uma tupla
tupla4_ex1 = (3,)   # Isso é uma tupla
tupla5_ex1 = 3,    # Isso é uma tupla
tupla6_ex1 = 1, 2, 3, 4, 5,     # Isso é uma tupla
tupla7_ex1 = tuple(range(11))
tupla8_ex1 = ()

print(f'Tupla 1: {tupla1_ex1} | tipo: {type((tupla1_ex1))}')
print(f'Tupla 2: {tupla2_ex1} | tipo: {type((tupla2_ex1))}')
print(f'Tupla 3: {tupla3_ex1} | tipo: {type((tupla3_ex1))}')
print(f'Tupla 4: {tupla4_ex1} | tipo: {type((tupla4_ex1))}')
print(f'Tupla 5: {tupla5_ex1} | tipo: {type((tupla5_ex1))}')
print(f'Tupla 6: {tupla6_ex1} | tipo: {type((tupla6_ex1))}')
print(f'Tupla 7: {tupla7_ex1} | tipo: {type((tupla7_ex1))}')
print(f'Tupla 8: {tupla8_ex1} | tipo: {type((tupla8_ex1))}')

print('\n\n')

# Exemplo 2
# Desempacotamento de tupla
# Gera erro se colocar um número diferente de elementos para desempacotar
print('Exemplo 2 - Desempacotamento de tupla')

tupla1_ex2 = ('Texto 1', 'Texto 2')

texto1_ex2, texto2_ex2 = tupla1_ex2  

print(f'Tupla 1: {tupla1_ex2}')
print(f'Variável 1: {texto1_ex2}')
print(f'Variável 1: {texto2_ex2}')

print('\n\n')

# Exemplo3
# Soma*, valor máximo*, valor mínimo* e tamanho
# * Se os valores forem todos inteiros ou reais
print('Soma*, valor máximo*, valor mínimo* e tamanho')

tupla1_ex3 = (1, 2, 3, 4, 5)

print(f'Soma: {sum(tupla1_ex3)}')
print(f'Valor máximo: {max(tupla1_ex3)}')
print(f'Valor mínimo: {min(tupla1_ex3)}')
print(f'Tamanho: {len(tupla1_ex3)}')

print('\n\n')

# Exemplo 4
# Concatenação de tuplas
print('Exemplo 4 - Concatenação de tuplas')

tupla1_ex4 = (1, 2, 3)
tupla2_ex4 = (4, 5, 6)

tupla3_ex4 = tupla1_ex4 + tupla2_ex4

print(f'Tupla 1: {tupla1_ex4}')
print(f'Tupla 2: {tupla2_ex4}')
print(f'Tupla 3 (concatenado): {tupla3_ex4}')

print('\n\n')

# Exemplo 5
# Alterar uma tupla
# Essa alteração faz sobrescrever a informação, ou seja, substitui a informação antiga pela nova
print('Exemplo 5 - Alterar uma tupla')

tupla1_ex5 = (1, 2, 3)
tupla2_ex5 = (4, 5, 6)

print(f'Tupla 1: {tupla1_ex5}')
print(f'Tupla 2: {tupla2_ex5}')

tupla1_ex5 = tupla1_ex5 + tupla2_ex5

print(f'Tupla 1(alterada): {tupla1_ex5}')

print('\n\n')

# Exemplo 6
# Verificar se determinado elemento está contido
print('Exemplo 6 - Verificar se determinado elemento está contido')

tupla1_ex6 = (1, 2, 3)

valor = 3

print(f'Tupla 1: {tupla1_ex6}')
print(f'O valor {valor} está contido na tupla? {3 in tupla1_ex6}')

print('\n\n')

# Exemplo 7
# Iterando
print('Exemplo 7 - Iterando')

tupla1_ex7 = (1, 2, 3)

print(f'Tupla 1: {tupla1_ex7}')
print('Itterando na tupla 1:')
for valor in tupla1_ex6:
    print(f'Valor: {valor}')

print('\n\n')

# Exemplo 8
# Usando o enumerate
print('Exemplo 8 - Usando o enumerate')

tupla1_ex8 = (1, 2, 3)

print(f'Tupla 1: {tupla1_ex8}')
print('Índices e valores da tupla 1:')
for indice, valor in enumerate(tupla1_ex8):
    print(f'Índice: {indice} valor: {valor}')

print('\n\n')

# Exemplo 9
# Contar um elemento específico com count
print('Exemplo 9 - Contar um elemento específico com "count"')

tupla1_ex9 = ('a', 'b', 'c', 'd', 'e', 'f')

print(f'Tupla 1: {tupla1_ex9}')
letra = 'b'
print(f'Buscando por: "{letra}" | Quantidade encontrada: {tupla1_ex9.count(letra)}')

print('\n\n')

# Exemplo 10
# Converter uma string para tupla
print("Exemplo 10 - Converter uma string para tupla")

texto1_ex10 = 'Um texto qualquer'
tupla1_ex10 = tuple(texto1_ex10)

print(f'Texto 1: {texto1_ex10}')
print(f'Tupla 1: {tupla1_ex10}')

print('\n\n')

# Exemplo 11
# Acessar valores das tuplas pelo índice
print('Exemplo 11 - Acessar valores das tuplas pelo índice')

tupla1_ex11 = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(f'Tupla 1: {tupla1_ex11}')
print(f'Índice: 1 valor: {tupla1_ex11[3]}')

print('\n\n')

# Exemplo 12
# Iterar com while
print('Exemplo 12 - Iterar com "while"')
      
tupla1_ex12 = ('Janeiro', 'Fevereiro', 'Março', 'Abril')

print(f'Tupla 1: {tupla1_ex12}')

i = 0

while i < len(tupla1_ex12):
    print(f'Índice: {i} valor: {tupla1_ex12[i]}')
    i += 1

print('\n\n')

# Exemplo 13
# Verificar em qual índice um elemento está na tupla com index
# Caso não exista, será gerado um erro
# Ele irá procurar até encontrar o primeiro
# Também é possível procurar através de um intervalor, indicando o primeiro e último índice para procurar. Vide os exemplos nos arquivos sobre "listas" referentes ao uso do "index" para mais informações
print('Exemplo 13 - Verificar em qual índice um elemento está na tupla com "index"')

tupla1_ex13 = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(f'Tupla 1: {tupla1_ex13}')

texto1_ex13 = 'Abril'
print(f'Procurando: {texto1_ex13} | índice: {tupla1_ex13.index(texto1_ex13)}')

print('\n\n')

# Exemplo 14
# Usando o slicing
# tupla[inicio:fim:passo]
# Lembrando que o fim, por padrão é fim-1, ou seja, para ir até o índice 5 é necessário colocar 5+1
print('Exemplo 14 - Usando o "slicing"')

tupla1_ex14 = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(f'Tupla 1: {tupla1_ex14}')
print(tupla1_ex14[5])
print(tupla1_ex14[5:])
print(tupla1_ex14[5:9])
print(tupla1_ex14[::2])
print(tupla1_ex14[-1:0:-1])
print(tupla1_ex14[-1:-20:-1])
print(tupla1_ex14[::-1])

print('\n\n')

# Exemplo 15
# Copiando uma tupla
# Nas tuplas não temos o Shallow Copy
print('Exemplo 15 - Copiando uma tupla')

tupla1_ex15 = (1, 2, 3)
tupla2_ex15 = tupla1_ex15   # Não há o shallow copy nas tuplas

print(f'Tupla 1: {tupla1_ex15}')
print(f'Tupla 2 (copia): {tupla2_ex15}')
