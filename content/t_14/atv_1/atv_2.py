'''
2 - Implemente uma classe chamada “ContaBancária” que possua atributos para armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar depósitos e saques.
'''

class ContaBancaria:
    
    def __init__(self, numero_conta: str, nome_titular: str, saldo: float) -> None:
        self.__numero_conta: str = numero_conta
        self.__nome_titular: str = nome_titular
        self.__saldo: float = saldo
    
    @property
    def numero_conta(self) -> str:
        return self.__numero_conta
    
    @property
    def nome_titular(self) -> str:
        return self.__nome_titular
    
    @property
    def saldo(self) -> float:
        return self.__saldo

    def __validar_retirada(self, valor: float) -> bool:
        if valor <= self.saldo:
            return True
        return False

    def sacar(self, valor: float) -> str:
        if self.__validar_retirada(valor):
            self.__saldo -= valor
            return 'Valor sacado'
        return 'Sem saldo suficiente para realziar o saque'
    
    def depositar(self, valor: float) -> str:
        if valor > 0:
            self.__saldo += valor
            return 'Valor depositado'
        return 'O valor precisa ser maior que zero'


if __name__ == '__main__':
    usuario1: ContaBancaria = ContaBancaria('123', 'Aninha Fulana', 5)
    print(f'{usuario1.numero_conta = }')
    print(f'{usuario1.nome_titular = }')
    print(f'{usuario1.saldo = :.2f}')

    print(f'{usuario1.sacar(6)}')
    print(f'{usuario1.sacar(5)}')
    print(f'{usuario1.saldo = :.2f}')
    print(f'{usuario1.sacar(5)}')
    usuario1.depositar(11.50)
    print(f'{usuario1.saldo = :.2f}')
    usuario1.depositar(0)


