'''
Preservando metadatas com wraps

Metadados são dados intrísecos dos arquivos
wraps são funções que envolvem elementos com diversas finalizades
'''

'''
# Exemplo em que será usado o """Eu sou uma função (logar) dentro de outra""" como retorno para o soma.__doc__
def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


print(soma(10, 30))
print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois números.
print(help(soma))  # Soma dois números.
'''

# Exemplo em que será usado o """Soma dois números.""" como retorno para o soma.__doc__
# Correto!

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


print(soma(10, 30))
print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois números.

print(help(soma))
