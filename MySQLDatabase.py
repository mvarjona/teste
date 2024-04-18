import mysql.connector as myconn
from dotenv import load_dotenv
import os

load_dotenv()


class MySQLDatabase:

    def __init__(self):
        self._host = os.getenv("HOST")
        self._username = os.getenv("USERNAME")
        self._passwd = os.getenv("PASSWD")
        self._database = os.getenv("DATABASE")
        
    def _conecta(self):
        self.conn = myconn.connect(
            user="root",
            password="1234",
            host="localhost",
            database="trends"
            
        )
        self.cursor = self.conn.cursor();
    
    def desconecta(self):
       if(self.conn.is_connected):
           self.conn.close()
    
    def executa_DQL(self, sql):
        self._conecta();
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.desconecta();
        return res
    
    def executa_DML(self, sql):
        self._conecta();
        print(sql);
        self.cursor.execute(sql)
        self.conn.commit()
        self.desconecta();
      
    