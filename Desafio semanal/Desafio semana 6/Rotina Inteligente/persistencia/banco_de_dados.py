import json
import os

from nucleo.configuracao import ARQUIVO_DADOS


class BancoDeDados:
    def __init__(self, arquivo=ARQUIVO_DADOS):
        self.arquivo = arquivo

    def salvar(self, dados):
        """Salva os dados no arquivo JSON."""
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

    def carregar(self):
        """Carrega os dados do arquivo JSON. Retorna dicionário vazio se não existir."""
        if not os.path.exists(self.arquivo):
            return {}
        with open(self.arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def limpar(self):
        """Remove o arquivo de dados."""
        if os.path.exists(self.arquivo):
            os.remove(self.arquivo)
