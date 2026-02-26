"""
Arquivo de Testes Automatizados - Sistema de Clima
Desafio Semana 5: Testes e Boas Práticas

Este módulo contém testes unitários e de integração para validar
o funcionamento correto das funcionalidades principais do sistema de clima.

Testes cobertos:
- Validação de dados climáticos
- Comportamento da API em diferentes cenários
- Tratamento de erros
- Formatação de dados
"""

import sys
import os

# Adiciona o diretório pai ao path para importações funcionarem
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from unittest.mock import patch, MagicMock
from Main.API.APIClima import buscar_clima, buscar_previsao_proximos_dias
from Main.Frases.frases_clima import FRASES_CLIMA


def _print_teste_ok(mensagem):
    print(mensagem)


# TESTES 1-3: VALIDAÇÃO DE DADOS E ESTRUTURAS

class TestEstruturaDados:
    """Testes para validar a estrutura e integridade dos dados"""

    def test_frases_clima_nao_vazio(self):
        """Teste 1: Verificar se o dicionário de frases não está vazio"""
        assert len(FRASES_CLIMA) > 0, "Dicionário de frases climáticas está vazio"
        _print_teste_ok("Teste 1 - frases de clima carregadas")

    def test_frases_clima_contem_tipos_esperados(self):
        """Teste 2: Validar que FRASES_CLIMA contém chaves e valores corretos"""
        assert isinstance(FRASES_CLIMA, dict), "FRASES_CLIMA não é um dicionário"

        for chave, valor in FRASES_CLIMA.items():
            assert isinstance(chave, str), f"Chave '{chave}' não é string"
            assert isinstance(valor, str), f"Valor para '{chave}' não é string"
            assert len(valor) > 0, f"Valor para '{chave}' está vazio"
        _print_teste_ok("Teste 2 - tipos e valores ok")

    def test_frases_clima_contem_climas_esperados(self):
        """Teste 3: Verificar se frases para climas comuns existem"""
        climas_esperados = ["céu limpo", "chuva forte", "nublado"]

        for clima in climas_esperados:
            assert (
                clima in FRASES_CLIMA
            ), f"Clima '{clima}' não encontrado em FRASES_CLIMA"
        _print_teste_ok("Teste 3 - climas esperados encontrados")


# TESTES 4-7: BUSCA DE CLIMA COM MOCKS (Sucesso e Erros)

class TestBuscarClima:
    """Testes para a função buscar_clima com diferentes respostas de API"""

    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_buscar_clima_sucesso(self, mock_get):
        """Teste 4: Verificar busca com sucesso (código 200)"""
        # Simula resposta exata do OpenWeatherMap
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": 200,
            "weather": [{"description": "céu limpo"}],
            "main": {"temp": 298.15, "humidity": 60},  # 298.15K = 25°C
        }
        mock_get.return_value = mock_response

        resultado = buscar_clima("São Paulo")

        # Validações
        assert resultado["cidade"] == "São Paulo"
        assert (
            resultado["temperatura"] == "25.0"
        ), "Conversão de Kelvin para Celsius falhou"
        assert resultado["descricao"] == "céu limpo"
        assert resultado["umidade"] == 60
        _print_teste_ok("Teste 4 - clima ok com codigo 200")

    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_buscar_clima_cidade_nao_encontrada(self, mock_get):
        """Teste 5: Verificar erro 404 - Cidade não encontrada"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"cod": "404"}
        mock_get.return_value = mock_response

        resultado = buscar_clima("CidadeInexistente123")

        assert resultado["temperatura"] == "N/A"
        assert resultado["descricao"] == "Cidade não encontrada"
        assert resultado["umidade"] == "N/A"
        _print_teste_ok("Teste 5 - cidade nao encontrada tratado")

    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "invalid_key"})
    def test_buscar_clima_api_key_invalida(self, mock_get):
        """Teste 6: Verificar erro 401 - API KEY inválida"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"cod": 401}
        mock_get.return_value = mock_response

        resultado = buscar_clima("Londres")

        assert resultado["descricao"] == "API KEY inválida"
        assert resultado["temperatura"] == "N/A"
        _print_teste_ok("Teste 6 - api key invalida tratada")

    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_buscar_clima_limite_requisicoes(self, mock_get):
        """Teste 7: Verificar erro 429 - Limite de requisições excedido"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"cod": 429}
        mock_get.return_value = mock_response

        resultado = buscar_clima("Tóquio")

        assert (
            resultado["descricao"] == "Muitas requisições — tente novamente mais tarde"
        )
        assert resultado["temperatura"] == "N/A"
        _print_teste_ok("Teste 7 - limite de requisicoes tratado")

    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_buscar_clima_erro_desconhecido(self, mock_get):
        """Teste 8: Verificar tratamento de erro desconhecido"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"cod": 500}
        mock_get.return_value = mock_response

        resultado = buscar_clima("Paris")

        assert "Erro desconhecido" in resultado["descricao"]
        assert resultado["temperatura"] == "N/A"
        _print_teste_ok("Teste 8 - erro desconhecido tratado")


