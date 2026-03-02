import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from persistencia.repositorio_base import RepositorioBase
from .modelo import Regra


class ServicoAutomacaoRegras:
    """Serviço responsável pelo gerenciamento de regras de automação."""

    def __init__(self):
        self._repositorio = RepositorioBase()

    def criar_regra(self, nome, condicao, acao):
        regra = Regra(nome=nome, condicao=condicao, acao=acao)
        return self._repositorio.salvar(regra)

    def listar_regras(self, apenas_ativas=False):
        regras = self._repositorio.listar_todos()
        if apenas_ativas:
            regras = [r for r in regras if r.ativa]
        return regras

    def ativar(self, regra_id):
        regra = self._repositorio.buscar_por_id(regra_id)
        if regra:
            regra.ativa = True
            self._repositorio.atualizar(regra)
        return regra

    def desativar(self, regra_id):
        regra = self._repositorio.buscar_por_id(regra_id)
        if regra:
            regra.ativa = False
            self._repositorio.atualizar(regra)
        return regra

    def executar_regras(self, contexto):
        """Avalia e executa as regras ativas com base no contexto informado."""
        for regra in self.listar_regras(apenas_ativas=True):
            if callable(regra.condicao) and regra.condicao(contexto):
                if callable(regra.acao):
                    regra.acao(contexto)
