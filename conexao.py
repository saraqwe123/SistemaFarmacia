import psycopg2

bdNome = ""
senha = ""
usuario = ""
host = ""

conexao = psycopg2(bdNome, senha, usuario, host)
