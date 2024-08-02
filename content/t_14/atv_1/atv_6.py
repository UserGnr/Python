'''
6 - Implemente uma classe chamada “Produto” que possua atributos para armazenar o nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor total em estoque e verificar se o produto está disponível.
'''

class Produto:
    def __init__(self, nome: str, preco: float, quantidade: float) -> None:
        self.nome: str = nome   # Desse modo irá acessar o setter e fazer a validação 
        self.preco: float = preco
        self.quantidade: float = quantidade

    @property
    def nome(self) -> str:
        """ Retorna o nome do produto """
        return self.__nome

    @property
    def preco(self) -> float:
        """ Retorna o preço do produto """
        return self.__preco

    @property
    def quantidade(self) -> float:
        """ Retorna a quantidade do produto """
        return self.__quantidade

    @nome.setter
    def nome(self, nome: str) -> None:
        """
        Define o nome do produto em estoque.

        :param nome: Nome do produto. Deve ter algum texto informado.
        """
        if len(nome) == 0:
            raise ValueError('O nome precisa ter algum texto')
        self.__nome = nome

    @preco.setter
    def preco(self, preco: float) -> None:
        """
        Define o preço do produto em estoque.

        :param preco: Preço do produto. Deve ser maior ou igual a zero.
        """
        if preco < 0:
            raise ValueError('O preço não pode ser menor que zero')
        self.__preco = preco

    @quantidade.setter  # Pelo que o enunciado pede, a própria quantidade é o estoque
    def quantidade(self, quantidade: float) -> None:
        """
        Define a quantidade do produto em estoque.

        :param quantidade: Quantidade do produto. Deve ser maior ou igual a zero.
        """
        if quantidade < 0: 
            raise ValueError('A quantidade não pode ser menor que zero')
        self.__quantidade = quantidade

    def disponibilidade(self) -> str:
        """ Retorna a disponibilidade do produto no estoque """
        return 'disponível' if self.__quantidade != 0 else 'indisponível'


if __name__ == '__main__':
    # produto1 = Produto('Prego', -1, 5000) # Retorna erro
    produto1 = Produto('Prego', 0.5, 5000)
    print(f'{produto1.nome = }')
    print(f'{produto1.preco = }')
    # produto1.preco = -1   # Retorna erro
    print(f'{produto1.preco = }')
    print(f'{produto1.quantidade = }')
    print(f'{produto1.disponibilidade() = }')
    produto1.quantidade = 0
    print(f'{produto1.disponibilidade() = }')
