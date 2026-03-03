class RepositorioTarefas:
    def __init__(self):
        self.tarefas = {}
        self.proximo_id = 1

    def salvar(self, tarefa):
        self.tarefas[tarefa.id] = tarefa
        return tarefa

    def buscar_por_id(self, id):
        return self.tarefas.get(id)

    def listar_todas(self):
        return list(self.tarefas.values())

    def remover(self, id):
        if id in self.tarefas:
            del self.tarefas[id]
            return True
        return False

    def proximo_id_disponivel(self):
        id_atual = self.proximo_id
        self.proximo_id += 1
        return id_atual
