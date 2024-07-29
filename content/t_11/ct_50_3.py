'''
Módulos customizados

- Assim como os módulos Python, os módulos customizados são arquivos Python, porém são os arquivos que nós criamos
- Pode ser necessário especificar a pasta que o módulo está

Módulos externos

- Para a instalação de módulos esternos é utilizado o gerenciador de pacotes Python chamado Pip (Python Installler Package)
- Digite no terminal:
    pip install nome_do_módulo
- Todos os pacotes externos oficiais em: https://pypi.org
'''

# Exemplo 1
# Importando uma um módulo
print('Exemplo 1 - Importando um módulo')

import cm_1 as cm_1

lista = [1, 2, 3, 4]

soma = cm_1.soma_impares(lista)

print(soma)
print(cm_1.lista_teste)

# Exemplo 2
# Importando uma função específica do nosso módulo
print('Exemplo 2 - Importando uma função e variável específica do nosso módulo')

from cm_1 import soma_impares, lista_teste

lista = [1, 2, 3, 4]

soma = soma_impares(lista)
print(soma)
print(lista_teste)
