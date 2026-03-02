class Tarefa:
    """Entidade que representa uma tarefa."""

    STATUS_PENDENTE = "pendente"
    STATUS_EM_ANDAMENTO = "em_andamento"
    STATUS_CONCLUIDA = "concluida"

    def __init__(self, titulo, descricao="", usuario_id=None, id=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.usuario_id = usuario_id
        self.status = self.STATUS_PENDENTE

    def __repr__(self):
        return f"Tarefa(id={self.id}, titulo={self.titulo!r}, status={self.status!r})"
