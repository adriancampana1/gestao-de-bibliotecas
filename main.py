from autor import Autor
from biblioteca import Biblioteca
from editora import Editora
from emprestimo import Emprestimo
from funcionario import Funcionario
from livro import Livro
from usuario import Usuario
# Importando datetime para manipulação de datas
from datetime import datetime, timedelta
# 
# 
# 

bibliotecas = []
usuarios = []
funcionarios = []
autores = []
editoras = []
lote_de_livros = []
historico_emprestimos = []


# Instanciando bibliotecas
biblioteca1 = Biblioteca("Biblioteca Central", "Rua Principal, 123", "Uma biblioteca pública")
bibliotecas.append(biblioteca1)
biblioteca2 = Biblioteca("Biblioteca Municipal", "Avenida Central, 456", "Uma biblioteca da prefeitura")
bibliotecas.append(biblioteca2)
biblioteca3 = Biblioteca("Biblioteca Escolar", "Rua da Escola, 789", "Biblioteca da escola local")
bibliotecas.append(biblioteca3)

# Listando as bibliotecas
print("\n------ BIBLIOTECAS ------\n")
for biblioteca in bibliotecas:
    print("Nome:", biblioteca.nome)
    print("Endereço:", biblioteca.endereco)
    print("Descrição:", biblioteca.descricao)
    print()

# Instanciando usuários
usuario1 = Usuario("João", "Silva", "Brasileira", "Masculino", "123.456.789-00", "1234567", "1990-01-01")
usuarios.append(usuario1)
usuario2 = Usuario("Maria", "Santos", "Brasileira", "Feminino", "987.654.321-00", "7654321", "1995-05-15")
usuarios.append(usuario2)
usuario3 = Usuario("Carlos", "Ferreira", "Portuguesa", "Masculino", "111.222.333-44", "9876543", "1988-11-30")
usuarios.append(usuario3)

# Listando os usuários
print("\n------ USUÁRIOS ------\n")
for usuario in usuarios:
    print("Nome:", usuario.nome)
    print("Sobrenome:", usuario.sobrenome)
    print("Nacionalidade:", usuario.nacionalidade)
    print("Sexo:", usuario.sexo)
    print("CPF:", usuario.cpf)
    print("RG:", usuario.rg)
    print("Data de Nascimento:", usuario.data_nascimento)
    print()

# Instanciando funcionários
funcionario1 = Funcionario("João", "Silva", "Brasileira", "Masculino", "123.456.789-00", "1234567", "Programador", 5000, "123456", "1990-01-01", "2020-01-01")
funcionarios.append(funcionario1)
funcionario2 = Funcionario("Maria", "Santos", "Brasileira", "Feminino", "987.654.321-00", "7654321", "Analista de RH", 6000, "654321", "1995-05-15", "2019-05-15")
funcionarios.append(funcionario2)
funcionario3 = Funcionario("Carlos", "Ferreira", "Portuguesa", "Masculino", "111.222.333-44", "9876543", "Gerente de Projetos", 8000, "111222", "1988-11-30", "2018-11-30")
funcionarios.append(funcionario3)

# Listando os funcionários
print("\n------ FUNCIONÁRIOS ------\n")
for funcionario in funcionarios:
    print("Nome:", funcionario.nome)
    print("Sobrenome:", funcionario.sobrenome)
    print("Nacionalidade:", funcionario.nacionalidade)
    print("Sexo:", funcionario.sexo)
    print("CPF:", funcionario.cpf)
    print("RG:", funcionario.rg)
    print("Cargo:", funcionario.cargo)
    print("Salário:", funcionario.salario)
    print("CTPS:", funcionario.ctps)
    print("Data de Nascimento:", funcionario.data_nascimento)
    print("Data de Contratação:", funcionario.data_contratacao)
    print("Data de Dispensa:", funcionario.data_dispensa)
    print()

# Instanciando e adicionando os autores à lista
autor1 = Autor("João", "da Silva", "Brasileira")
autores.append(autor1)
autor2 = Autor("Maria", "dos Santos", "Brasileira")
autores.append(autor2)
autor3 = Autor("Carlos", "Ferreira", "Portuguesa")
autores.append(autor3)

# Listando os autores
print("\n------ AUTORES ------\n")
for autor in autores:
    print("Nome:", autor.nome)
    print("Sobrenome:", autor.sobrenome)
    print("Nacionalidade:", autor.nacionalidade)
    print()

