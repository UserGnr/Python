'''
Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a idade e o histórico de consultas de um paciente. Implemente métodos para adicionar uma nova consulta ao histórico e exibir as consultas realizadas.
'''

from datetime import date, datetime

class Paciente:
    def __init__(self, nome: str, nascimento: date) -> None:
        self.nome: str = nome
        self.nascimento: date = nascimento
        self.__historico: list = []

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def nascimento(self) -> date:
        return self.__nascimento

    @nome.setter
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise ValueError('O nome precisa conter letras')
        if len(nome) == 0 or len(nome) > 50:
            raise ValueError('O nome tamanho de caracteres no nome deve ser maior que zero e menor que 51')
        self.__nome = nome

    @nascimento.setter
    def nascimento(self, nascimento: date) -> None:
        if not isinstance(nascimento, date):
            raise TypeError('O nascimento da pessoa deve corresponder ao formato date')
        if not (0 <= (datetime.now().year - nascimento.year) <= 120):
            raise ValueError('A idade deve estar entre 0 e 120 anos')
        
        self.__nascimento = nascimento

    def idade(self) -> int:
        hoje = datetime.now().date()
        
        idade = hoje.year - self.__nascimento.year
        if (self.__nascimento.month, self.__nascimento.day) > (hoje.month, hoje.day): idade -= 1
    
        return idade

    @property
    def historico(self) -> list:
        return self.__historico.copy()
    
    def nova_consulta(self, medico: str, especialidade: str, datahora_consulta: datetime) -> None:
        if not isinstance(medico, str) or not isinstance(especialidade, str):
            raise ValueError('Médico e especialidade devem ser strings')
        if len(medico) == 0 or len(medico) > 50 or len(especialidade) == 0 or len(especialidade) > 50:
            raise ValueError('Médico e especialidade devem ter no mínimo 1 caracter e no máximo 50')
        if not isinstance(datahora_consulta, datetime):
            raise ValueError('O formato do momento da consulta deve contemplar o formato aceito pelo datetime')
        
        agora = datetime.now()

        if datahora_consulta < agora:
            raise ValueError('O momento da consulta deve ser maior ou igual ao momento atual')

        for consulta in self.__historico:
            if consulta['data'] == datahora_consulta:
                raise ValueError('O paciente não pode ter mais de uma consulta no mesmo horário')

        self.__historico.append({'medico': medico, 'especialidade': especialidade, 'data': datahora_consulta})

if __name__ == '__main__':
    paciente1 = Paciente('Aninha',date(day= 1, month=9, year=2000))
    print(f'{paciente1.nome = }')
    print(f'{paciente1.nascimento = }')
    print(f'{paciente1.idade() = }')
    paciente1.nova_consulta('João','Clinico geral', datetime(2024,8,6,16,5,0))
    paciente1.nova_consulta('João','Clinico geral', datetime(2024,8,6,16,6,0))
    paciente1.nova_consulta('João','Clinico geral', datetime(2024,8,6,16,4,0))
    # paciente1.nova_consulta('João','Clinico geral', datetime(2024,8,6,16,4,0)) # Retorna erro pois o horário é o mesmo
    # paciente1.nova_consulta('João','Clinico geral', datetime(2024,8,5,16,4,0))   # Retorna erro pois o momento é menor que o momento atual
    print(f'{paciente1.historico = }')