# TESTES 9-10: VALIDAÇÃO DE FORMATAÇÃO E DADOS

class TestFormatacaoDados:
    """Testes para validar a formatação correta dos dados retornados"""

    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_temperatura_formatada_corretamente(self, mock_get):
        """Teste 9: Verificar se temperatura é formatada com 1 casa decimal"""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": 200,
            "weather": [{"description": "céu limpo"}],
            "main": {"temp": 300.45, "humidity": 50},  # Temperatura aleatória em Kelvin
        }
        mock_get.return_value = mock_response

        resultado = buscar_clima("Rio")

        # Verifica se a temperatura tem exatamente 1 casa decimal
        temp_str = resultado["temperatura"]
        assert "." in temp_str, "Temperatura não contém ponto decimal"
        partes = temp_str.split(".")
        assert (
            len(partes[1]) == 1
        ), f"Temperatura deveria ter 1 casa decimal, mas tem {len(partes[1])}"
        _print_teste_ok("Teste 9 - temperatura com 1 casa decimal")

    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_estrutura_dados_completa(self, mock_get):
        """Teste 10: Validar que todos os campos obrigatórios estão presentes"""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": 200,
            "weather": [{"description": "chuva"}],
            "main": {"temp": 290.15, "humidity": 80},
        }
        mock_get.return_value = mock_response

        resultado = buscar_clima("Brasília")

        # Validações
        campos_obrigatorios = ["cidade", "temperatura", "descricao", "umidade"]
        for campo in campos_obrigatorios:
            assert (
                campo in resultado
            ), f"Campo obrigatório '{campo}' não encontrado no resultado"

        # Valida tipos
        assert isinstance(resultado["cidade"], str)
        assert isinstance(resultado["temperatura"], str)
        assert isinstance(resultado["descricao"], str)
        _print_teste_ok("Teste 10 - estrutura de dados completa")


# TESTES 11-12: CONVERSÃO DE TEMPERATURA

class TestConversaoTemperatura:
    """Testes para validar a conversão de Kelvin para Celsius"""

    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_conversao_kelvin_celsius_zero_absoluto(self, mock_get):
        """Teste 11: Validar conversão em casos extremos (próximo ao zero absoluto)"""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": 200,
            "weather": [{"description": "neve"}],
            "main": {"temp": 273.15, "humidity": 30},  # 0°C em Kelvin
        }
        mock_get.return_value = mock_response

        resultado = buscar_clima("Sibéria")

        assert resultado["temperatura"] == "0.0"
        _print_teste_ok("Teste 11 - conversao zero absoluto ok")

    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_conversao_kelvin_celsius_temperatura_alta(self, mock_get):
        """Teste 12: Validar conversão em temperatura alta"""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": 200,
            "weather": [{"description": "céu limpo"}],
            "main": {"temp": 323.15, "humidity": 40},  # 50°C em Kelvin
        }
        mock_get.return_value = mock_response

        resultado = buscar_clima("Deserto")

        assert resultado["temperatura"] == "50.0"
        _print_teste_ok("Teste 12 - conversao temperatura alta ok")


# TESTES 13: INTEGRAÇÃO COM PREVISÃO

class TestPrevisaoProximosDias:
    """Testes para a função de previsão dos próximos dias"""

    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_previsao_proximos_dias_resposta_invalida(self, mock_get):
        """Teste 13: Verificar tratamento de resposta inválida na previsão"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"cod": "404"}
        mock_get.return_value = mock_response

        resultado = buscar_previsao_proximos_dias("CidadeInvalida")

        assert resultado == [], "Deveria retornar lista vazia para resposta inválida"
        _print_teste_ok("Teste 13 - previsao invalida retorna lista vazia")


# TESTES DE PARAMETRIZAÇÃO (Extra: Múltiplos casos em um teste)

class TestParametrizacao:
    """Testes parametrizados para cobrir múltiplos cenários"""

    @pytest.mark.parametrize(
        "codigo_erro,mensagem_esperada",
        [
            ("404", "Cidade não encontrada"),
            (401, "API KEY inválida"),
            (429, "Muitas requisições — tente novamente mais tarde"),
        ],
    )
    @patch("Main.API.APIClima.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_erros_api_parametrizados(self, mock_get, codigo_erro, mensagem_esperada):
        """
        Teste 14: Validar múltiplos códigos de erro em um único teste

        Este teste parametrizado verifica automaticamente 3 casos de erro
        diferentes sem duplicar código.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"cod": codigo_erro}
        mock_get.return_value = mock_response

        resultado = buscar_clima("TestCity")

        assert resultado["descricao"] == mensagem_esperada
        _print_teste_ok(f"Teste 14 - erro {codigo_erro} tratado")


# CONFIGURAÇÃO PYTEST

if __name__ == "__main__":
    # Permite executar testes diretamente com: python Teste_Automatizado.py
    pytest.main([__file__, "-v", "-s", "--tb=short"])
