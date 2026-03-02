class ServicoAssistenteIA:
    """Serviço responsável pela integração com assistente de inteligência artificial."""

    def __init__(self, api_key=None):
        self._api_key = api_key
        self._historico = []

    def perguntar(self, mensagem):
        """Envia uma mensagem ao assistente e retorna a resposta."""
        self._historico.append({"papel": "usuario", "mensagem": mensagem})
        # TODO: integrar com API de IA (ex: OpenAI, Gemini)
        resposta = "Assistente ainda não configurado."
        self._historico.append({"papel": "assistente", "mensagem": resposta})
        return resposta

    def limpar_historico(self):
        self._historico = []

    def obter_historico(self):
        return list(self._historico)
