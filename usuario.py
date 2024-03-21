from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome, sobrenome, nacionalidade, sexo, cpf, rg, data_nascimento):
        super().__init__(nome, sobrenome, nacionalidade)
        self.sexo = sexo
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento