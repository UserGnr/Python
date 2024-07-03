'''
Usando o input

input()
input(prompt)

Permite a entrada de dados pelo usuário.
Se o argumento prompt estiver presente, escreve na saída padrão sem uma nova linha ao final.
A função então lê uma linha da fonte de entrada, converte a mesma para uma string (removendo o caractere de nova linha ao final), e a devolve.

'''

# Forma 1
print("Qual o seu nome?")
nome = input()

# Forma 2
sobrenome = input('Qual o seu sobrenome? ')

# As entradas do input sempre são do tipo str
idade1 = input("Qual a sua idade? ")
# Converter uma entrada para o tipo inteiro
idade2 = int(input("Qual a sua idade novamente? "))
# Verificando os tipos de dados obtidos
print(f"A primeira idade fornecida é do tipo {type(idade1)} e a segunda {type(idade2)}")
