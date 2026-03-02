import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from persistencia.repositorio_base import RepositorioBase


class RepositorioUsuarios(RepositorioBase):
    """Repositório de usuários."""

    def buscar_por_email(self, email):
        for usuario in self._dados.values():
            if usuario.email == email:
                return usuario
        return None
