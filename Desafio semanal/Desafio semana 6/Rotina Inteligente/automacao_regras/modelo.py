class Regra:
    """Entidade que representa uma regra de automação."""

    def __init__(self, nome, condicao, acao, ativa=True, id=None):
        self.id = id
        self.nome = nome
        self.condicao = condicao
        self.acao = acao
        self.ativa = ativa

    def __repr__(self):
        return f"Regra(id={self.id}, nome={self.nome!r}, ativa={self.ativa})"
