from dataclasses import dataclass

@dataclass()
class User:
    name: str
    email: str
    password: str

# Criação de um objeto User
user = User(name='John Doe', email='john@mail.com', password='123456')

# Imprimindo o objeto
print(user)
