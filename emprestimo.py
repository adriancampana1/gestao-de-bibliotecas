class Emprestimo:
    def __init__(self, biblioteca, funcionario, usuario, livro, data_inicio, data_fim, status, multa):
        self.biblioteca = biblioteca
        self.funcionario = funcionario
        self.usuario = usuario
        self.livro = livro
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status
        self.multa = multa