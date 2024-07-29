'''
Loop while

Forma geral

while expressão_booleana:
    //execução do loop

O boloco while será executado repetidamente até que uma expressão booleana seja verdadeira
Expressão booleana é toda expressão que o resultado é verdadeiro ou falso
É importande que seja tratado algum critério de parada para evitar um loop infinit
'''

# Exemplo 1
print('Exemplo 1')
numero = 1

while numero < 10:
    print(numero)
    numero += 1

# Exemplo 2
print('Exemplo 2')
resposta = ''

while resposta != 'sim':
    resposta = input("Encerrar loop? [sim] [qualquer outra cosia para continuar]: ")
