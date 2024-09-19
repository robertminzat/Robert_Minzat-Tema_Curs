import os
import time
import shutil
import csv
import MySqlConn

# entries = 'A_Tema_Curs/entries'
# print(os.path.abspath(entries))


class access_gate():

    def __init__(self, entries = 'A_Tema_Curs/entries', backup = 'A_Tema_Curs/backup'):
        self.entries = os.path.abspath(entries)
        self.backup = os.path.abspath(backup)
        self.db = db()



    def new_file(self):
        while True:
            files = os.listdir(self.entries)
            for file in files:
                if file.startswith('gate') and file.endswith('.csv'):
                    gate_id = self.gate_number(file)
                    self.file_processing('file', 'gate_id')
                    self.move_to_backup(file)
                if file.startswith('gate') and file.endswith('.txt'):
                    gate_id = self.gate_number(file)
                    self.file_processing(file, gate_id)
                    self.move_to_backup(file)
            time.sleep(30)


    def file_processing(self,file, gate_id):
        file_path = os.path.join(self.entries, file)
        print(f"File processing: {file_path}")
        if file.endswith('.csv'):





    def gate_number(self, file):
        return int(file.split('gate')[1].split('.')[0])




    def move_to_backup(self,file):
        intrari=os.path.join(self.entries,file)
        backup=os.path.join(self.backup,file)
        shutil.move(intrari,backup)
        




    