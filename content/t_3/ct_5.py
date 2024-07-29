'''
Escopo de variáveis

Dois casos de escopo:
1 - Variáveis globais:
- Variåveis globais tem seu escopo reconhecido em todo o programa.
2 - Variáveis locais;
- Variáveis tocais são limitadas/reconhecidas apenas no bloco onde foram declaradas.

Para declarar variáveis em Python fazemos:
nome da variavel = valor da variavel

Python é uma linguagem de tipagem dinânica. Isso significa que ao declararmos uma variável, não colocamos o tipo de dado que a variável é, seu tipo é inferido ao atribuirmos o valor à mesma.
Em outras linguagens de programação o conceito de tipagem é diferente.
'''

# Variável global

numero = 42
print(numero)
print(type(numero))

    # Reatribuição de variável: alterar o tipo de variável para outro
numero = "texto"    # O valor da variável está deixando de ser número inteiro e está passando a ser um texto do tipo string
print(numero)
print(type(numero))

# Variável local
numero = 42

if numero > 10:
    novo = numero + 10  # A variável novo só existe se a condição for verdadeira, se não for verdadeira, a variável não existirá
    print(novo)

print(novo) # Caso a regra do if acima seja falsa, a variável 'novo' não existirá, portanto, retornará um erro na execução. É necessário tomar cuidado no uso de variáveis locais.
# O ideal é tornar as variáveis locais em globais em python, declarando-as onde sempre seram acessadas inicialmente, por exemplo:
numero = 42
novo = 0
if numero > 10:
    novo = numero + 10
    print(novo)
print(novo)
