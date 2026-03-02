from datetime import datetime


class Agendamento:
    """Entidade que representa um item agendado na rotina."""

    def __init__(self, titulo, horario, usuario_id=None, tarefa_id=None, id=None):
        self.id = id
        self.titulo = titulo
        self.horario = horario if isinstance(horario, datetime) else datetime.fromisoformat(horario)
        self.usuario_id = usuario_id
        self.tarefa_id = tarefa_id
        self.ativo = True

    def __repr__(self):
        return f"Agendamento(id={self.id}, titulo={self.titulo!r}, horario={self.horario})"
