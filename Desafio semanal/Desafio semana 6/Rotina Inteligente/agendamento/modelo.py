from datetime import datetime


class Agendamento:
    def __init__(self, id, titulo, data_hora, tarefa_id=None, recorrente=False):
        self.id = id
        self.titulo = titulo
        self.data_hora = data_hora
        self.tarefa_id = tarefa_id
        self.recorrente = recorrente
        self.ativo = True
        self.data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
