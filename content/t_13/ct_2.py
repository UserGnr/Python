'''
Decorators (Decoradores)

- São funções
- Aprimoram o comportamento de outras funções
- Também são exemplos de Higher Order Functions
- Tem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)

Decorator é diferente de Decorator Function
'''

# Exemplo 1
# Decoradores sem Syntact Sugar - sintaxe não recomendada
print('Exemplo 1 - Decoradores sem Syntact Sugar - sintaxe não recomendada')


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a)!')


teste = seja_educado(saudacao)

print(teste())

print('\n\n')

# Exemplo 2
# Decoradores com Syntact Sugar - sintaxe recomendada
print('Exemplo 2 - Decoradores com Syntact Sugar - sintaxe recomendada')


def seja_educado_2(funcao):
    def sendo2():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo2


@seja_educado_2
def saudacao2():
    print('Seja bem-vindo(a)!')

saudacao2()
