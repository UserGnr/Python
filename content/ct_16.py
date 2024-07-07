'''
Dicionários ou mapas (parte 1)

Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas

Dicionários:
- São coleções do tipo chave/valor
- Não são indexados
- São representados por chaves {}
- Chave e valor são separados por dois pontos(:)
- Tanto a chave quanto o valor podem ser de qualquer tipo de dado
- Podem ser misturado tipos de dados
- Pode ser utilizado qualquer tipo de dado (int, float, string, boolean, lista, tupla, dicionário...)
- Não pode ter 2 chaves repetidas 
'''

# Exemplo 1
# Criação de dicionários
print('Exemplo 1 - Criação de dirionários')
dicionario1_ex1 = {}
dicionario2_ex1 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ru': 'Rússia'} # Forma mais comum
dicionario3_ex1 = dict(br = 'Brasil', eua = 'Estados Unidos')   # Forma menos comum

print(f'Dicionário 1: {dicionario1_ex1} | tipo: {type(dicionario1_ex1)}')
print(f'Dicionário 2: {dicionario2_ex1} | tipo: {type(dicionario2_ex1)}')
print(f'Dicionário 3: {dicionario3_ex1} | tipo: {type(dicionario3_ex1)}')

print('\n\n')

# Exemplo 2
# Acessando os valores através da chave
# Se a chave não existir é retornado um erro
print('Exemplo 2 - Acessando os valores através da chave')

dicionario1_ex2 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ru': 'Rússia'} # Forma mais comum

print(f'Dicionário 1: {dicionario1_ex2}')
print(f'Procurando "eua": {dicionario1_ex2['eua']}')

print('\n\n')

# Exemplo 3
# Acessando os valores usando o get (recomendado)
# Se a chave não existir é retorna none
# No get é possível definir o que deve ser retornado se não encontrar o objeto com a chave informada
print('Exemplo 3 - Acessando os valores usando "get" (recomendado)')

dicionario1_ex3 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ru': 'Rússia'} # Forma mais comum

print(f'Dicionário 1: {dicionario1_ex3}')

print(f'Procurando "eua": {dicionario1_ex3.get('eua')}')
print(f'Procurando "brz": {dicionario1_ex3.get('brz')}')    # Retorna none porque não existe
print(f'Procurando "brz": {dicionario1_ex3.get('brz', 'Não encontrado')}')    # Retorna 'Não encontrado' se não existir o valor procurado

print('\n\n')

# Exemplo 4
# Verificar se determinada chave está no dicionário com in
print('Exeplo 4 - Verificar se determinada chave está no dicionário com "in"')

dicionario1_ex4 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ru': 'Rússia'} # Forma mais comum

print(f'Dicionário 1: {dicionario1_ex4}')

texto1_ex4 = 'eua'
print(f'A chave {texto1_ex4} está no dicionário 1? {texto1_ex4 in dicionario1_ex4}')
texto1_ex4 = 'brz'
print(f'A chave {texto1_ex4} está no dicionário 1? {texto1_ex4 in dicionario1_ex4}')
texto1_ex4 = 'Estados unidos'   # A busca não é feita pelo valor, a busca é feita pela chave
print(f'A chave {texto1_ex4} está no dicionário 1? {texto1_ex4 in dicionario1_ex4}')

print('\n\n')

# Exemplo 5
# Usando as tuplas como chaves em dicionários
# As tuplas podem ser usadas como chaves de dicionários e são interessantes ´por serem imutáveis
print('Exemplo 5 - Usando as tuplas como chaves em dicionários')

dicionario1_ex5 = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(f'Dicionário 1: {dicionario1_ex5}')
print(f'Tipo do dicionário 1: {type(dicionario1_ex5)}')

print('\n\n')

# Exemplo 6
# Adicionar elementos em um dicionário
print('Exemplo 6 - Adicionar elementos em um dicionário')

dicionario1_ex6 = {'jan': 100, 'fev': 120, 'mar': 300}

print(F'Dicionário 1: {dicionario1_ex6}')

# Forma 1 - Mais comum
dicionario1_ex6['abr'] = 350

print(F'Dicionário 1 com novo elemento: {dicionario1_ex6}')

# Forma 2
novo_dado1_ex6 = {'mai': 500}
dicionario1_ex6.update(novo_dado1_ex6)  # É o mesmo que dicionario1_ex6.update({'mai': 500})

