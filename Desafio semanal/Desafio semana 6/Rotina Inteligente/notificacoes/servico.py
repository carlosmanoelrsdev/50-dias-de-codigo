from datetime import datetime


class ServicoNotificacoes:
    def __init__(self):
        self.historico = []

    def enviar(self, mensagem, tipo="info"):
        notificacao = {
            "mensagem": mensagem,
            "tipo": tipo,
            "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        self.historico.append(notificacao)
        print(f"[{tipo.upper()}] {mensagem}")

    def listar_historico(self):
        return self.historico
