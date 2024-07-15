'''
Reduce

A partir do Python3+ a função reduce() não é mais uma função integrada (built-in)
Para usa-la é necessário importar o módulo 'functools'
Utilize a função reduce() se realmente for necessário
Em 99% das vezes um loop for é mais legível
Assim como map() e filter(), a função reduce() recebe dois parâmetros: função e iterável


Para entender o reduce()
- Uma coleção de dados:

    dados = [a1, a2, a3, ..., an]

- Uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

reduce(funcao, dados)

O reduce() funciona da seguinte forma:
   Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
   Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.
   Passo n: resn = f(resm , an)

Ou seja, em cada passo é aplicado a função passando como primeiro argumento o resultado da aplicação anterior. No final, reduce() irá retornar o resultado final
'''

from functools import reduce

# Exemplo 1
# Usando o reduce
print('Exemplo 1 - Usando o reduce')

# reduce() para multiplicar todos os números de uma lista

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

print(f'Dados: {dados}')


# Para utilizar o reduce() é necessário uma função que receba dois parâmetros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(f'Resultado (usando "reduce"): {res}')

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(f'Alteranitiva (usando "for"): {res}')