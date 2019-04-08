import sqlite3
from time import sleep as sl
connection = sqlite3.connect('assist.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS gastos(nome text, valor real)')
    c.execute('CREATE TABLE IF NOT EXISTS receitas(nome text, valor real)')
    return True

def insert_gastos(nome,valor):
    c.execute("INSERT INTO gastos(nome,valor) VALUES(?,?)",(nome,valor))
    connection.commit()
    return True
    
def insert_receitas(nome,valor):
    c.execute('INSERT INTO receitas(nome,valor) VALUES(?,?)',(nome,valor))
    connection.commit()
    return True

def ler_gastos():
    sql = 'SELECT * FROM gastos'
    itens=[]
    for linha in c.execute(sql):
        itens.append(linha)
    return itens

def ler_receitas():
    sql = 'SELECT * FROM receitas'
    itens=[]
    for linha in c.execute(sql):
        itens.append(linha)
    return itens
