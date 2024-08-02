'''
1 - Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e métodos para calcular a área e o perímetro do círculo.
'''

class Circulo:

    pi: float = 3.14159265359


    def __init__(self, raio: float) -> None:
        self.__raio: float = raio
    

    @property
    def raio(self) -> float:
        return self.__raio
    

    @raio.setter
    def raio(self, raio: float) -> None:
        self.__raio = raio
    

    def area(self) -> float:
        return Circulo.pi * self.__raio ** 2
    

    def perimetro(self) -> float:
        return 2 * Circulo.pi * self.__raio


if __name__ == '__main__':
    circulo1: Circulo = Circulo(5)
    print(f'{circulo1.raio = }')
    circulo1.raio = 6
    print(f'{circulo1.raio = }')
    print(f'{circulo1.area() = :.2f}')
    print(f'{circulo1.perimetro() = :.2f}')
