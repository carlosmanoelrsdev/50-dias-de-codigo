from datetime import datetime
from database import obter_conexao

DIAS_SEMANA = {
    0: "segunda",
    1: "terca",
    2: "quarta",
    3: "quinta",
    4: "sexta",
    5: "sabado",
    6: "domingo",
}


def obter_dia_atual():
    return DIAS_SEMANA[datetime.now().weekday()]


def obter_hora_atual():
    return datetime.now().strftime("%H:%M")


def listar_tarefas_hoje():
    dia_hoje = obter_dia_atual()
    hora_atual = obter_hora_atual()
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, nome, categoria, hora, dias_semana, status FROM tarefas WHERE status = 'ativa'"
        )
        linhas = cursor.fetchall()
    agendadas = [t for t in linhas if dia_hoje in t[4].lower()]
    if not agendadas:
        print(f"Nenhuma tarefa agendada para hoje ({dia_hoje.capitalize()}).")
        return []
    print(f"\n=== Tarefas para hoje ({dia_hoje.capitalize()}) - Hora atual: {hora_atual} ===")
    for t in agendadas:
        print(f"  [{t[3]}] {t[1]} ({t[2]})")
    return agendadas
