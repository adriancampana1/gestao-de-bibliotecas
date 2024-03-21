from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, nacionalidade, sexo, cpf, rg, cargo, salario, ctps, data_nascimento, data_contratacao, data_dispensa=None):
        super().__init__(nome, sobrenome, nacionalidade)
        self.sexo = sexo
        self.cpf = cpf
        self.rg = rg
        self.cargo = cargo
        self.salario = salario
        self.ctps = ctps
        self.data_nascimento = data_nascimento
        self.data_contratacao = data_contratacao
        self.data_dispensa = data_dispensa