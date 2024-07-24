'''
POO - Atributos de classes

Atributos: representam as características do objeto. Ou seja, pelos atributos é possível representar computacionalmente os estados de um objeto

Atributos públicos e privados:
- Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público, ou seja, pode ser acessado em todo o projeto 
- Usa-se Name Mangling (__ duplo underscore no início do nome do atributo) para demostrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado somente dentro da própria classe onde está declarado
- Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedrir que façamos acesso aos atributos sinalizados como privados fora da classe com ou sem o uso do duplo underscore


Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

Atributos de instância:
Ao criar instâncias/objetos de uma classe, todas as instâncias terão estes atributos

Atributos de Classe:
São atributos que são declarados diretamente na classe, ou seja, fora do contrutor. Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias terão o mesmo valor para este atributo

Atributos Dinâmicos
São atributos de instância que podem ser criados em tempo de execução
O atributo dinâmico será exclusivo da instância que o criou
'''

# Exemplo 1
# Atributos públicos e privados
print('Exemplo 1 - Atributos públicos e privados')


class Acesso1:

    def __init__(self, nome_completo, email, senha):
        self.nome_completo = nome_completo  # Definido como público
        self.email = email  # Definido como público
        self.__senha = senha    # Definido como privado


user1_ex1 = Acesso1('Maria Fulana', 'mariafulana@email.com', 'Senha123')
print(user1_ex1.__dict__)

print(user1_ex1.nome_completo)
print(user1_ex1.email)
# print(user1_ex1.senha)    # Retorna erro
print(user1_ex1._Acesso1__senha)    # Para retornar um atributo definido como privado é necessário usar essa sintaxe
# Vale salientar que o mesmo sendo privado, é possível acessar o valor do atributo

print('\n\n')

# Exemplo 2
# Atributos de instância
# Todas as instâncias terão os atributos
print('Exemplo 2 - Atributos de instância')


class Acesso2:

    def __init__(self, nome_completo, email, senha):
        self.nome_completo = nome_completo
        self.email = email
        self.__senha = senha
    
    def mostra_nome_completo(self):
        print(self.nome_completo)

    def mostra_email(self):
        print(self.email)

    def mostra_senha(self):
        print(self.__senha)


user1_ex2 = Acesso2('Maria Fulano1', 'mariafulano@gmail.com', 'Senha123')
user2_ex2 = Acesso2('João Fulano1', 'joaofulano@gmail.com', 'Senha456')

user1_ex2.mostra_email()
user2_ex2.mostra_email()

print('\n\n')

# Exemplo 3
# Atributos de classe
# São declarados diretamente na classe
print('Exemplo 3 - Atributos de classe')


class Produto:

    contador = 0    # Atributos de classe estático
    imposto = 0.05  # Atributos de classe estático

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor + valor * Produto.imposto
        Produto.contador = self.id
    

p1_ex3 = Produto('Banana', 'Fruta', 5)
p2_ex3 = Produto('Maça', 'Fruta', 3.99)

print(p1_ex3.nome + ':')
print(p1_ex3.id)
print(p1_ex3.valor)

print(p2_ex3.nome + ':')
print(p2_ex3.id)
print(p2_ex3.valor)

print(Produto.imposto) # Acesso correto de um atributo de classe

print('\n\n')

# Exemplo 4
# Atributos dinâmicos
print('Exemplo 4 - Atributos dinâmicos')

class Produto2:

    contador = 0
    imposto = 0.05

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor + valor * Produto.imposto
        Produto.contador = self.id

p1_ex4 = Produto('Banana', 'Fruta', 5)
p2_ex4 = Produto('Maça', 'Fruta', 3.99)

print(p1_ex4.__dict__)
print(p2_ex4.__dict__)

p1_ex4.peso = '5kg' # Criando um atributo em tempo de execução
# Note que na classe Produto2 não existe o atributo peso

print(p1_ex4.__dict__)
print(p2_ex4.__dict__)

del p1_ex4.peso # Deletando o atributo

print(p1_ex4.__dict__)
print(p2_ex4.__dict__)