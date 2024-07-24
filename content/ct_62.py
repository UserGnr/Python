"""
Programação Orientada a Objetos - POO

- POO é um paradigma de programação que utiliza que mapeamento de objetos do mundo real para modelos computacionais
- Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas

Principais elementos da Orientação a Objetos
- Classe: modelo do objeto do mundo real sendo representado computacionalmente
- Atributo: características do objeto. Ou seja, pelos atributos é possível representar computacionalmente os estados de um objeto
    Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos
- Método: comportamento do objeto (funções)
- Construtor: método especial utilizado para criar os objetos
- Objeto: instância da classe


Classes
- Para definir uma classe utilizamos a palavra reservada class
- Utiizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado
- Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em maiúsculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo
- Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidade
"""

# Exemplo de uma classe

class Acesso:   # Classe

    contador = 0    # Atributo de classe | Estático
    valor = 1.55    # Atributo de classe | Estático

    def __init__(self, nome_completo, email, senha):    # Método especial __init__
        self.nome_completo = nome_completo  # Atributo de instancia | Definido como público
        self.email = email  # Atributo de instancia |  Definido como público
        self.__senha = senha    # Atributo de instancia |  Definido como privado
        self.id = Acesso.contador   # Atributo de instancia
        Acesso.contador = self.id   # Atributo de classe


    def mostra_nome_completo(self):  # Método
        print(self.nome_completo)

    def mostra_email(self):  # Método
        print(self.email)

    def mostra_senha(self): # Método
        print(self.__senha)


maria = Acesso('Maria Fulana', 'mariafulana@email.com', 'Senha123')

print('\n')
# Acessando os atributos de isntância:
# Forma incorreta:
print('Forma incorreta de acessar os atributos de instância')
print(maria.nome_completo)
print(maria.email)
print(maria._Acesso__senha)

print('\n')
# Forma correta:
print('Forma correta de acessar os atributos de instância')
maria.mostra_nome_completo()
maria.mostra_email()
maria.mostra_senha()

print('\n')
# Forma correta ao acessar um atributo de classe:
print('Forma correta de acessar os atributos de classe')
Acesso.valor
print(Acesso.valor)

print('\n')
print('Exibindo os tipos de dados:')
print(type(maria))
print(type(Acesso))

print('\n')
print('Exibindo como um dicionário')
print(maria.__dict__)
print(Acesso.__dict__)
