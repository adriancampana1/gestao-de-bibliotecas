from pessoa import Pessoa

class Autor(Pessoa):
    def __init__(self, nome, sobrenome, sexo=None):
        super().__init__(nome, sobrenome, sexo)