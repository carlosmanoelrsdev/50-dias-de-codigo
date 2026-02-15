import requests
import os
from dotenv import load_dotenv
from datetime import datetime


def buscar_clima(cidade):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    print("Entrou no sistema....")
    print("API recebeu a cidade:", cidade)

    link_clima_atual = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao_atual = requests.get(link_clima_atual)
    requisicao_dic_atual = requisicao_atual.json()
    cod = requisicao_dic_atual.get("cod")


    if cod == 200:
        descricao_clima = requisicao_dic_atual["weather"][0]["description"]
        temperatura_clima = (requisicao_dic_atual["main"]["temp"] - 273.15)
        umidade_clima = requisicao_dic_atual["main"]["humidity"]

        dados = {
            "cidade": cidade,
            "temperatura": f"{temperatura_clima:.1f}",
            "descricao": descricao_clima,
            "umidade": umidade_clima
        }

    elif cod == "404":
        dados = {
            "cidade": cidade,
            "temperatura": "N/A",
            "descricao": "Cidade não encontrada",
            "umidade": "N/A"
        }

    elif cod == 401:
        dados = {
            "cidade": cidade,
            "temperatura": "N/A",
            "descricao": "API KEY inválida",
            "umidade": "N/A"
        }

    elif cod == 429:
        dados = {
            "cidade": cidade,
            "temperatura": "N/A",
            "descricao": "Muitas requisições — tente novamente mais tarde",
            "umidade": "N/A"
        }

    else:
        dados = {
            "cidade": cidade,
            "temperatura": "N/A",
            "descricao": f"Erro desconhecido (cod {cod})",
            "umidade": "N/A"
        }

    return dados


def buscar_previsao_proximos_dias(cidade):
    """Busca previsão para os próximos 5 dias e agrupa por dia"""
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    link_proximos_dias = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&lang=pt_br"
    
    requisicao = requests.get(link_proximos_dias)
    dados_api = requisicao.json()
    
    if dados_api.get("cod") != "200":
        return []
    
    previsoes_por_dia = {}
    
    for item in dados_api["list"]:
        data_hora = datetime.fromtimestamp(item["dt"])
        data_str = data_hora.strftime("%Y-%m-%d")
        dia_semana = data_hora.strftime("%A")
        data_formatada = data_hora.strftime("%d/%m/%Y")
        
        if data_str not in previsoes_por_dia:
            previsoes_por_dia[data_str] = {
                "data": data_formatada,
                "dia_semana": dia_semana,
                "temp_min": item["main"]["temp_min"] - 273.15,
                "temp_max": item["main"]["temp_max"] - 273.15,
                "descricao": item["weather"][0]["description"],
                "umidade": item["main"]["humidity"],
                "cidade": cidade
            }
        else:
            previsoes_por_dia[data_str]["temp_max"] = max(
                previsoes_por_dia[data_str]["temp_max"], 
                item["main"]["temp_max"] - 273.15
            )
    
    lista_previsoes = list(previsoes_por_dia.values())[:5]
    
    return lista_previsoes
