'''
Tipos de operadores: aritméticos, atribuição, comparação, lógicos, identidade, associação
'''

'''
Operadores aritméticos
+   Adição ou sinal positivo
-   Subtração ou sinal negativo
*   Multiplicação
/   Divisão
//  Divisão inteira
%   Módulo
**  Exponenciação
'''

# Fazer testes nos valores e nos operadores abaixo
print("Operadores aritméticos")

numero_1 = 3
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(f'Soma: {soma}') # 5
print(f'Subtração: {subtracao}') # 1
print(f'Mulotiplicação: {multiplicacao}')  # 6
print(f'Divisão: {divisao}') # 1.5
print(f'Divisão inteira: {divisao_inteira}') # 1
print(f'Módulo: {modulo}')  # 1
print(f'Exponenciação: {exponenciacao}') # 9
print('\n')

'''
Operadores de atribuição

Operador	Exemplo	    Equivalente a
=	        x = 1	    x = 1
+=	        x += 1	    x = x + 1
-=	        x -= 1	    x = x - 1
*=	        x *= 1	    x = x * 1
/=	        x /= 1	    x = x / 1
%=	        x %= 1	    x = x % 1
'''

# Fazer testes nos valores e nos operadores abaixo
print("Operadores de atribuição")

num = 1
num += num  # num = num + 1
# num -= num  # num = num - 1
# num *= 2    # num = num * 2
# num /=2 # num = num / 1
# num //=2    # num = num // 1
# num **=2    # num = num ** 1

print(num)
print('\n')

'''
Operadores de comparação
==  Igual
>   Maior que
<   Menor que
>=  Maior ou igual que
<=  Menor ou igual que
!=  Diferente de
'''

# Fazer testes nos valores e nos operadores abaixo
print("Operadores de comparação")

numero_1 = 1
numero_2 = 2

if numero_1 < numero_2:
    print("Verdadeiro")
else:
    print("Falso")

print('\n')

'''
Operadores lógicos
and     Retorna verdadeiro se todas as condições devem ser verdadeiras
or      Retorna verdadeiro se pelo menos uma das condições seja verdadeira
not     Inverte o resultado
'''

# Fazer testes nos valores e nos operadores abaixo
print("Operadores lógicos")

numero_1 = 1
numero_2 = 2
numero_3 = 2

if numero_1 >= numero_2 or numero_2 >= numero_3:
    print('Verdadeiro')
else:
    print('Falso')

print('\n')

'''
Operadores de identidade

Servem para comparar objetos

is          Retorna True se forem o mesmo objeto
is not      Retorna True se não forem o mesmo objeto
'''

# Fazer testes nos valores e nos operadores abaixo
print("Operadores de identidade")

cor_1 = "Amarelo"
cor_2 = "Amarelo"
cor_3 = "Azul"

if cor_1 is cor_2:
    print("Verdadeiro")
else:
    print("Falso")

if cor_2 is not cor_3:
    print("Verdadeiro")
else:
    print("Falso")

print('\n')

'''
Operadores de associação

Verificar se contém um objeto

in          Retorna True caso seja encontrado
not in      Retorna True caso não seja encontrado
'''

# Fazer testes nos valores e nos operadores abaixo
print("Operadores de associação")

texto1 = "Abacaxi"
texto2 = "xi"

print(texto2 in texto1)
print(texto2 not in texto1)
