from menu import menu_interativo
from Classes import Gerenciador_taferas

def main():
    gerenciador = Gerenciador_taferas()
    
    def criar_task():
        print("=== Criar Tarefa ===")
        titulo = input("Digite sua tarefa: ")
        while True:
            if not titulo:
                titulo = input("A tarefa não pode ficar vazio! Digite sua tarefa: ")
            if titulo:
               break
        
        tarefa = gerenciador.criar_tarefa(titulo)
        print(f"A tarefa '{titulo}' foi adicionada com ID {tarefa.status_id}!")

    def listar_task():
        print("\n=== Listar Tarefas ===")
        gerenciador.listar_tarefas()
        
    def atualizar_task():
        print("=== Atualizar Tarefa ===")
        try:
            status_id = int(input("Digite o ID da tarefa que deseja atualizar: "))
        except ValueError:
            print("ID inválido! digite um número inteiro.")
            return

        while True:
            try:
                qual_atualizar = int(input("Qual deseja atualizar [1] Título da tarefa [2] Status da tarefa.\nSua opção: "))
            except ValueError:
                print("Permitido somente número inteiros!")
                continue
            if qual_atualizar == 1:
                novo_titulo = input("Digite o novo título: ")
                gerenciador.atualizar_tarefas(status_id, novo_titulo if novo_titulo else None)
                if not novo_titulo:
                    print('O título não pode ficar vazio. \nReiniciando pergunta...')
                    continue
                break

            elif qual_atualizar == 2:
                novo_status = input("Digite o novo status [1] Pendente [2] Concluído.\n")
                if not novo_status or novo_status not in ("1", "2"):
                    print('Opção de status não disponível. \nReiniciando pergunta...')
                    continue
                if novo_status == "1":
                    novo_status = "pendente"
                elif novo_status == "2":
                    novo_status = "concluído"
                gerenciador.atualizar_tarefas(status_id, None, novo_status)
                break
            else:
                print("Digite uma das opções Disponíveis!")


    def remover_task():
        print("=== Remover Tarefa ===")
        try:
            status_id = int(input("Digite o ID da tarefa que deseja remover: "))
        except ValueError:
            print("ID inválido. Por favor, digite um número inteiro.")
            return
        gerenciador.remover_tarefa(status_id)

    def buscar_task():
        print("=== Buscar Tarefa pelo ID ===")
        try:
            status_id = int(input("Digite o ID da tarefa que deseja buscar: "))
        except ValueError:
            print("ID inválido. Digite um número inteiro.")
            return
        gerenciador.buscar_tarefa_por_id(status_id)
        
    def finalizar_sistema():
        print("Encerrando Sistema...")

    direcionar_funcao = {
    1: criar_task,
    2: listar_task,
    3: atualizar_task,
    4: remover_task,
    5: buscar_task,
    6: finalizar_sistema
    }

    
    while True:
        try:
            opcao = menu_interativo()
        except ValueError:
            print("Opção não aceita! digite valores entre 1 e 6.")
            continue

        funcao = direcionar_funcao.get(opcao)
        if not funcao:
            print("Opção não aceita! digite valores entre 1 e 6.")
            continue

        funcao()

        if opcao == 6:
            break
        continuar = input("Aperte qualquer tecla para continuar: ")

main()