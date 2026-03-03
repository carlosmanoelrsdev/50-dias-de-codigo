from agendamento import listar_tarefas_hoje
from datetime import datetime


def verificar_lembretes():
    hora_atual = datetime.now().strftime("%H:%M")
    tarefas_hoje = listar_tarefas_hoje()
    lembretes = []
    for t in tarefas_hoje:
        if t[3] == hora_atual:
            lembretes.append(t)
            print(f"  *** LEMBRETE: '{t[1]}' está agendada agora ({hora_atual})! ***")
    if not lembretes:
        print("Nenhum lembrete ativo para o horário atual.")
    return lembretes


def enviar_notificacao(mensagem):
    print(f"\n[NOTIFICAÇÃO] {mensagem}")
