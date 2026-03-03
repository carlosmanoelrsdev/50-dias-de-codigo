from agendamento.modelo import Agendamento


class ServicoAgendamento:
    def __init__(self):
        self.agendamentos = {}
        self.proximo_id = 1

    def criar_agendamento(self, titulo, data_hora, tarefa_id=None, recorrente=False):
        id = self.proximo_id
        self.proximo_id += 1
        agendamento = Agendamento(id, titulo, data_hora, tarefa_id, recorrente)
        self.agendamentos[id] = agendamento
        return agendamento

    def listar_agendamentos(self):
        return list(self.agendamentos.values())

    def cancelar_agendamento(self, id):
        agendamento = self.agendamentos.get(id)
        if agendamento:
            agendamento.ativo = False
            return True
        return False

    def buscar_por_id(self, id):
        return self.agendamentos.get(id)
