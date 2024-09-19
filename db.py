class Database():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='root2024#',
            database='employees',
        )
        self.cursor=self.connection.cursor()
        
    def add_user(self,id_angajat,nume,prenume,companie,id_manager):
        query=f'INSERT INTO employees.users VALUES (%s, %s, %s, %s, %s);'
        values=(id_angajat,nume,prenume,companie,id_manager)
        self.cursor.execute(query,values)
        self.connection.commit()
        return "Am adaugat utilizatorul!"

    def acces(self,Poarta,id_angajat,Data,Sens):
        query=f'INSERT INTO employees.access VALUES (%s, %s, %s, %s, %s);'
        values=(Poarta,id_angajat,Data,Sens)
        self.cursor.execute(query,values)
        self.connection.commit()
    
    def close(self):
        self.cursor.close()
        self.connection.close()
