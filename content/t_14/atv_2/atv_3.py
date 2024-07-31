'''
3 - Crie um programa, instancie um objeto da classe Carro e teste o seu médodo.
'''

from atv_2 import Carro


if __name__ == '__main__':
    carro1 = Carro('Fiat','Uno', 5)
    carro1.imprimir()

    carro1.portas = 6
    carro1.imprimir()

    carro2 = Carro('Fiat','Argo', 5)
    carro2.imprimir()
    carro3 = Carro('Chery','Tiggo 7', 6)
    carro3.imprimir()
