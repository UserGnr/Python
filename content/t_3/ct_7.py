'''
Checagem de dados com MyPy

- Mesmo declarando o tipo dos dados das variáveis, em Python, permite o uso de outros tipos
- O erro normalmente só aparece quando faz uso de um dado que não permite alguma operação específica
- Para verificar onde esta ocorrendo essa alguma incompatibilidade com o tipo especificado no código pode se utilizar o Mypy
- O MyPyFaz a checagem do tipo do uso e aponta onde está ocorrendo a falha para que possa ser corrigido
- Para usa-lo basta escrever, no terminal: mypy seu_arquivo.py
- É necessário instalar a bibliotéca mypy instalada
'''


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('um texto qualquer'))
print(cabecalho('um texto qualquer', alinhamento=1))
print(cabecalho('um texto qualquer', alinhamento=True))
# cabecalho(texto=4, alinhamento=True)    # Retorna erro pois o tipo inteiro não pode ser utilizado o title
