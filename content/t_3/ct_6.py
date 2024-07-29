'''
Tipagem dinâmica, type hinting e MyPy

O Python é uma linguagem do tipo de tipagem dinâmica, ou seja, não é necessário especificar o tipo da variavél

Vantagens:
- Facilita encontrar erros durante a execução do código
- Evita erros e bugs no código
- Melhora legibilidade e a documentação do código
- Melhora a funcionalidade das IDE's, por exemplo do autocomplete e sugestões
- É opcional
Desvantagens:
- O recurso foi disponibilisado a partir da vs 3.5 e completado na vs 3.7
- Tem uma queda no desempenho do programa (velocidade)


Exemplos da definição correta e incorreta:
    # Correto
    texto: str
    # Incorreto
    texto:str
    texto : str

    # Correto
    ) -> str
    # Incorreto
    )->str
    ) ->str

    # Correto
    alinhamento: bool = True
    # Incorreto
    alinhamento:bool=True
    alinhamento : bool = True
    alinhamento : bool=True
    alinhamento: bool= True

'''

# Exemplo 1
# Simples

# Recomendada
texto: str = 'Olá'
numero: int = 5
ativo: bool = True
numero_flutuante: float = 5.5

# Correta mas não recomendada
numero_outra_forma: float
numero_outra_forma = 5.6


# Exemplo 2
# Em uma função

import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

def imprimir_texto(texto: str) -> None:     # Como não tem retorno definido na função, o retorno é None
    print(texto)


# Exemplo 3
# Em uma clasee


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='Nome de alguém', idade=37, peso=69.5)


# Exemplo 4
# Em coleções

nomes: list = ['Primeiro', 'Segundo']
versoes: tuple = (3, 4, 7)
opcoes: dict = {'ar': True, 'banco_couro': True}
valores: set = {3, 4, 5, 6}

# Exemplo 5
# Em dados dentro das coloções

nomes2: list[str] = ['Geek', 'University']
versoes2: tuple[int, int, int] = (3, 7, 4)
opcoes2: dict[str, bool] = {'ar': True, 'bancos_couro': True}
valores2: set[int] = {3, 4, 5, 6}
