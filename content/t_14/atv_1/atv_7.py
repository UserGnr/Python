'''
7 - Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua área.
'''

# Em construção
class Triangulo:
    def __init__(self, *lado: float) -> None:
        self.lados: tuple = lado
        print(sorted(self.lados)[:2])
        print(sorted(self.lados)[-1])

    def _triangulo_valido(self, lados: tuple) -> bool:
        print(sorted(self.lados)[:2])
        print(sorted(self.lados)[-1])


if __name__ == '__main__':
    triangulo1 = Triangulo(9, 5, 3)
