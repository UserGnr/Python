# 8 - Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.

numero: int = 10

while numero >= 0:
    print(numero)
    numero -= 1

print('Fim')