from clima import obter_clima
from database import obter_conexao


REGRAS_PADRAO = [
    ("chuva", "Lembre-se de levar guarda-chuva e prefira atividades internas."),
    ("frio", "Vista-se bem e considere adiar atividades externas."),
    ("ensolarado", "Ótimo dia para atividades ao ar livre!"),
    ("nublado", "Dia nublado, fique atento a possíveis chuvas."),
]


def inicializar_regras_padrao():
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM regras")
        total = cursor.fetchone()[0]
        if total == 0:
            cursor.executemany(
                "INSERT INTO regras (condicao, acao) VALUES (?, ?)",
                REGRAS_PADRAO,
            )
            conn.commit()


def avaliar_regras():
    dados_clima = obter_clima()
    condicao_atual = dados_clima["condicao"].lower()
    temperatura = dados_clima["temperatura"]

    if temperatura < 15:
        condicao_atual = "frio"

    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT acao FROM regras WHERE ativa = 1 AND condicao = ?",
            (condicao_atual,),
        )
        regras = cursor.fetchall()

    if regras:
        print("\n=== Regras de Automação Ativadas ===")
        for regra in regras:
            print(f"  -> {regra[0]}")
    else:
        print("Nenhuma regra de automação aplicável no momento.")


def listar_regras():
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, condicao, acao, ativa FROM regras")
        regras = cursor.fetchall()
    if not regras:
        print("Nenhuma regra cadastrada.")
        return
    print("\n=== Regras de Automação ===")
    for r in regras:
        estado = "Ativa" if r[3] else "Inativa"
        print(f"  ID: {r[0]} | Condição: {r[1]} | Ação: {r[2]} | {estado}")


def adicionar_regra(condicao, acao):
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regras (condicao, acao) VALUES (?, ?)",
            (condicao, acao),
        )
        conn.commit()
    print(f"Regra para '{condicao}' adicionada com sucesso!")
