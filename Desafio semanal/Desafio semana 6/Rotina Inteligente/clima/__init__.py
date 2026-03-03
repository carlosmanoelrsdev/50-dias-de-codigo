CLIMA_SIMULADO = {
    "condicao": "ensolarado",
    "temperatura": 28,
    "umidade": 60,
}


def obter_clima():
    """Retorna dados climaticos simulados para uso nas regras de automacao."""
    return CLIMA_SIMULADO


def exibir_clima():
    dados = obter_clima()
    print(
        f"Clima atual: {dados['condicao'].capitalize()} | "
        f"Temperatura: {dados['temperatura']}°C | "
        f"Umidade: {dados['umidade']}%"
    )
