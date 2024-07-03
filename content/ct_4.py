'''
Tipo de ponto flutuante (float) e complexo

Float: tipo real, decimal
Obs: o separador das casas decimais é o ponto(.) e não a vírgula(,)

'''

# Tipo de dado float
valor = 1.44
print(f"Valor: {valor}, tipo: {type(valor)}")

# Dupla atribuição
valor1, valor2 = 1, 44.1  # É  permitido
valor3 = 1, 44 # isso é uma tupla e não um tipo de dado float
print(f"Valor1: {valor1}, tipo: {type(valor1)}")
print(f"Valor2: {valor2}, tipo: {type(valor2)}")
print(f"Valor3: {valor3}, tipo: {type(valor3)}")

# Converter flaot para int
valor4 = 5.44
valor5 = int(valor4)
print(f"Valor 4: {valor4}, tipo: {type(valor4)}")
print(f"Valor 5: {valor5}, tipo: {type(valor5)}")
# Obs: perde a precisão ao converter float para int

'''
Número complexo

Basta atribuir o "j" no final do número
'''
valor6 = 5j
print(f"Valor 6: {valor6}, tipo: {type(valor6)}")

valor7 = valor5**2
print(f"Valor 7: {valor7}, tipo: {type(valor7)}")
