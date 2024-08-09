import psycopg2

conexao = psycopg2.connect(host = "localhost", bdNome = "SistemaFarmacia", senha = "natipedro14", usuario = "postgres", porta = "5432")

def cursor():
    conexao.cursor()

def commit():
    conexao.commit()

def close():
    conexao.close()

