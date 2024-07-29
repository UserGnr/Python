'''
Raise

- Levanta excessões
- Não é uma função, é uma palavra reservada, assim como def ou qualquer outra em Python
- Criar nossas próprias exceções e mensagens de erro
- A forma geral de utilização é:
    raise TipoDoErro('Mensagem de erro')
- O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado
'''

'''
# Exemplo 1
# Usando o raise
print('Exemplo 1 - Usando o "raise"')


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

    
colore('True', 7)
'''

'''
# Exemplo 2
# Refatorando o exemplo anterior
print('Exemplo 2 - Refatorando o exemplo anterior')


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Um texto qualquer', 'preto')
'''

# Exemplo 3
# Exemplo real
print('Exemplo 3 - Exemplo real')

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Um texto qualquer', 'preto')
