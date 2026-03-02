class ServicoClima:
    """Serviço responsável pela integração com dados de clima."""

    def __init__(self, api_key=None):
        self._api_key = api_key

    def buscar_clima_atual(self, cidade):
        """Retorna dados de clima atual para a cidade informada."""
        # TODO: integrar com API de clima (ex: OpenWeatherMap)
        return {
            "cidade": cidade,
            "temperatura": None,
            "descricao": None,
            "umidade": None,
        }

    def buscar_previsao(self, cidade, dias=5):
        """Retorna previsão para os próximos dias."""
        # TODO: integrar com API de previsão
        return []
