'''
Saindo de loops com break

O break é usado para sair de loops de forma planejada.
'''

# Exemplo 1
print('Exemplo 1')

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)

print('\nSaiu do loop\n\n')

# Exemplo 2
print('Exemplo 2')

while True:
    comando = input("Digite 'sair para sair do loop: ")
    if comando == 'sair':
        break
