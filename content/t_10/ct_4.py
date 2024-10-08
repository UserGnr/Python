'''
Try, except, else e finally

- Dica de quando e onde tratar código: 
    TODA ENTRADA DEVE SER TRATADA!
    "A função do usuário é DESTRUIR seu sistema"


Else - é executado somente se não ocorrer o erro
Finally - é SEMPRE executado. Independente se houve exceção ou não
- O finally, geralmente, é utilizado para fechar ou desalocar recursos

O desenvolvedor é responsável pelas entradas das suas funções. Então, é necessário trata-las!
'''

'''
# Exemplo 1
# Usando o else
print('Exemplo 1 - Usando o "else"')

try:
   num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
'''

'''
# Exemplo 2
# Usando o finally
print('Exemplo 2 - Usando o finally')

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')
'''

'''
# Exemplo 3
# Exemplo mais complexo (ERRADO)
print('Exemplo 3 - Exemplo mais complexo (ERRADO)')


def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')
'''

'''
# Exemplo 4
# Exemplo mais complexo (CORRETO)
print('Exemplo 4 - Exemplo mais complexo (CORRETO)')

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
'''

'''
# Exemplo 5
# Exemplo mais complexo genérico
print('Exemplo 5 - Exemplo mais complexo genérico')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
'''


# Exemplo 6
# Exemplo mais complexo semi-genérico
print('Exemplo 6 - Exemplo mais complexo semi-genérico')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
