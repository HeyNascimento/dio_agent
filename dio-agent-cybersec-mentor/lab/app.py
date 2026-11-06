"""
LABORATÓRIO - código PROPOSITALMENTE VULNERÁVEL.

Serve apenas para estudar e testar a skill vulnerability-analysis
com um código seu, rodando localmente. Nunca use em produção.
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
    # O SQL é montado juntando o que a pessoa digitou.
    consulta = (
        "SELECT * FROM usuarios "
        f"WHERE usuario = '{usuario}' AND senha = '{senha}'"
    )
    return conn.execute(consulta).fetchone() is not None


if __name__ == "__main__":
    banco = criar_banco()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if login(banco, usuario, senha):
        print("Login realizado com sucesso.")
    else:
        print("Usuário ou senha inválidos.")
