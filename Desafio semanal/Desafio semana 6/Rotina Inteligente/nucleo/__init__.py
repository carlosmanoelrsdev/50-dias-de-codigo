from database import inicializar_banco
from automacao_regras import inicializar_regras_padrao
from interface import (
    menu_principal,
    fluxo_tarefas,
    fluxo_regras,
)
from agendamento import listar_tarefas_hoje
from notificacoes import verificar_lembretes
from clima import exibir_clima
from automacao_regras import avaliar_regras


def inicializar():
    inicializar_banco()
    inicializar_regras_padrao()


def executar():
    inicializar()
    while True:
        opcao = menu_principal()
        if opcao == "1":
            fluxo_tarefas()
        elif opcao == "2":
            listar_tarefas_hoje()
        elif opcao == "3":
            verificar_lembretes()
        elif opcao == "4":
            exibir_clima()
            avaliar_regras()
        elif opcao == "5":
            fluxo_regras()
        elif opcao == "6":
            print("Encerrando Rotina Inteligente. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        input("\nAperte Enter para continuar...")
