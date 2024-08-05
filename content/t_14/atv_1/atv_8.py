'''
8 - Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a velocidade atual.
'''

class Carro:
    def __init__(self, marca: str, modelo: str, velocidade: float) -> None:
        self.marca: str = marca
        self.modelo: str = modelo
        self.velocidade: float = velocidade
    
    @property
    def marca(self) -> str:
        ''' Retorna a marca do veículo'''
        return self.__marca
    
    @property
    def modelo(self) -> str:
        ''' Retorna o modelo do veículo'''
        return self.__modelo
    
    @property
    def velocidade(self) -> float:
        ''' Retorna a velocidade do veículo'''
        return self.__velocidade
    
    @marca.setter
    def marca(self, marca: str) -> None:
        ''' Define a marca do veículo'''
        if not isinstance(marca, str):
            raise ValueError('O valor informado para a marca deve ser um texto (string)')
        self.__marca = marca

    @modelo.setter
    def modelo(self, modelo: str) -> None:
        ''' Define o modelo do veículo'''
        if not isinstance(modelo, str):
            raise ValueError('O valor informado para o modelo deve ser um texto (string)')
        self.__modelo = modelo

    @velocidade.setter
    def velocidade(self, velocidade: float) -> None:
        ''' Define a velocidade do veículo'''
        if not isinstance(velocidade, (float, int)):
            raise ValueError('O valor informado para a velocidade deve ser um número (float)')
        self.__velocidade = velocidade
    
    def acelerar(self, aumentar_velocidade: float = 1):
        """
        Acelerar o veículo

        Parâmetro(s):
        aumentar_velocidade: corresponde ao aumento da velocidade do veículo. Por padrão o valor é 1.
        """
        if aumentar_velocidade < 0:
            raise ValueError('A aceleração não pode ser menor que zero')
        self.__velocidade += aumentar_velocidade
        return print(f'O carro está acelerando em +{aumentar_velocidade}')
        
    def frear(self, reduzir_velocidade: float = __velocidade):
        """
        Frear o veículo

        Parâmetro(s):
        reduzir_velocidade: corresponde ao aumento da velocidade do veículo. Por padrão o valor é a velocidade atual do carro.
        """
        if reduzir_velocidade < 0:
            raise ValueError('A velocidade do carro não pode ser menor que zero')
        self.__velocidade -= reduzir_velocidade
        return print(f'O carro está freando em -{reduzir_velocidade}')


if __name__ == '__main__':
    carro1 = Carro('Fiat', 'Uno', 0)
    print(f'{carro1.marca = }')
    print(f'{carro1.modelo = }')
    print(f'{carro1.velocidade = }')

    carro1.marca = 'Volkswagen'
    carro1.modelo = 'Gol'
    # carro1.velocidade = '1' # Retorna erro
    carro1.velocidade = 1
    print(f'{carro1.marca = }')
    print(f'{carro1.modelo = }')
    print(f'{carro1.velocidade = }')


    carro1.acelerar()
    print(f'{carro1.velocidade = }')
    carro1.acelerar()
    print(f'{carro1.velocidade = }')
    # carro1.acelerar(-50)    # Retorna erro
    carro1.acelerar(50)    # Retorna erro
    print(f'{carro1.velocidade = }')
    carro1.acelerar()
    print(f'{carro1.velocidade = }')
    carro1.frear(5)
    print(f'{carro1.velocidade = }')
    carro1.frear()
    print(f'{carro1.velocidade = }')


