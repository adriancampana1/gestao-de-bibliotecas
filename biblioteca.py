from livro import Livro

class Biblioteca:
    def __init__(self, nome, endereco, descricao=""):
        self.nome = nome
        self.endereco = endereco
        self.descricao = descricao
        self.livros = []