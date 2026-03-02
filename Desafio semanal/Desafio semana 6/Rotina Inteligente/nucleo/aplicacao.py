import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from usuarios.servico import ServicoUsuarios
from tarefas.servico import ServicoTarefas
from agendamento.servico import ServicoAgendamento
from notificacoes.servico import ServicoNotificacoes
from clima.servico import ServicoClima
from assistente_ia.servico import ServicoAssistenteIA
from automacao_regras.servico import ServicoAutomacaoRegras


class Aplicacao:
    """Núcleo da aplicação Rotina Inteligente.

    Centraliza a inicialização dos serviços e o ciclo de vida da aplicação.
    """

    def __init__(self):
        self.servico_usuarios = ServicoUsuarios()
        self.servico_tarefas = ServicoTarefas()
        self.servico_agendamento = ServicoAgendamento()
        self.servico_notificacoes = ServicoNotificacoes()
        self.servico_clima = ServicoClima()
        self.servico_assistente_ia = ServicoAssistenteIA()
        self.servico_automacao = ServicoAutomacaoRegras()

    def iniciar(self):
        """Inicia o ciclo principal da aplicação."""
        from interface.menu import MenuPrincipal
        menu = MenuPrincipal(self)
        menu.executar()
