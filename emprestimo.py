class Emprestimo:
    def __init__(self, biblioteca, funcionario, usuario, num_emprestimo, livros, data_inicio, prazo, data_fim, status, multa_diaria):
        self.biblioteca = biblioteca
        self.funcionario = funcionario
        self.usuario = usuario
        self.num_emprestimo = num_emprestimo
        self.livros = livros
        self.data_inicio = data_inicio
        self.prazo = prazo
        self.data_fim = data_fim
        self.status = status
        self.multa = multa_diaria