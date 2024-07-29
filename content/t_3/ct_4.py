'''
String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos: 
Aspas simples: 'uma string', '1234', 'a', 'True', '42.3'
Aspas duplas: "uma string", "1234", "a", "True", "42.3"
.
.
.
Observação:
- O mais comum é aspas simples
- Se abrir com um tipo de aspas específico, é necessário fechar
- O \ Funciona com ocaractere de escape, vide exemplo abaixo
'''

# Exemplos 1
print("Exemplos 1", end='\n\n')

nome = 'Um nome qualquer'
print(f'Nome: {nome} | tipo: {type(nome)}', end='\n\n')

nome = "Tom's Bar"
print(f'Nome: {nome} | tipo: {type(nome)}', end='\n\n')

nome = """Alfredo
Holm"""
print(f'Nome: {nome} | tipo: {type(nome)}', end='\n\n')

nome = '''Tonia
Balin'''
print(f'Nome: {nome} | tipo: {type(nome)}', end='\n\n')

# Usando o caractere de escape
print('Usando aspas simples com caractere de escape: \' ', end='\n\n\n\n')

# ----------------------------------------------------
# Exemplos 2
print("Exemplos 2", end='\n\n')

nome = 'Um noMe qualQUER'
print(nome.upper(), end='\n\n')     # Maiúsculo

nome = 'Um noMe qualQUER'
print(nome.lower(), end='\n\n')     # Minúsculo

nome = 'Um noMe qualQUER'
print(nome.title(), end='\n\n\n\n')     # Primeira letra de cada palavra em maiúscula

# ----------------------------------------------------
# Exemplos 3
print('Exemplos 3')
print('Percorrendo uma string', end='\n\n')
'''
# Posições
  0 ,  1 ,  2 ,  3 ,  4 -> Crescente
['L', 'I', 'S', 'T', 'A'] 
 -5 , -4 , -3 , -2 , -1 -> Decrescente

 É necessário prestar atenção ao operar, vide os exemplos abaixo com atenção
'''

nome = 'um nome qualquer'
print(f'Da posição 0 até a 3: {nome[0:4]}')    # Inicia na posição 0 e vai até a posição 3
print(nome[3:7])    # Vai da posição 3 até a 6
print(nome[-1:-5:-1])    # Vai da posição -1 até a -4
print(nome[-1:9:-1])    # Vai da posição -1 até a 10
print(nome[::1])   # Pecorrer do primeiro até o último com o intervalo de um em um
print(nome[::-1])   # Pecorrer de trás para frente
print(nome[::2], end='\n\n\n\n')   # Pecorrer do primeiro até o último com o intervalo de dois em dois

# ----------------------------------------------------
# Exemplos 4
print('Exemplos 4')
print('Usando o split', end='\n\n')

nome = 'um nome qualquer'
print(nome.split())     # Transforma uma string em uma lista com strings
print(type(nome.split()), end='\n\n')

print(nome.split()[0])  # Imprime a posição 0 da lista
print(nome.split()[1])  # Imprime a posição 1 da lista
print(nome.split()[2], end='\n\n')  # Imprime a posição 2 da lista

# É necessário prestar atenção ao operar, vide os exemplos abaixo com atenção
print(nome.split())     # Imprime a lsita completa
print(nome.split()[::1])    # Indo do primeiro elemento até o último
print(nome.split()[::-1])   # Indo do último elemento até o primeiro
print(nome.split()[1:2])   # Indo do elemento 1
print(nome.split()[-1:-2:-1])   # Indo do elemento -1
print(nome.split()[0:3])   # Indo do elemento 0 ao 2
print(nome.split()[1:3])   # Indo do elemento 1 ao 2
print(nome.split()[-1:-3:-1], end='\n\n\n\n')   # Indo do elemento -1 ao -2

# ----------------------------------------------------
# Exemplos 5
print('Exemplos 5')
print('Usando o replace', end='\n\n')

nome = 'um nome qualquer'

print(nome.replace('e','z'), end='\n\n\n\n')

# ----------------------------------------------------
# Exemplos 6
print('Exemplos 6')
print('Palíndromo', end='\n\n')

texto = 'Lava esse aval'
print(texto)
print(texto[::-1])

texto = 'subi no ônibus'
print(texto)
print(texto[::-1])
