'''
1 - Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um método para imprimir os dados de um veículo. Crie também o construtor da classe.
'''

class Veiculo():


    def __init__(self, marca: str, modelo: str) -> None:
        self.__marca: str = marca
        self.__modelo: str = modelo
    

    @property
    def marca(self) -> str:
        return self.__marca
    

    @marca.setter
    def marca(self, marca: str) -> None:
        self.__marca = marca
    

    @property
    def modelo(self) -> str:
        return self.__modelo
    

    @modelo.setter
    def modelo(self, modelo: str) -> None:
        self.__modelo = modelo


    def imprimir(self) -> None:
        print(f'Marca: {self.__marca} Modelo: {self.__modelo}')


if __name__ == '__main__':
    
    carro1: Veiculo = Veiculo(marca= 'Fiat', modelo= 'Uno')
    carro2: Veiculo = Veiculo(marca= 'Fiat', modelo= 'Argo')
    carro3: Veiculo = Veiculo(marca= 'Chery', modelo= 'Tiggo 7')

    print(carro1.marca)
    print(carro1.modelo)

    carro1.marca = 'Volkswagen'
    carro1.modelo = 'Gol'

    print(carro1.marca)
    print(carro1.modelo)

    print(carro2.marca)
    print(carro2.modelo)

    print(carro3.marca)
    print(carro3.modelo)

    carro1.imprimir()
    carro2.imprimir()
    carro3.imprimir()
