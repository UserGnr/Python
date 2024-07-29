'''
Generator Functions 

- Geradores (Generators) são Iterators (Iteradores), orém nem todo iterator é um generator

Outras informações:
- Generators podem ser criados com funções geradoras
- Funções geradoras utilizam a palavra reservada yield
- Generators podem ser criados com Expressões Geradoras

Diferenças entre Funções e Generator Functions (Funções Geradoras)

-----------------------------------------------------------------------------------
| Funções                                 | Generator Functions                   |
-----------------------------------------------------------------------------------
| utilizam return                         | utilizam yield                        |
-----------------------------------------------------------------------------------
| retorna uma vez                         | podem utilizar yield múltiplas vezes  |
-----------------------------------------------------------------------------------
| quando executada, retorna um valor      | quanto executada, retorna um generator|
-----------------------------------------------------------------------------------

- O yield é como o retorno de uma função, contudo ele não sai da função. O yield fica aguardando o próximo next
- Desse modo, o yield retorna e aguarda na linha onde está o yield

'''

# Exemplo de uma função geradora (generator function)
# Uma Generator Function não é um Generator. Ela gera um generator.


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
gen = conta_ate(5)

print(gen)
print(type(gen))

for num in gen:
    print(num)
