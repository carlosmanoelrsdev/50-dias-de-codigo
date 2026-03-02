class Notificacao:
    """Entidade que representa uma notificação enviada ao usuário."""

    TIPO_INFO = "info"
    TIPO_ALERTA = "alerta"
    TIPO_LEMBRETE = "lembrete"

    def __init__(self, mensagem, usuario_id=None, tipo=TIPO_INFO, id=None):
        self.id = id
        self.mensagem = mensagem
        self.usuario_id = usuario_id
        self.tipo = tipo
        self.lida = False

    def __repr__(self):
        return f"Notificacao(id={self.id}, tipo={self.tipo!r}, lida={self.lida})"
