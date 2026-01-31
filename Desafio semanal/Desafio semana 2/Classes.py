class Modelo_tarefas():
    def __init__(self, status_id, titulo, status="pendente"):
        self.status_id = status_id
        self.titulo = titulo
        self.status = status

class Gerenciador_taferas():

    def __init__(self):
        self.tarefas = {}
        self.proximo_id = 1


    def criar_tarefa(self, titulo, status="pendente"):
        nova_tarefa = Modelo_tarefas(self.proximo_id, titulo, status)
        self.tarefas[self.proximo_id] = nova_tarefa
        self.proximo_id += 1
        return nova_tarefa

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        for t in self.tarefas.values():
            print(f"ID: {t.status_id} | Título: {t.titulo} | Status: {t.status}")

    
    def atualizar_tarefas(self, status_id, novo_titulo=None, novo_status=None):
        tarefa = self.tarefas.get(status_id)
        if not tarefa:
            print(f"Tarefa com ID {status_id} não encontrada.")
            return
        if novo_titulo:
            tarefa.titulo = novo_titulo
        if novo_status:
            tarefa.status = novo_status
        print(f"Tarefa com ID {status_id} atualizada.")

    
    def remover_tarefa(self, status_id):
        if status_id in self.tarefas:
            del self.tarefas[status_id]
            print(f"Tarefa com ID {status_id} removida.")
        else:
            print(f"Tarefa com ID {status_id} não encontrada.")
            

    def buscar_tarefa_por_id(self, status_id):
        tarefa = self.tarefas.get(status_id)
        if tarefa:
            print(f"ID: {tarefa.status_id} | Título: {tarefa.titulo} | Status: {tarefa.status}")
        else:
            print(f"Tarefa com ID {status_id} não encontrada.")