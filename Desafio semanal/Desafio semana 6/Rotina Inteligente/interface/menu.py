def exibir_menu_principal():
    print("\n=== Rotina Inteligente ===")
    print("[1] Gerenciar Tarefas")
    print("[2] Agendamentos")
    print("[3] Notificações")
    print("[4] Consultar Clima")
    print("[5] Automação de Regras")
    print("[6] Resumo do Dia")
    print("[0] Sair")

    try:
        opcao = int(input("Sua opção: "))
    except ValueError:
        return -1
    return opcao


def exibir_menu_tarefas():
    print("\n=== Gerenciar Tarefas ===")
    print("[1] Criar tarefa")
    print("[2] Listar tarefas")
    print("[3] Atualizar status")
    print("[4] Remover tarefa")
    print("[0] Voltar")

    try:
        opcao = int(input("Sua opção: "))
    except ValueError:
        return -1
    return opcao