print(F'Dicionário 1 com novo elemento usando o update: {dicionario1_ex6}')

print('\n\n')

# Exemplo 7
# Atualizando dados em um dicionário
# A forma de atualizar e adiocionar novos elementos em um dicionário é a mesma
print('Exemplo 7 - Atualizando dados em um dicionário')

dicionario1_ex7 = {'jan': 100, 'fev': 120, 'mar': 300}

print(F'Dicionário 1: {dicionario1_ex7}')

# Forma 1
dicionario1_ex7['fev'] = 200
print(F'Dicionário 1 | Novo valor para fevereiro:  {dicionario1_ex7}')

# Forma 2
dicionario1_ex7.update({'fev': 500})
print(F'Dicionário 1 | Novo valor para fevereiro:  {dicionario1_ex7}')

print('\n\n')

# Exemplo 8
# Remover dados com pop
# Sempre é necessário informar uma chave
# Se a chave não existir é retornado um erro
# Ao remover um objeto com pop, ele pode ser retornado dentro de uma variável
# Ao remover dom del, o valor não é retornado
print('Exemplo 8 - Remover dados')

dicionario1_ex8 = {'jan': 100, 'fev': 120, 'mar': 300}

print(F'Dicionário 1: {dicionario1_ex8}')

# Forma 1 - Mais comum
apagado = dicionario1_ex8.pop('mar')
print(F'Dicionário 1 | Removendo com pop: {dicionario1_ex8}')
print(F'Dicionário 1 | Valor apagado: {apagado}')


# Forma 2
del dicionario1_ex8['fev']
print(F'Dicionário 1 | Removendo com del: {dicionario1_ex8}')

print('\n\n')

# Exemplo 9
# Limpar o dicionário com clear
print('Exemplo 9 - Limpar o dicionário com "clear"')

dicionario1_ex9 = dict(a=1, b=2, c=3)

print(F'Dicionário 1: {dicionario1_ex9} | Tipo: {type(dicionario1_ex9)}')
dicionario1_ex9.clear()
print(F'Dicionário 1 sem dados: {dicionario1_ex9}')

print('\n\n')

# Exemplo 10
# Copiando com copy (deep copy)
print('Exemplo 10 - Copiando com "copy" (deep copy)')

dicionario1_ex10 = {'jan': 100, 'fev': 120, 'mar': 300}
dicionario1_ex11 = dicionario1_ex10.copy()

print(F'Dicionário 1: {dicionario1_ex10}')
print(F'Dicionário 2 (cópia profunda): {dicionario1_ex11}')


print('\n\n')

# Exemplo 11
# Copiando (shallow copy)
print('Exemplo 11 - Copiando (shallow copy)')

dicionario1_ex11 = {'jan': 100, 'fev': 120, 'mar': 300}
dicionario2_ex11 = dicionario1_ex11

print(F'Dicionário 1: {dicionario1_ex11}')
print(F'Dicionário 2 (cópia rasa): {dicionario2_ex11}')


print('\n\n')

# Exemplo 12
# Froma não usual para criação de dicionários com fromkeys
# O método fromkeys recebe dois parâmetros: um iterável e um valor
# O fromkeys vai gerar para cada valor do iterável uma chave e irá subir para a chave o valor informado
print('Exemplo 12 - Froma não usual para criação de dicionários com "fromkeys"')

dicionario1_ex12 = {}.fromkeys('a', 'b')
print(F'Dicionário 1: {dicionario1_ex12} | Tipo: {type(dicionario1_ex12)}')

dicionario2_ex12 = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(F'Dicionário 2: {dicionario2_ex12} | Tipo: {type(dicionario2_ex12)}')

dicionario3_ex12 = {}.fromkeys('teste', 'valor')
print(F'Dicionário 3: {dicionario3_ex12} | Tipo: {type(dicionario3_ex12)}')

dicionario4_ex12 = {}.fromkeys(['teste'], 'valor')
print(F'Dicionário 4: {dicionario4_ex12} | Tipo: {type(dicionario4_ex12)}')

dicionario5_ex12 = {}.fromkeys(range(1, 11), 'novo')
print(F'Dicionário 5: {dicionario5_ex12} | Tipo: {type(dicionario5_ex12)}')
