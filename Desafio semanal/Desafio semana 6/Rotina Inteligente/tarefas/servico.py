from .modelo import Tarefa
from .repositorio import RepositorioTarefas


class ServicoTarefas:
    """Serviço responsável pela lógica de negócio de tarefas."""

    def __init__(self):
        self._repositorio = RepositorioTarefas()

    def criar(self, titulo, descricao="", usuario_id=None):
        tarefa = Tarefa(titulo=titulo, descricao=descricao, usuario_id=usuario_id)
        return self._repositorio.salvar(tarefa)

    def listar(self):
        return self._repositorio.listar_todos()

    def listar_por_usuario(self, usuario_id):
        return self._repositorio.listar_por_usuario(usuario_id)

    def atualizar_status(self, tarefa_id, novo_status):
        tarefa = self._repositorio.buscar_por_id(tarefa_id)
        if not tarefa:
            raise ValueError(f"Tarefa com id {tarefa_id} não encontrada.")
        tarefa.status = novo_status
        return self._repositorio.atualizar(tarefa)

    def remover(self, tarefa_id):
        return self._repositorio.remover(tarefa_id)
