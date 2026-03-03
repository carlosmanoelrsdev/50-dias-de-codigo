from tarefas.modelo import Tarefa
from tarefas.repositorio import RepositorioTarefas


class ServicoTarefas:
    def __init__(self):
        self.repositorio = RepositorioTarefas()

    def criar_tarefa(self, titulo, descricao="", prioridade="normal"):
        id = self.repositorio.proximo_id_disponivel()
        tarefa = Tarefa(id, titulo, descricao, prioridade)
        return self.repositorio.salvar(tarefa)

    def listar_tarefas(self):
        return self.repositorio.listar_todas()

    def atualizar_tarefa(self, id, titulo=None, descricao=None, prioridade=None, status=None):
        tarefa = self.repositorio.buscar_por_id(id)
        if not tarefa:
            return None
        if titulo:
            tarefa.titulo = titulo
        if descricao is not None:
            tarefa.descricao = descricao
        if prioridade:
            tarefa.prioridade = prioridade
        if status:
            tarefa.status = status
        return tarefa

    def remover_tarefa(self, id):
        return self.repositorio.remover(id)

    def buscar_por_id(self, id):
        return self.repositorio.buscar_por_id(id)
