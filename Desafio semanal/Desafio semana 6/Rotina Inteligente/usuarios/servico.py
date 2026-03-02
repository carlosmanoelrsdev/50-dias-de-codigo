from .modelo import Usuario
from .repositorio import RepositorioUsuarios


class ServicoUsuarios:
    """Serviço responsável pela lógica de negócio de usuários."""

    def __init__(self):
        self._repositorio = RepositorioUsuarios()

    def cadastrar(self, nome, email):
        if self._repositorio.buscar_por_email(email):
            raise ValueError(f"Usuário com e-mail '{email}' já cadastrado.")
        usuario = Usuario(nome=nome, email=email)
        return self._repositorio.salvar(usuario)

    def listar(self):
        return self._repositorio.listar_todos()

    def buscar_por_id(self, usuario_id):
        return self._repositorio.buscar_por_id(usuario_id)

    def remover(self, usuario_id):
        return self._repositorio.remover(usuario_id)
