from datetime import datetime
from Database import *
import csv
from MySqlConn import *


class Chiulangii():
    def __init__(self):
        self.db=MySqlConn



def afisare_chiulangii(self):
    query=""
    self.db.cursor.execute(query)
    results=self.db.cursor.fetchfall()
    self.db.connection.commit()
    return results
    print(query)