'''
Try e except

- O bloco try/except é usado para tratar erros que podem ocorrer no código. Previnindo assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.
- Forma geral:
try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema
- Tratar erro de forma genérica não é a melhor forma de tratamento de erros
- O ideal é SEMPRE tratar de forma específica
- É possível efetuar diversos tratamentos de erros de uma vez
'''


'''
# Exemplo 1
# Tratando erros genéricos
print('Exemplo 1 - Tratando erros genéricos')

try:
    teste()
except:
    print('Deu algum problema')
# Tenta executar a função teste(), caso não seja encontrada imprime a mensagem de erro
'''

'''
# Exemplo 2
# Tratando um erro genérico
print('Exemplo 2 - Tratando um erro genérico')
try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar o len(), caso você encontre erros é impresso a mensagem de erro
'''

'''
# Exemplo 3
# Tratando um erro específico
print('Exemplo 3 - Tratando um erro específico')

try:
    teste()
except NameError:
    print('Você está utilizando uma função inexistente')
'''

'''
# Exemplo 4
# Tratando um erro específico e nomeando-o
print('Exemplo 4 - Tratando um erro específico e nomeando-o')

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
'''

'''
# Exemplo 5
# Tratando vários erro específicos e nomeando-os
print('Exemplo 5 - Tratando vários erro específicos e nomeando-os')

try:
    teste()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')
'''

'''
# Exemplo 6
# Outro exemplo
print('Exemplo 6 - Outro exemplo')

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Valor"}

print(pega_valor(dic, 8))
'''
