import sqlite3
import os

CAMINHO_DB = os.path.join(os.path.dirname(__file__), "rotina.db")


def obter_conexao():
    return sqlite3.connect(CAMINHO_DB)


def inicializar_banco():
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL DEFAULT 'geral',
                hora TEXT NOT NULL,
                dias_semana TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'ativa'
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS regras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                condicao TEXT NOT NULL,
                acao TEXT NOT NULL,
                ativa INTEGER NOT NULL DEFAULT 1
            )
            """
        )
        conn.commit()
