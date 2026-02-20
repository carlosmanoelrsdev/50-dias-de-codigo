# Módulos para requisições HTTP, variáveis de ambiente e manipulação de datas
import requests
import os
from dotenv import load_dotenv
from datetime import datetime


def buscar_clima(cidade):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    # Constrói URL com parâmetros: cidade, chave API e idioma português
    link_clima_atual = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    # Requisita dados à API
    requisicao_atual = requests.get(link_clima_atual)
    requisicao_dic_atual = requisicao_atual.json()
    cod = requisicao_dic_atual.get("cod")
    
    # Tratamento de códigos de resposta HTTP
    if cod == 200:
        # Sucesso: extrai dados climáticos
        descricao_clima = requisicao_dic_atual["weather"][0]["description"]
        # Converte temperatura de Kelvin (padrão da API) para Celsius
        temperatura_clima = requisicao_dic_atual["main"]["temp"] - 273.15
        umidade_clima = requisicao_dic_atual["main"]["humidity"]

        dados = {
            "cidade": cidade,
            "temperatura": f"{temperatura_clima:.1f}",
            "descricao": descricao_clima,
            "umidade": umidade_clima,
        }

    elif cod == "404":
        # Erro: cidade não encontrada
        dados = {
            "cidade": cidade,
            "temperatura": "N/A",
            "descricao": "Cidade não encontrada",
            "umidade": "N/A",
        }

    elif cod == 401:
        # Erro: chave API inválida ou expirada
        dados = {
            "cidade": cidade,
            "temperatura": "N/A",
            "descricao": "API KEY inválida",
            "umidade": "N/A",
        }

    elif cod == 429:
        # Erro: limite de requisições excedido
        dados = {
            "cidade": cidade,
            "temperatura": "N/A",
            "descricao": "Muitas requisições — tente novamente mais tarde",
            "umidade": "N/A",
        }

    else:
        # Erro: resposta inesperada da API
        dados = {
            "cidade": cidade,
            "temperatura": "N/A",
            "descricao": f"Erro desconhecido (cod {cod})",
            "umidade": "N/A",
        }

    return dados


def buscar_previsao_proximos_dias(cidade):
    """Busca previsão para os próximos 5 dias e agrupa por dia"""
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    # Endpoint para previsão de 5 dias (retorna dados em intervalos de 3 horas)
    link_proximos_dias = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link_proximos_dias)
    dados_api = requisicao.json()

    # Valida resposta da API
    if dados_api.get("cod") != "200":
        return []

    # Dicionário para agregar múltiplas previsões do mesmo dia
    previsoes_por_dia = {}

    # Itera sobre cada previsão (3 em 3 horas) e agrupa por dia
    for item in dados_api["list"]:
        # Converte timestamp Unix para objeto datetime
        data_hora = datetime.fromtimestamp(item["dt"])
        # Extrai data para usar como chave de agrupamento
        data_str = data_hora.strftime("%Y-%m-%d")
        dia_semana = data_hora.strftime("%A")
        data_formatada = data_hora.strftime("%d/%m/%Y")

        if data_str not in previsoes_por_dia:
            # Primeira previsão do dia: inicializa registro
            previsoes_por_dia[data_str] = {
                "data": data_formatada,
                "dia_semana": dia_semana,
                # Converte temperatura de Kelvin para Celsius
                "temp_min": item["main"]["temp_min"] - 273.15,
                "temp_max": item["main"]["temp_max"] - 273.15,
                "descricao": item["weather"][0]["description"],
                "umidade": item["main"]["humidity"],
                "cidade": cidade,
            }
        else:
            # Atualiza temperatura máxima do dia (mantém a maior encontrada)
            previsoes_por_dia[data_str]["temp_max"] = max(
                previsoes_por_dia[data_str]["temp_max"],
                item["main"]["temp_max"] - 273.15,
            )

    # Converte dict em lista e limita aos primeiros 5 dias
    lista_previsoes = list(previsoes_por_dia.values())[:5]

    return lista_previsoes
