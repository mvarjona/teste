from MySQLDatabase import MySQLDatabase
from datetime import datetime


def incluir(nome, valor):
        c = MySQLDatabase()
        sql = f'select id from moeda where moedaCorrente = "{nome}"'
        id = c.executa_DQL(sql)
        id_moeda = int(id[0][0])
        dataAtual = datetime.now()
        sql = f'Insert Into valor(tempo, valor, id_moeda) Values("{dataAtual}", {valor}, {id_moeda})'
        c.executa_DML(sql)