from MySQLDatabase import MySQLDatabase


def __init__(self, id = None, nome = None):
        self.id
        self.nome

def incluir(nome):
        c = MySQLDatabase()
        sql = f'Insert Into usuario(nome) Values("{nome}")'
        c.executa_DML(sql)