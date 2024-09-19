from inregistrare_intrari import *
from db import Database
from chiulangii import Chiulangii
from flask import Flask,request,render_template
import time
import threading
from send_email import *
from MySqlConn import *
import os

app=Flask(__name__)
mysqlConn=MySqlConn()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add')
def adaugareUtilizator():
    return render_template('insert.html')

@app.route('/utilizator',methods=['POST'])
def adaugare_utilizator():
    inputs=request.form
    query=f"employees.users VALUES (null,'{inputs['id_angajat']}', \
                                              '{inputs['Nume']}', \
                                              {inputs['Prenume']}, \
                                              {inputs['Companie']}, \
                                              '{inputs['id_manager']}')" 
    mysqlConn.insert(query)
    return 'Utilizator adaugat!'

@app.route('/access',methods=['POST'])
def json():
    sql=request.get_json()
    id_angajat=sql.get('id_angajat')
    Data=sql.get('Data')
    Poarta=sql.get('Poarta')
    Sens=sql.get('Sens')
    user=mysqlConn()
    user.acces(Poarta,id_angajat,Data,Sens)
    return json.dumps(sql)

