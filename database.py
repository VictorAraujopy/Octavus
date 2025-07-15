import sqlite3
from datetime import datetime

def conect():
    conn = sqlite3.connect('octavus.db')
    return conn

def tabela():
    conn = conect()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mensagens_whats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        destinatario TEXT,
        numero TEXT,
        mensagem TEXT,
        data_envio TEXT 
                   
                   )               
                   
                  ''' )
    
    conn.commit()
    conn.close()


def registrar(destinatario, numero, mensagem):


    conn = conect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mensagens_whats (destinatario, numero, mensagem, data_envio) VALUES (?, ?, ?, ? )",
                   (destinatario, numero, mensagem, datetime.now().isoformat()))
    
    conn.commit()
    conn.close()
                    
