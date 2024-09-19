import mysql.connector

class MySqlConn():
    def __init__(self):
        self.mydb=mysql.connector.connect(host='localhost',
                                          user='root',
                                          password='root2024#',
                                          database='employees')
        self.cursor=self.mydb.cursor()

    def select(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self,query):
        self.cursor.execute(query)
        self.mydb.commit()

    def update(self,query):
        self.cursor.execute(query)
        self.mydb.commit()
    
    def acces(self,Poarta,id_angajat,Data,Sens):
        query=f'INSERT INTO employees.access VALUES (%s, %s, %s, %s, %s);'
        values=(Poarta,id_angajat,Data,Sens)
        self.cursor.execute(query,values)
        self.connection.commit()
    
    def close(self):
        self.cursor.close()
        self.connection.close()


