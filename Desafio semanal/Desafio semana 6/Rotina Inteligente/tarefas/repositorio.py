import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from persistencia.repositorio_base import RepositorioBase


class RepositorioTarefas(RepositorioBase):
    """Repositório de tarefas."""

    def listar_por_usuario(self, usuario_id):
        return [t for t in self._dados.values() if t.usuario_id == usuario_id]

    def listar_por_status(self, status):
        return [t for t in self._dados.values() if t.status == status]
