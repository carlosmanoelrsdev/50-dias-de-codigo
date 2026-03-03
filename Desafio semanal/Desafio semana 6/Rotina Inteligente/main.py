from tarefas.servico import ServicoTarefas
from agendamento.servico import ServicoAgendamento
from notificacoes.servico import ServicoNotificacoes
from clima.servico import ServicoClima
from automacao_regras.servico import ServicoAutomacaoRegras
from assistente_ia.servico import ServicoAssistenteIA
from interface.app import Interface


def main():
    servico_tarefas = ServicoTarefas()
    servico_agendamento = ServicoAgendamento()
    servico_notificacoes = ServicoNotificacoes()
    servico_clima = ServicoClima()
    servico_automacao = ServicoAutomacaoRegras()
    assistente = ServicoAssistenteIA()

    app = Interface(
        servico_tarefas,
        servico_agendamento,
        servico_notificacoes,
        servico_clima,
        servico_automacao,
        assistente
    )
    app.mainloop()

    print("Finalizando Rotina Inteligente...")


main()
