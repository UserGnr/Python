'''
Tipos em comentários

- O python permite que também seja possível escrever os tipo de dados em comentários
- Essa forma é tem a mesma finalidade, porém, pode ser menos legível dependendo do caso
- Essa forma é menos usual
'''


import math

# Exemplo 1
def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


# print(circunferencia(8))

#  print(circunferencia('Texto'))

# Exemplo 2
def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


# cabecalho1(texto=43, alinhamento='texto')

# Exemplo 3
def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho2(texto='42', alinhamento=False)

nome = 'Um texto qualquer'  # type: str
