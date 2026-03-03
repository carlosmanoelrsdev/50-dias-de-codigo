from nucleo.configuracao import NOME_SISTEMA, VERSAO
from tarefas.servico import ServicoTarefas
from agendamento.servico import ServicoAgendamento
from notificacoes.servico import ServicoNotificacoes
from clima.servico import ServicoClima
from interface.menu import exibir_menu_principal, exibir_menu_tarefas
from automacao_regras.servico import ServicoAutomacaoRegras
from assistente_ia.servico import ServicoAssistenteIA


def gerenciar_tarefas(servico_tarefas, servico_notificacoes):
    while True:
        opcao = exibir_menu_tarefas()

        if opcao == 1:
            titulo = input("Título da tarefa: ")
            if not titulo:
                print("O título não pode ficar vazio!")
                continue
            descricao = input("Descrição (opcional): ")
            prioridade = input("Prioridade [baixa/normal/alta] (padrão: normal): ").strip() or "normal"
            tarefa = servico_tarefas.criar_tarefa(titulo, descricao, prioridade)
            servico_notificacoes.enviar(f"Tarefa '{tarefa.titulo}' criada com ID {tarefa.id}.")
            print(f"Tarefa criada com sucesso! ID: {tarefa.id}")

        elif opcao == 2:
            tarefas = servico_tarefas.listar_tarefas()
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            for t in tarefas:
                print(f"ID: {t.id} | {t.titulo} | Prioridade: {t.prioridade} | Status: {t.status}")

        elif opcao == 3:
            try:
                id = int(input("ID da tarefa a atualizar: "))
            except ValueError:
                print("ID inválido!")
                continue
            novo_status = input("Novo status [pendente/em andamento/concluído]: ").strip()
            tarefa = servico_tarefas.atualizar_tarefa(id, status=novo_status if novo_status else None)
            if tarefa:
                print(f"Tarefa ID {id} atualizada.")
            else:
                print(f"Tarefa ID {id} não encontrada.")

        elif opcao == 4:
            try:
                id = int(input("ID da tarefa a remover: "))
            except ValueError:
                print("ID inválido!")
                continue
            if servico_tarefas.remover_tarefa(id):
                print(f"Tarefa ID {id} removida.")
            else:
                print(f"Tarefa ID {id} não encontrada.")

        elif opcao == 0:
            break
        else:
            print("Opção inválida!")

        input("\nAperte qualquer tecla para continuar: ")


def main():
    print(f"Bem-vindo ao {NOME_SISTEMA} v{VERSAO}!")

    servico_tarefas = ServicoTarefas()
    servico_agendamento = ServicoAgendamento()
    servico_notificacoes = ServicoNotificacoes()
    servico_clima = ServicoClima()
    servico_automacao = ServicoAutomacaoRegras()
    assistente = ServicoAssistenteIA()

    while True:
        opcao = exibir_menu_principal()

        if opcao == 1:
            gerenciar_tarefas(servico_tarefas, servico_notificacoes)

        elif opcao == 2:
            agendamentos = servico_agendamento.listar_agendamentos()
            if not agendamentos:
                print("Nenhum agendamento cadastrado.")
            for a in agendamentos:
                print(f"ID: {a.id} | {a.titulo} | {a.data_hora} | Ativo: {a.ativo}")

        elif opcao == 3:
            historico = servico_notificacoes.listar_historico()
            if not historico:
                print("Nenhuma notificação registrada.")
            for n in historico:
                print(f"[{n['data_hora']}] [{n['tipo'].upper()}] {n['mensagem']}")

        elif opcao == 4:
            cidade = input("Digite o nome da cidade: ")
            dados = servico_clima.buscar_clima(cidade)
            print(f"\nCidade: {dados['cidade']}")
            print(f"Temperatura: {dados['temperatura']}")
            print(f"Descrição: {dados['descricao']}")
            sugestao = servico_clima.adaptar_rotina_ao_clima(dados)
            print(f"Sugestão: {sugestao}")

        elif opcao == 5:
            regras = servico_automacao.listar_regras()
            if not regras:
                print("Nenhuma regra cadastrada.")
            for r in regras:
                print(f"ID: {r.id} | {r.nome} | Ativa: {r.ativa}")

        elif opcao == 6:
            tarefas = servico_tarefas.listar_tarefas()
            agendamentos = servico_agendamento.listar_agendamentos()
            resumo = assistente.gerar_resumo_diario(tarefas, agendamentos)
            print("\n=== Resumo do Dia ===")
            print(f"Total de tarefas: {resumo['total_tarefas']}")
            print(f"Concluídas: {resumo['concluidas']}")
            print(f"Pendentes: {resumo['pendentes']}")
            print(f"Agendamentos: {resumo['agendamentos']}")

        elif opcao == 0:
            print("Encerrando Rotina Inteligente...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            continue

        input("\nAperte qualquer tecla para continuar: ")


main()
