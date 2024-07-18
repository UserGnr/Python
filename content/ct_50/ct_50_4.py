'''
Pacotes

Módulo: é apenas um arquivo Python que pode ter diversas funções para utilizarmos
Pacote: é um diretório contendo uma coleção de módulos (vários módulos)

- Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py
- Nas versões do Python 3.x, não é mais obrigatória a utilização deste arquivo, mas normalmente ainda é utilizado para manter compatibilidade.
'''

# Executando vários testes simultâneamente

from pk_1 import cm_2
from pk_1 import cm_3

from pk_1.pk_1_1 import cm_5
from pk_1.pk_1_1 import cm_6

from pk_1.pk_1_1.cm_5 import testando_tambem

print(cm_2.pi)
print(type(cm_2.pi))
print(cm_6.variavel_teste)
print(testando_tambem)
