'''
Debugando com PDB

PDB - Python Debugger
Bug - Inseto

- Existem várias formas de debugar um código, seja através do debug do IDE ou de alguma ferramenta da própria linguagem
- Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()
- Comandos básicos do PDB:
    l (listar onde estamos no código)
    n (próxima linha)
    p (imprime variável)
    c (continua a execução - finaliza o debugging)
- A partir do Python 3.7 não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como função built-in (integrada) chamada breakpoint()
- É necessário ter cuidado com conflitos entre nomes de variáveis e os comandos do pdb. Como pode existir nomes das variávels com os mesmos dos comandos do pdb, deve ser utilizado o comando 'p' para imprimir as variáveis, ou seja: 
    p nome_da_variavel
'''

# Importando a bibliotéca

'''
# Exemplo 1
# Usando o PDB
print('Exemplo 1 - Usando o PDB')

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)
'''

'''
# Exemplo 2
# Usando o PDB - importando e usando o comando 
print('Exemplo 2 - Usando o PDB - importando e usando o comando ')
"""
Por que utilizar este formato:
- O debug é utilizado durante o desenvolvimento
- Custumamos realizar todos os imports de bibliotecas no início do arquivo
- Por isso, ao invés de colocarmos o import do pdb no início do arquivo, é colocado somente onde vamos debuggar, e ao finalizar já fazemos a remoção
"""

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)
'''

'''
# Exemplo 3
# Usando o breakpoint
# A partir do Python 3.7 não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como função built-in (integrada) chamada breakpoint()
print('Exemplo 1 - Usando o "breakpoint"')

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)
'''


# Exemplo 4
# Cuidado com conflitos entre nomes de variáveis e os comandos do pdb
# Como pode existir nomes das variávels com os mesmos dos comandos do pdb, deve ser utilizado o comando 'p' para imprimir as variáveis, ou seja: p nome_da_variavel


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))
