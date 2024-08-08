import psycopg2

conexao = psycopg2.connect(database = "datacamp_courses", user = "datacamp", host = 'localhost', password = "postgresql_tutorial", port = 5432)
cursor