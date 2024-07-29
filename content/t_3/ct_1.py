'''
Tipos numéricos (int)

int -> inteiro
'''

# Operações matemáticas
# Soma (+)
soma = 5 + 4
print(f"Soma: {soma}, tipo: {type(soma)}")

# Subtração (-)
subtracao = 5 - 4
print(f"Subtração: {subtracao}, tipo: {type(subtracao)}")

# Multiplicação (*)
multiplicacao = 5 * 4
print(f"Multiplicação: {multiplicacao}, tipo: {type(multiplicacao)}")

# Divisão (/)
divisao = 5 / 4 # Float
divisao_inteira = int(5 / 4)
divisao_inteira1 = 5 // 4

print(f"divisao: {divisao}, tipo: {type(divisao)}")
print(f"divisao_inteira: {divisao_inteira}, tipo: {type(divisao_inteira)}")
print(f"divisao_inteira1: {divisao_inteira1}, tipo: {type(divisao_inteira1)}")

# Exponenciação (**)
exponenciacao = 5 ** 4
print(f"Exponenciação: {exponenciacao}, tipo: {type(exponenciacao)}")

# Resto (%)
resto = 5 % 4
print(f"Resto: {resto}, tipo: {type(resto)}")

# Representação de números
milhao = 1000000
milhao1 = 1_000_000

print(f"milhao: {milhao}, tipo: {type(milhao)}")
print(f"milhao1: {milhao1}, tipo: {type(milhao1)}")

# Simplificação de operações com a mesma variável
num = 1
num += num  # num = num + 1
num -= num  # num = num - 1
num *= 2    # num = num * 2
num /=2 # num = num / 1
num //=2    # num = num // 1
num **=2    # num = num ** 1
