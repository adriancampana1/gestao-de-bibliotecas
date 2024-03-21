from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome, sobrenome, sexo, cpf, id):
        super().__init__(nome, sobrenome, sexo, cpf)
        self.id = id

class ControleDeUsuarios:
    def __init__(self) -> None:
        self.users = {}
    def add_user(self, user):
        if user.id in self.users:
            print(f"User with ID {user.id} already exists.")
        else:
            self.users[user.id] = user
            print(f"User {user.nome} added successfully.")

    def update_user(self, id, **kwargs):
        if id not in self.users:
            print(f"User with ID {id} not found.")
            return

        user = self.users[id]
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                print(f"Attribute {key} not found in User.")
        print(f"User {id} updated successfully.")

    def remove_user(self, id):
        if id in self.users:
            del self.users[id]
            print(f"User with ID {id} removed successfully.")
        else:
            print(f"User with ID {id} not found.")

    def read_user(self, id):
        if id in self.users:
            user = self.users[id]
            print(f"User ID: {user.id}, Name: {user.nome}, Surname: {user.sobrenome}, Gender: {user.sexo}, CPF: {user.cpf}")
        else:
            print(f"User with ID {id} not found.")    