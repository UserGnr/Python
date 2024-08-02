'''
1 - Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e setters para os atributos e um método para imprimir os dados de uma pessoa.
'''
from datetime import date


class Pessoa:

    def __init__(self, nome, data_nascimento, email) -> None:
        self.__nome: str = nome
        self.__data_nascimento: date = data_nascimento
        self.__email: str = email
    
    @property
    def nome(self) -> str:
        return self.__nome  + "AAA"
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome + "AAA"

    @property
    def data_nascimento(self) -> str:
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str) -> None:
        self.__data_nascimento: date = data_nascimento

    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email) -> None:
        self.__email = email
    
    def imprimir(self) -> None:
        print(f'Nome: {self.__nome}')
        print(f'Nascimento: {self.__data_nascimento.strftime('%d/%m/%y')}')
        print(f'Email: {self.__email}')


if __name__ == '__main__':
    ana: Pessoa = Pessoa('Ana', date(year=2024, month=1, day=1), 'ana@gmail.com')

    print(ana.__dict__)
    ana.imprimir()

    # Acessando os get
    print(ana.nome)
    print(ana.data_nascimento)
    print(ana.email)
    # Usando os set
    ana.nome = 'Aninha'
    ana.data_nascimento = '02/01/2024'
    ana.email = 'aninha@gmail.com'
    # Acessando os get
    print(ana.nome)
    print(ana.data_nascimento)
    print(ana.email)
