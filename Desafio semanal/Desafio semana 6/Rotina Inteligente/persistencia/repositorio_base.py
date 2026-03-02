class RepositorioBase:
    """Repositório base com operações CRUD genéricas em memória."""

    def __init__(self):
        self._dados = {}
        self._proximo_id = 1

    def salvar(self, entidade):
        if not hasattr(entidade, "id") or entidade.id is None:
            entidade.id = self._proximo_id
            self._proximo_id += 1
        self._dados[entidade.id] = entidade
        return entidade

    def buscar_por_id(self, entity_id):
        return self._dados.get(entity_id)

    def listar_todos(self):
        return list(self._dados.values())

    def remover(self, entity_id):
        return self._dados.pop(entity_id, None)

    def atualizar(self, entidade):
        if entidade.id not in self._dados:
            return None
        self._dados[entidade.id] = entidade
        return entidade
