from datetime import datetime


class Tarefa:
    def __init__(self, id, titulo, descricao="", prioridade="normal", status="pendente"):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
