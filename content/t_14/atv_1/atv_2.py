'''
2 - Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.
'''

from atv_1 import Veiculo

class Carro(Veiculo):

    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        super().__init__(marca, modelo)
        self.__portas = portas


    @property
    def portas(self) -> int:
        return self.__portas


    @portas.setter
    def portas(self, portas: int) -> None:
        self.__portas = portas
    

    def imprimir(self) -> None:
        # super().imprimir()
        print(f'Marca: {super().marca} Modelo: {super().modelo} Portas: {self.__portas}')
    

if __name__ == '__main__':
    carro1: Carro = Carro('Fiat','Uno', 5)
    carro1.imprimir()

    carro1.portas = 6
    carro1.imprimir()

    carro2: Carro = Carro('Fiat','Argo', 5)
    carro2.imprimir()
    carro3: Carro = Carro('Chery','Tiggo 7', 6)
    carro3.imprimir()
