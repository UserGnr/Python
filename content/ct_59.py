'''
Decorators com diferentes assinaturas

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada
'''

# Exemplo 1
# Decorators com diferentes assinaturas
print('Exemplo 1 - Decorators com diferentes assinaturas')


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def pedido(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'


@gritar
def lol():
    return 'lol'


print(saudacao('Felicity'))
print(pedido('Picanha', 'Batata Frita'))
print(lol())

# Também pode ser utilziado parâmetros nomeados
print(pedido(acompanhamento='Batata Frita', principal='Picanha'))

print('\n\n')


# Exemplo 2
# Decorator com argumentos
print('Exemplo 2 - Decorator com argumentos')

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))
print(soma_dez(1, 21))
print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('sanduiche', 'pizza'))
