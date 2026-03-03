from database import obter_conexao


class Tarefa:
    def __init__(self, id, nome, categoria, hora, dias_semana, status):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.hora = hora
        self.dias_semana = dias_semana
        self.status = status

    def __str__(self):
        return (
            f"ID: {self.id} | {self.nome} | {self.categoria} | "
            f"{self.hora} | Dias: {self.dias_semana} | Status: {self.status}"
        )


class GerenciadorTarefas:
    def criar(self, nome, categoria, hora, dias_semana):
        with obter_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tarefas (nome, categoria, hora, dias_semana) VALUES (?, ?, ?, ?)",
                (nome, categoria, hora, dias_semana),
            )
            conn.commit()
            print(f"Tarefa '{nome}' criada com sucesso!")

    def listar(self):
        with obter_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, categoria, hora, dias_semana, status FROM tarefas")
            linhas = cursor.fetchall()
        if not linhas:
            print("Nenhuma tarefa cadastrada.")
            return []
        tarefas = [Tarefa(*linha) for linha in linhas]
        for t in tarefas:
            print(t)
        return tarefas

    def atualizar_status(self, tarefa_id, novo_status):
        with obter_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE tarefas SET status = ? WHERE id = ?",
                (novo_status, tarefa_id),
            )
            conn.commit()
        print(f"Status da tarefa {tarefa_id} atualizado para '{novo_status}'.")

    def remover(self, tarefa_id):
        with obter_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
            conn.commit()
        print(f"Tarefa {tarefa_id} removida.")

    def buscar_por_id(self, tarefa_id):
        with obter_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nome, categoria, hora, dias_semana, status FROM tarefas WHERE id = ?",
                (tarefa_id,),
            )
            linha = cursor.fetchone()
        if linha:
            t = Tarefa(*linha)
            print(t)
            return t
        print(f"Tarefa com ID {tarefa_id} não encontrada.")
        return None
