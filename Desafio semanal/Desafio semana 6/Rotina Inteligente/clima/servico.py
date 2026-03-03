class ServicoClima:
    def buscar_clima(self, cidade):
        """Retorna dados climáticos da cidade informada."""
        # Integração com API de clima a ser implementada
        return {
            "cidade": cidade,
            "temperatura": "N/A",
            "descricao": "Serviço de clima não configurado",
            "umidade": "N/A"
        }

    def adaptar_rotina_ao_clima(self, dados_clima):
        """Sugere ajustes na rotina com base nas condições climáticas."""
        descricao = dados_clima.get("descricao", "").lower()
        if "chuva" in descricao:
            return "Chuva prevista: evite atividades ao ar livre"
        elif "sol" in descricao or "limpo" in descricao:
            return "Dia ensolarado: ótimo para atividades externas"
        return "Verifique a previsão antes de planejar atividades externas"
