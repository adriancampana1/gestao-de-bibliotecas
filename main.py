from usuario import Usuario, ControleDeUsuarios

controle_usuarios = ControleDeUsuarios()

user1 = Usuario(id=1, nome="Adrian", sobrenome="Campana", sexo="M", cpf="1430241512")
user2 = Usuario(id=2, nome="Andriw", sobrenome="da Silva", sexo="M", cpf="151905810")

controle_usuarios.add_user(user1)
controle_usuarios.add_user(user2)

controle_usuarios.read_user(1)