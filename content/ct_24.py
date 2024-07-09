'''
Variáveis locais e globais em funções
'''

# Exemplo 1
# Variável global
# Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.
print('Exemplo 1 - Variável global')

texto = 'Linguagem'  # Variável global


def diz_oi():
    texto = 'Python'  # Variável local
    return f'Oi {texto}'


texto = 'Linguagem 2'  # Variável global

print(diz_oi())

print('\n\n')

# Exemplo 2
# Variável local
print('Exemplo 2 - Variável local')


def diz_oi2():
    novo_texto = 'testando'  # Variável local
    return f'Texto: {novo_texto}'


print(diz_oi2())

print('\n\n')

# Exemplo 3
# Usando o valor de uma variável global em uma função
# ATENÇÃO com variáveis globais (Se puder evitar, evite em uma função!)
print('Exemplo 3 - Usando o valor de uma variável global em uma função')

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

print('\n\n')

# Exemplo 4
# Funções dentro de funções
print('Exemplo 4 - UFunções dentro de funções')


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        # nonlocal que dizer que não é local e também não é global, quer dizer que é a variável que está na função acima

        contador = contador + 1
        return contador
    return dentro()


print(fora())
# print(dentro())  # Gera erro porque a função dentro só está disponível dentro da função 'fora'