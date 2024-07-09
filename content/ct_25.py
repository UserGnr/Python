'''
Documentando funçõs com docstrings (""" """)

- É possível documentação de funções usando docstrings
- Podemos ter acesso á documentação de uma função em Python utilizando a propriedade  __doc__ ou com a função help()

'''

# Exemplo 1
print('Exemplo 1')


def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi! '


print('Usando __doc__')
print(diz_oi.__doc__)
print('Usando help')

print(help(diz_oi()))

print('\n\n')

# Exemplo 2
print('Exemplo 2')


def potencia(numero, expoente=2):
    """
    Função que retorna a potência, com base no 'numero' (base) e 'expoente'.
    :param 'numero': base
    :param 'expoente': expoente. Por padrão é 2.
    :return: retorna a potência do 'numero' e 'expoente'.
    """
    return numero ** potencia

print('Usando __doc__')
print(potencia.__doc__)
print('Usando help')
print(help(potencia))

# Também é possível usar o __doc__ e o help através do terminal
