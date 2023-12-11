import sqlite3

class Database:
    def init(self):
        conn = sqlite3.connect("estrela.db")
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS dim_taxi_zones (id PRIMARY KEY, distrito VARCHAR, zona VARCHAR, zona_servico VARCHAR);")
        cursor.execute("CREATE TABLE IF NOT EXISTS dim_rate_code  (id PRIMARY KEY, descricao VARCHAR);")
        cursor.execute("CREATE TABLE IF NOT EXISTS dim_payment  (id PRIMARY KEY, descricao VARCHAR);")

        conn.commit()
        conn.close()
    def runQuery(self, query):
        conn = sqlite3.connect("estrela.db")
        cursor = conn.cursor()

        cursor.execute(query)

        conn.commit()
        conn.close()