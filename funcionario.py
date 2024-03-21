from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, sexo, cargo, salario, ctps, rg, idade, data_contratacao, cpf=None):
        super().__init__(nome, sobrenome, sexo, cpf)
        self.cargo = cargo
        self.salario = salario
        self.ctps = ctps
        self.rg = rg
        self.idade = idade
        self.data_contratacao = data_contratacao
