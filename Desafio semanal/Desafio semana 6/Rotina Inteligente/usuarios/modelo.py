class Usuario:
    """Entidade que representa um usuário do sistema."""

    def __init__(self, nome, email, id=None):
        self.id = id
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome!r}, email={self.email!r})"
