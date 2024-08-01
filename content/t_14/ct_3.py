'''
POO - Métodos

Métodos (funções)
Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema
Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline

Em Python, dividimos os métodos, em 2 grupos: 
    Métodos de instância
    Métodos de Classe

    
Métodos de Instância
Usa as instâncias do objeto para ter acesso
O método dunder init __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe
Obs.: 
- Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)
- Os métodos/funções dunder em Python são chamados de métodos mágicos
- Mesmo que qualquer desenvolvedor possa criar as próprias funções utilizando dunder (underline no início e no fim) não é aconselhado, pois em Python possui vários métodos que fazem uso do dunder e pode aconcer que seja feito alguma mudança no comportamento das funções mágicas internas da linguagem

Métodos de Classe
Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras linguagens
São usados quando não faz uso dos atributos de instâncias, faz uso dos atributos de classes
'''

# Método de instância
# Trabalha com os valores da instância

# Método de classe
# @classmethod
# O método de classe é usado quando o método usa os atributos de classes
# Não tem acesso a instância do objeto, tem acesso a classe

# Métodos estáticos
# @staticmethod
# Não tem acesso a classe e também não tem acesso a instância

# Métodos privados
# São executados apenas dentro da classe
# Inicia o com duplo underline
# É possível acessa-lá, porém é privada e deve ser₹usada apenas dentro da classe

print('Exemplo')

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod    # Método de classe
    def conta_usuarios(cls):    # O cls é uma convenção que representa a própria classe
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod   # Método estático
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):    # Método de instância
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):   # Método de instância
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):   # Método privado
        return self.__email.split('@')[0]


user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
user2 = Usuario('Felicity2', 'Jones2', 'felicity2@gmail.com', '1234562')

print(' ------ ')
# Acesso correto aos métodos de instância:
print(Usuario.nome_completo(user1))
print(user1.nome_completo())


# Forma correta de acessar um método de classe
Usuario.conta_usuarios()
# Forma incorreta de acessar um método de classe
# user2.conta_usuarios()

# Método Estático
print(Usuario.contador)
print(Usuario.definicao())
user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
print(user.contador)
print(user.definicao())
