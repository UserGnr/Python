'''
Funções com parâmetro (de entrada)

- Os parâmetros são entradas que serão usadas pela função
- As funções podem ter quantos parâmetros de entrada forem necessários
- Os parâmetros são separados por vírgula
- A ordem dos parâmetros importa, a menos que sejam declarados os nomes dos parâmetros diretamente nos argumentos

A diferença entre Parâmetros e Argumentos
- Parâmetros são variáveis declaradas na definição de uma função;
- Argumentos são dados passados durante a execução de uma função;

Keyword Arguments: Argumentos nomeados
'''

# Exemplo 1
# Usando um parâmetro de entrada
print('Exemplo 1 - Usando um parâmetro de entrada')


def quadrado(numero):
    return numero ** 2


print(f'Quadrado de 2: {quadrado(2)}')
print(f'Quadrado de 3: {quadrado(3)}')
print(f'Quadrado de 4: {quadrado(4)}')
print(f'Quadrado de 5: {quadrado(5)}')
# print(f'Quadrado de 5: {quadrado()}')   # Retorna erro, pois, a entrada número não foi especificada como opcional

print('\n\n')

# Exemplo 2
# Usando 2 parâmetros de entrada
print('Exemplo 2 - Usando 2 parâmetros de entrada')


def multiplicar(num1, num2):
    return num1 * num2


print(f'Multiplicando 1 * 2: {multiplicar(1, 2)}')
print(f'Multiplicando 2 * 3: {multiplicar(2, 3)}')
print(f'Multiplicando 4 * 4: {multiplicar(4, 4)}')
print(f'Multiplicando 6 * 5: {multiplicar(6, 5)}')
# print(f'Multiplicando 6 * 5 * 7: {multiplicar(6, 5, 7)}')   # Retorna erro pois a função não comporta 3 argumento
# print(f'Multiplicando 6: {multiplicar(6)}')   # Retorna erro pois a função não comporta apenas 1 argumento

print('\n\n')

# Exemplo 3
# Usar nome dos parâmetros nos argumentos
print('Exemplo 3 - Usando 2 parâmetros de entrada')


def nome_completo (nome, sobrenome):
    return print(f'Nome completo: {nome} {sobrenome}')


nome_completo('Felicity', 'da Silva')
nome_completo('da Silva', 'Felicity')
nome_completo(sobrenome='da Silva', nome='Felicity')