# Instanciando editoras
editora1 = Editora("Editora A", "Editora A Fantasia", "1234567890", "123456", "Rua A, 123", "123456789", "Fulano de Tal")
editoras.append(editora1)
editora2 = Editora("Editora B", "Editora B Fantasia", "0987654321", "654321", "Rua B, 456", "987654321", "Beltrano de Tal")
editoras.append(editora2)
editora3 = Editora("Editora C", "Editora C Fantasia", "9876543210", "987654", "Rua C, 789", "987654321", "Ciclano de Tal")
editoras.append(editora3)

# Listando as editoras
print("\n------ EDITORAS ------\n")
for editora in editoras:
    print("Razão Social:", editora.razao_social)
    print("Nome Fantasia:", editora.nome_fantasia)
    print("CNPJ:", editora.cnpj)
    print("IE:", editora.ie)
    print("Endereço:", editora.endereco)
    print("Telefone:", editora.telefone)
    print("Responsável:", editora.responsavel)
    print()

# Instanciando livros
livro1 = Livro("Dom Quixote", 1605, 1, editora1, autor1, 10)
lote_de_livros.append(livro1)
livro2 = Livro("1984", 1949, 1, editora2, autor2, 15)
lote_de_livros.append(livro2)
livro3 = Livro("O Pequeno Príncipe", 1943, 1, editora3, autor3, 20)
lote_de_livros.append(livro3)

# Listando os livros
print("\n------ LIVROS ------\n")
for livro in lote_de_livros:
    print("Título:", livro.titulo)
    print("Ano:", livro.ano)
    print("Edição:", livro.edicao)
    print("Editora:", livro.editora.razao_social)
    print("Autor:", livro.autor.nome, livro.autor.sobrenome)
    print("Quantidade:", livro.quantidade)
    print()

# Adicionando os livros à lista de livros das bibliotecas
for biblioteca in bibliotecas:
    biblioteca.livros.extend(lote_de_livros)

# Listando as bibliotecas e os livros de cada uma
print("\n------ BIBLIOTECAS E SEUS LIVROS ------\n")
for biblioteca in bibliotecas:
    print("Biblioteca:", biblioteca.nome)
    print("Endereço:", biblioteca.endereco)
    print("Descrição:", biblioteca.descricao)
    print("Livros:")
    for livro in biblioteca.livros:
        print("- Título:", livro.titulo)
        print("  Ano:", livro.ano)
        print("  Edição:", livro.edicao)
        print("  Editora:", livro.editora.razao_social)
        print("  Autor:", livro.autor.nome, livro.autor.sobrenome)
        print("  Quantidade:", livro.quantidade)
        print()
    print()

# Função para calcular a data de retorno baseada na data de início e no prazo
def calcular_data_retorno(data_inicio, prazo):
    return data_inicio + timedelta(days=prazo)

# Data atual
data_atual = datetime.now()

# Instanciando empréstimos
emprestimo1 = Emprestimo(biblioteca1, funcionario1, usuario1, 1, [livro1, livro2], data_atual, 14, calcular_data_retorno(data_atual, 14), "Concluído", 0)
historico_emprestimos.append(emprestimo1)

emprestimo2 = Emprestimo(biblioteca2, funcionario2, usuario2, 2, [livro3], data_atual, 7, calcular_data_retorno(data_atual, 7), "Concluído", 0)
historico_emprestimos.append(emprestimo2)

# Listando o histórico de empréstimos
print("\n------ HISTÓRICO DE EMPRÉSTIMOS ------\n")
for emprestimo in historico_emprestimos:
    print("Número de Empréstimo:", emprestimo.num_emprestimo)
    print("Biblioteca:", emprestimo.biblioteca.nome)
    print("Funcionário:", emprestimo.funcionario.nome, emprestimo.funcionario.sobrenome)
    print("Usuário:", emprestimo.usuario.nome, emprestimo.usuario.sobrenome)
    print("Livros emprestados:")
    for livro in emprestimo.livros:
        print("- Título:", livro.titulo)
    print("Data de Início:", emprestimo.data_inicio.strftime("%d/%m/%Y"))
    print("Data de Retorno:", emprestimo.data_fim.strftime("%d/%m/%Y"))
    print("Status:", emprestimo.status)
    print("Multa Diária:", emprestimo.multa)
    print()