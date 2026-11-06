"""
LABORATÓRIO - versão corrigida do app.py.

Troca a concatenação de texto por consulta parametrizada.
Pendência proposital: a senha continua em texto puro no banco
(ponto para uma segunda rodada de análise com o agente).
"""
import sqlite3


def criar_banco():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT)"
    )
    conn.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES ('admin', 'senha-de-laboratorio')"
    )
    conn.commit()
    return conn


def login(conn, usuario, senha):
    # Os valores vão separados do comando e são tratados sempre como dado.
    consulta = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"
    return conn.execute(consulta, (usuario, senha)).fetchone() is not None


if __name__ == "__main__":
    banco = criar_banco()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if login(banco, usuario, senha):
        print("Login realizado com sucesso.")
    else:
        print("Usuário ou senha inválidos.")
