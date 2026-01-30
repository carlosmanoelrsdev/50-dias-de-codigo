from menu import menu_interativo

def main():
    def criar_task():
        print("criar")
    def listar_task():
        print("Listar")
    def atualizar_task():
        print("atualizar")
    def remover_task():
        print("remover")
    def buscar_task():
        print("buscar")
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

main()