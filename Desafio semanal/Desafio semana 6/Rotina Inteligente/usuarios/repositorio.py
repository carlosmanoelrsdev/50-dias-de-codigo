class RepositorioUsuarios:
    def __init__(self):
        self.usuarios = {}
        self.proximo_id = 1

    def salvar(self, usuario):
        self.usuarios[usuario.id] = usuario
        return usuario

    def buscar_por_id(self, id):
        return self.usuarios.get(id)

    def listar_todos(self):
        return list(self.usuarios.values())

    def proximo_id_disponivel(self):
        id_atual = self.proximo_id
        self.proximo_id += 1
        return id_atual
