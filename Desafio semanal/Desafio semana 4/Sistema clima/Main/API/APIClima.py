import requests
import os
from dotenv import load_dotenv


def buscar_clima(cidade):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    print("API recebeu a cidade:", cidade)

    link_clima_atual = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao_atual = requests.get(link_clima_atual)
    requisicao_dic_atual = requisicao_atual.json()
    print(requisicao_dic_atual)
    cod = requisicao_dic_atual.get("cod")


    link_proximos_dias = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao_proximos_dias = requests.get(link_clima_atual)
    requisicao_dic_proximos_dias = requisicao_proximos_dias.json()
    print(f"proximos dias {requisicao_dic_proximos_dias}")


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
