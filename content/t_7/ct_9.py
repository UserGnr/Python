'''
Ordem dos parâmetros de uma função

Nas funções, pode-se ter (NESTA ORDEM):
- Parâmetros obrigatórios;
- *args;
- Parâmetros detault (não obrigatórios);
- **kwargs
É importante manter essa ordem na declaração
'''

# Exemplo 1
# Função com a ordem correta de parâmetros
print('Exemplo 1 - Função com a ordem correta de parâmetros')

# Função com a ordem correta de parâmetros
def mostra_info(a, b, *args, instrutor='Nome padrão se não existir', **kwargs):
    return [a, b, args, instrutor, kwargs]


# # Função com a ordem incorreta de parâmetros
# def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
#     return [a, b, args, instrutor, kwargs]


a = 1
b = 2
args = (3,)
instrutor = 'Sem nome'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}

print(mostra_info(1, 2, 3, sobrenome='Sobrenome', cargo='Instrutor'))
# Comentário
# 1 e 2 são argumentos obrigatórios
# 3 é um arg (vai virar uma tupla)
# sobrenome='University' e cargo='Instrutor' são kwargs
# Observe que instrutor não recebe valores e será usado o valor padrão
# Desse modo:
# a = 1
# b = 2
# args = (3,)
# instrutor = 'Nome padrão se não existir'
# kwargs = {'sobrenome': 'Sobrenome', 'cargo': 'Instrutor'}
