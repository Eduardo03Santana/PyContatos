import sqlite3
from Contatos import Contato
from time import sleep

class BD:
    def __init__(self):
        self.con = ''
        self.conStatus = False
        self.cursor = ''
    def abrirConexao(self):
        try:
            self.con = sqlite3.connect('file:banco.db?mode=rw', uri=True) # Se nao existe banco devolve uma Exception
        except Exception as err:
            #print(err)
            self.con = sqlite3.connect("banco.db") # Cria O Banco
            self.cursor = self.con.cursor()
            self.criarTabela() # Cria Tabela
        self.cursor = self.con.cursor()
    def fecharConexao(self):
        self.con.close()
        self.cursor = ''
    def criarTabela(self):
        self.cursor.execute("""CREATE TABLE tblContatos (

id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
Nome VARCHAR(255) NOT NULL,
Numero VARCHAR(255) NOT NULL,
Email VARCHAR(255)
);""")
        self.con.commit()

    def criarContato(self, contato): # Espera receber um obj da class contato
        try:
            if contato.nome == '' or contato.numero == '': raise Exception("Nome e numero nao podem ser vazios")
            self.cursor.execute(f"INSERT INTO tblContatos (Nome, Numero, Email) VALUES ('{contato.nome}', '{contato.numero}', '{contato.email}')")
            self.con.commit()
        except Exception as err:
            #print(err)
            return False
        return True


    def readAllContatos(self):
        return [Contato(str(x[1]), str(x[2]), str(x[3]), str(x[0])) for x in self.cursor.execute(f"SELECT * FROM tblContatos").fetchall()]
    
    def readContatoById(self, iD):
        return [Contato(str(x[1]), str(x[2]), str(x[3]), str(x[0])) for x in self.cursor.execute(f"SELECT * FROM tblContatos WHERE id = {iD}").fetchall()][0] if self.cursor.execute(f"SELECT * FROM tblContatos WHERE id = {iD}").fetchall() else False
        

    def updateContato(self, contato): # Espera receber um obj da class contato
        try:
            self.cursor.execute(f"update tblContatos set Nome ='{contato.nome}', Numero = '{contato.numero}', Email = '{contato.email}' where id = '{contato.id}'")
            self.con.commit()
        except Exception as err:
            #print(err)
            return False
        return True


    def deleteContato(self, contato): # Espera receber um obj da class contato
        try:
            self.cursor.execute(f"DELETE FROM tblContatos where id = '{contato.id}'")
            self.con.commit()
        except Exception as err:
            #print(err)
            return False
        return True




            
                    



            
        
        
    


    
        
