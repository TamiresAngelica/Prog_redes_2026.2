import sqlite3

conexao = sqlite3.connect("monitoramento.db")
print("conexão estabelecida")
conexao.close()