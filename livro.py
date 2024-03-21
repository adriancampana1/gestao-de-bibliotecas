from editora import Editora
from autor import Autor

class Livro:
    def __init__(self, titulo, ano, edicao, editora, autor, unidades):
        self.titulo = titulo
        self.ano = ano
        self.edicao = edicao
        self.editora = editora
        self.autor = autor
        self.unidades = unidades