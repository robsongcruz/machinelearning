# -*- coding: utf-8 -*-
# pip install psycopg2

import psycopg2

conexao = psycopg2.connect(host="localhost", database="CD", user="postgres", password="12345", port=5432)

cursor = conexao.cursor()

consulta = "XXXXX comando sql "

cursor.execute(consulta)

registros = cursor.fetchall()

cursor.close()

conexao.close()



