'''
Anotations

- Mostra os tipos
'''

# Exemplo 1

import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(circunferencia.__annotations__)
print(__annotations__)  # Não imprime nada

# Exemplo 2

class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='Um texto qualquer', idade=37, peso=69.5)

print(p.__dict__)
# print(p.__annotations__)  # Retorna um erro - não tem annotations
print(p.andar.__annotations__)
print(p.__init__.__annotations__)
