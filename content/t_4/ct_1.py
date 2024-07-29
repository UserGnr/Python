'''
Estruturas condicionais (if, elif e else)

if      se
elif    senão se
else    senão

Obs.:
- O elif e o else são opcionais
- O elif deve ter uma regra

'''

# Fazer testes nos valores e nos operadores dos exemplos abaixo 

# Exemplo 1
print('Exemplo 1')

idade = 18

if idade > 18 and idade < 25:
    print('Idade está entre 19 anos e 25')
elif idade == 25 or idade == 26:
    print('Idade é igual a 25 ou 26')
elif idade == 27:
    print('Idade é igual a 27')
elif idade >= 28:
    print('A idade é maior ou igual a 28 anos')
else:
    print('Idade menor que 18')

print("\n")

# Exemplo 2
print('Exemplo 2')

ativo = False
logado = False

if ativo and logado:
    print("Usuário ativo e logado")
elif ativo == False and logado == False:
    print ("O usuário não está ativo e não está logado")
elif ativo:
    print('O usuário está ativo')
else:
    print('O usuário está logado')

# Outra forma de escrever o exemplo acima
if ativo is logado and ativo is True:
    print("Usuário ativo e logado")
elif not ativo and not logado:
    print ("O usuário não está ativo e não está logado")
elif not logado:
    print('O usuário não está logado')
elif ativo is False:
    print('O usuário não está ativo')
else:
    print('Testando')
