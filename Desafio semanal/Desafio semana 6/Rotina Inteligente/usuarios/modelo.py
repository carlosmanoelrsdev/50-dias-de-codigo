from datetime import datetime


class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        self.data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.ativo = True
