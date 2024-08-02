'''
5 - Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, considerando descontos de impostos e benefícios.
'''

class Encargos:
    def __init__(self, beneficios: float, impostos: float) -> None:
        """
        Benefícios: valor de benefícios comom vale alimentação, bonificações e demais. Unidade: reais
        Impostos: valor em porcentagem associado aos descontos. Unidade: porcentagem
        """
        self.__beneficios = beneficios
        self.__impostos = impostos


    @property
    def beneficios(self) -> float:
        return self.__beneficios
    

    @property
    def impostos(self) -> float:
        return self.__impostos
    
    @beneficios.setter
    def beneficios(self, valor: float) -> None:
        self.__beneficios = valor


    @impostos.setter
    def impostos(self, valor: float) -> None:
        self.__impostos = valor


class Funcionario:
    def __init__(self, nome: str, salario: float, cargo: str, encargos: Encargos) -> None:
        self.__nome: str = nome
        self.__salario: float = salario
        self.__cargo: str = cargo
        self.__encargos: Encargos = encargos

    @property
    def nome(self) -> str:
        return self.__nome
    

    @property
    def salario(self) -> float:
        return self.__salario


    @property
    def cargo(self) -> str:
        return self.__cargo


    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome
    

    @salario.setter
    def salario(self, salario: float) -> None:
        self.__salario = salario
    

    @cargo.setter
    def cargo(self, cargo: str) -> None:
        self.__cargo = cargo


    def salario_liquido(self) -> float:
        return self.__salario * (1 - self.__encargos.impostos / 100) + self.__encargos.beneficios   # Nesse caso, os benefícios não estão inclusos nos descontos

if __name__ == '__main__':
    encargos1 = Encargos(500, 50)
    funcionario1 = Funcionario('Aninha', 1000, 'Analista', encargos1)

    print(f'{funcionario1.nome = }')
    print(f'{funcionario1.salario = }')
    print(f'{funcionario1.cargo = }')
    print(f'{funcionario1.salario_liquido() = }')
