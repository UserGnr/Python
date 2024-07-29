'''
Funções

- Funções são pequenas partes de código que realizam tarefas específicas
- Pode ou não receber entradas de dados
- Pode ou não retornar uma saída de dados
- Comumente utilizadas em procedimentos repetitivos
- DRY (Don't Repeat Yourself / não repita a si mesmo): em um sistema deve existir uma representação única, livre de ambiguidades/repetições desnecessárias
- As funções Built-in são funções integradas com a linguagem de programação, o print é um exemplo
- Para criar uma função, é possível utilizar qualquer tipo de dado, inclusive funções detro de funções

Obs.: 
- se uma função estiver realizando várias tarefas, é recomendado fazer uma verificação para que seja simplificada
- para tirar dúvida sobre as funções basta, por exemplo: print(help(print))

- Exemplos de funções:
    - print()
    - len()
    - max()
    - min()
    - count()
    - list()
    - append()
    - e muitas outras

Variável local sobrepõem a variável global, ou seja, a local terá preferência
Evite variáveis globais em um função
'''

# Exemplo 1
# Definindo uma função
print('Exemplo 1 - Definindo uma função')
'''
def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:
def: palavra reservada para definir uma função
':': o bloco de código é aberto com dois pontos ':'
    : a identação é de 4 espaços, normalmente
nome_da_funcao: SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case). O Ideal é que o nome da função seja intuitivo, representando o que a função faz
parametros_de_entada: fica entre parênteses. Esses parâmetros são opcionais, separados por vírgula caso tenha mais de um
bloco_da_funcao: também chamado de corpo da função ou implementação, é onde o processamento da função acontece, podendo ter ou não retorno da função.
'''


def diz_oi():
    print('Oi')


diz_oi()

"""
OBS:
1 - Essa função só executa 1 tarefa, a única coisa que ela faz é dizer 'oi'
2 - Essa função não recebe nenhum parâmetro de entrada
3 - Essa função não retorna nada
4 - Para chamar a função é preciso usar o parênteses '()'
"""

print('\n\n')

# Exemplo 2
# Criar uma variável da função
print('Exemplo 2 - Criar uma variável da função')
'''
# Em Python é possível criar uma variáveis do tipo de uma função e executar esta função através da variável
'''


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


# cantar_parabens()     # Chamando a função para que seja executada, como no exemplo anterior
canta = cantar_parabens     # Atribuindo a função 'cantar_parabens' na variável 'canta'

canta()
print(type(canta))
