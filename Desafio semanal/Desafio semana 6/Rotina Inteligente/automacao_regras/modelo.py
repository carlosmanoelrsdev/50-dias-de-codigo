class Regra:
    def __init__(self, id, nome, condicao, acao, ativa=True):
        self.id = id
        self.nome = nome
        self.condicao = condicao
        self.acao = acao
        self.ativa = ativa
