'''
7 - Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua área.
'''

from math import sqrt

# Em construção
class Triangulo:
    def __init__(self, *lados: float) -> None:
        """ Instancia a classe """
        self.__validacao(lados)
        self.__lados: tuple = lados

    @staticmethod
    def __validacao (lados: tuple) -> None:
        """ Valida se é um triângulo válido """
        if len(lados) != 3:
            raise ValueError('O triângulo deve ter 3 lados')
        
        if any(not isinstance(lado, (int, float)) for lado in lados) :
            raise ValueError('Devem ser informado apenas números para os lados do triângulo')
        
        if sum(sorted(lados)[:2]) < sorted(lados)[-1]:
            raise ValueError('A soma dos lados menores do triângulo deve ser maior que o tamanho do lado maior')

    @property
    def lados(self) -> tuple:
        """ Exibe os lados do triângulo """
        return self.__lados

    @lados.setter
    def lados(self, lados: tuple) -> None:
        """ Atualiza os lados do triângulo """
        self.__validacao(lados)
        self.__lados = lados

    def area(self) -> float:
        """ Cálculo da área utilizando a fórmula de Heron """
        a, b, c = self.__lados
        sp = sum(self.__lados)/2
        return sqrt(sp * (sp - a) * (sp - b) * (sp - c))


if __name__ == '__main__':
    triangulo1 = Triangulo(9, 5, 6)
    print(f'{triangulo1.lados = }')
    triangulo1.lados = 5, 5, 6
    print(f'{triangulo1.lados = }')
    print(f'{triangulo1.area() = }')
    