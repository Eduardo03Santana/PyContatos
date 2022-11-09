class Contato():
    def __init__(self, nome, numero, email, iD = 0):
        self.id = iD
        self.nome = nome
        self.numero = numero
        self.email = email
        if email == '': self.email = 'Nao Cadastrado'

    def __repr__(self):
        return f"""Id: {self.id}
Nome: {self.nome}
Numero: {self.numero}
Email: {self.email}"""
