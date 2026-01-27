class Livro():
    def __init__(self, titulo, autor, ano, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponibilidade = disponibilidade

    def pegar_livro(self):
        if self.disponibilidade == 1:
            print(f"O livro {self.titulo} está disponível")
        elif self.disponibilidade == 0:
            print(f"O livro {self.titulo} não está disponível")

def main():
    livro1 = Livro(
        "O pequeno príncipe",
        "Antoine de Saint-Exupéry",
        1943,
        1
    )
    livro2 = Livro(
        "Dom Casmurro",
        "Machado de Assis",
        1899,
        0
    )

    livro1.pegar_livro()
    livro2.pegar_livro()

main()
