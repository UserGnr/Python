'''
4 - Implemente uma classe chamada “Aluno” que possua atributos para armazenar o nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado).
'''

class Aluno:

    n_media: float = 7.0

    def __init__(self, nome: str, matricula: str, *notas: float) -> None:
        self.__nome: str = nome
        self.__matricula: str = matricula
        self.__notas: tuple = notas
    

    @property
    def nome(self) -> str:
        return self.__nome
    

    @property
    def matricula(self) -> str:
        return self.__matricula
    

    @property
    def notas(self) -> str:
        return self.__notas
    
    def media(self) -> float:
        return sum(self.__notas) / (len(self.__notas))

    
    def situacao(self) -> str:
        if self.media() >= Aluno.n_media:
            return 'aprovado'
        return 'reprovado'

    
if __name__ == '__main__':
    aluno1 = Aluno('Aninha', '123', 6.9, 7, 7)
    print(aluno1.media())
    print(aluno1.situacao())