class Animal():
    def __init__(self, especie, categoria, tamanho, som):
        self.especie = especie
        self.categoria = categoria
        self.tamanho = tamanho
        self.som = som
    
    def emitir_som(self):
        print(f"O {self.especie} faz '{self.som}'")

    
    def alimentar_animal(self):
        print(f"{self.especie} foi alimentado!")
    
class Zoologico():
    def adicionar_animal(self):
        especie = input("Espécie do animal: ")
        categoria = input("Categoria do animal: ")
        tamanho = input("Tamanho do animal: ")
        som = input("Som do animal: ")
        self.cadastrar_animal(especie, categoria, tamanho, som)
    
    def cadastrar_animal(self, especie, categoria, tamanho, som):
        novo_animal = Animal(especie, categoria, tamanho, som)
        animais_cadastrados.append(novo_animal)
        print(f"O {especie} foi cadastrado")

animais_cadastrados = [
    Animal("Leão", "Carnívoro", "Grande", "Ruarrrrr")
    ]


def main():
    zoo = Zoologico()
    registro_do_animal = 0
    print("Bem vindo ao sistema do zoológico")

    while True:
        opcao = int(input("\n[1] Adicionar animal. [2] Emitir som dos animais. [3] Alimentar animais. [4] listar animais. \n Sua escolha: "))

        if opcao == 1:
            zoo.adicionar_animal()

        elif opcao == 2:
            for animal in animais_cadastrados:
                animal.emitir_som()

        elif opcao == 3:
            for animal in animais_cadastrados:
                animal.alimentar_animal()

        elif opcao == 4:
            for animal in animais_cadastrados:
                registro_do_animal += 1
                print(f"Id de registro: {registro_do_animal} e a especie é {animal.especie}")
        
        else:
            print("Encerrando programa...")
            break
main()