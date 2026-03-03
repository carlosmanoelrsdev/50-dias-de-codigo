from tarefas import GerenciadorTarefas
from agendamento import listar_tarefas_hoje
from automacao_regras import listar_regras, adicionar_regra, avaliar_regras
from notificacoes import verificar_lembretes
from clima import exibir_clima

gerenciador = GerenciadorTarefas()


def menu_principal():
    print("\n=============================")
    print("    ROTINA INTELIGENTE")
    print("=============================")
    print("[1] Gerenciar tarefas")
    print("[2] Ver tarefas de hoje")
    print("[3] Verificar lembretes agora")
    print("[4] Ver clima e regras ativas")
    print("[5] Gerenciar regras de automação")
    print("[6] Sair")
    print("-----------------------------")
    return input("Sua opção: ").strip()


def menu_tarefas():
    print("\n--- Gerenciar Tarefas ---")
    print("[1] Criar tarefa")
    print("[2] Listar todas as tarefas")
    print("[3] Atualizar status")
    print("[4] Remover tarefa")
    print("[5] Voltar")
    return input("Sua opção: ").strip()


def menu_regras():
    print("\n--- Regras de Automação ---")
    print("[1] Listar regras")
    print("[2] Adicionar regra")
    print("[3] Avaliar regras agora")
    print("[4] Voltar")
    return input("Sua opção: ").strip()


def fluxo_tarefas():
    while True:
        opcao = menu_tarefas()
        if opcao == "1":
            nome = input("Nome da tarefa: ").strip()
            categoria = input("Categoria (ex: saude, trabalho, lazer): ").strip() or "geral"
            hora = input("Hora (HH:MM): ").strip()
            dias = input(
                "Dias da semana (ex: segunda,quarta,sexta): "
            ).strip().lower()
            gerenciador.criar(nome, categoria, hora, dias)
        elif opcao == "2":
            gerenciador.listar()
        elif opcao == "3":
            try:
                tid = int(input("ID da tarefa: "))
            except ValueError:
                print("ID inválido.")
                continue
            novo_status = input("Novo status (ativa/pausada/concluida): ").strip().lower()
            gerenciador.atualizar_status(tid, novo_status)
        elif opcao == "4":
            try:
                tid = int(input("ID da tarefa a remover: "))
            except ValueError:
                print("ID inválido.")
                continue
            gerenciador.remover(tid)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")


def fluxo_regras():
    while True:
        opcao = menu_regras()
        if opcao == "1":
            listar_regras()
        elif opcao == "2":
            condicao = input("Condição climática (ex: chuva, frio, ensolarado): ").strip().lower()
            acao = input("Ação sugerida: ").strip()
            adicionar_regra(condicao, acao)
        elif opcao == "3":
            avaliar_regras()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
