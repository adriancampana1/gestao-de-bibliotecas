from pessoa import Pessoa

class Autor(Pessoa):
    def __init__(self, nome, sobrenome, nacionalidade):
        super().__init__(nome, sobrenome, nacionalidade)