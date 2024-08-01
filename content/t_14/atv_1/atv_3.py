'''
3 - Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e a altura. Implemente métodos para calcular a área e o perímetro do retângulo.
'''

class Retangulo():


    def __init__(self, largura: float, altura: float) -> None:
        self.__largura: float = largura
        self.__altura: float = altura
    

    @property
    def largura(self) -> float:
        return self.__largura

        
    @property
    def altura(self) -> float:
        return self.__altura


    def area(self) -> float:
        return self.__largura * self.__altura
    

    def perimetro(self) -> float:
        return 2 * self.__largura + 2 * self.__altura
    

if __name__ == '__main__':
    retangulo1: Retangulo = Retangulo(5, 2)
    print(f'{retangulo1.altura = }')
    print(f'{retangulo1.largura = }')
    print(f'{retangulo1.area() = }')
    print(f'{retangulo1.perimetro() = }')
