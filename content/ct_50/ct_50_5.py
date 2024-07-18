'''
Dunder name e dunder main

Dunder: Doble Under '__'
Dunder Name: __name__
Dunder Main: __main__


- Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando Double Under para não gerar conflito com os nomes desses elementos na programação
- Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal
    Main: Significa principal

'''


print(__name__) # Como esse arquivo será executado diretamente, então o valor de __name__ será __main__

import pk_2.cm_5

print(pk_2.cm_5.__name__)   # Como o arquivo pm_5 da pasta pk_2 está sendo importada, o retorno de __name__ será o nome do arquivo

if __name__ == '__main__':
    print('Executando apenas se esse for o módulo pincipal')

# Isso é útil caso seja necessário executar coisas de um módulo que só podem ser executadas caso o módulo seja executado diretamente