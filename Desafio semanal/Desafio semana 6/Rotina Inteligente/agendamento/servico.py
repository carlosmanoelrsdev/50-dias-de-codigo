import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from persistencia.repositorio_base import RepositorioBase
from .modelo import Agendamento


class ServicoAgendamento:
    """Serviço responsável pelo gerenciamento de agendamentos."""

    def __init__(self):
        self._repositorio = RepositorioBase()

    def agendar(self, titulo, horario, usuario_id=None, tarefa_id=None):
        item = Agendamento(
            titulo=titulo,
            horario=horario,
            usuario_id=usuario_id,
            tarefa_id=tarefa_id,
        )
        return self._repositorio.salvar(item)

    def listar(self):
        return self._repositorio.listar_todos()

    def cancelar(self, agendamento_id):
        item = self._repositorio.buscar_por_id(agendamento_id)
        if item:
            item.ativo = False
            self._repositorio.atualizar(item)
        return item
