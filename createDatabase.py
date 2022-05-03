import sqlite3

conn = sqlite3.connect('database.db')
print("Sucesso")

conn.execute('CREATE TABLE usuarios (email TEXT, nome TEXT, endereco TEXT)')
print("Tabela criada")
conn.close()
