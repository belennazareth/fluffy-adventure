import os
import sys
import psycopg2 
from flask import Flask, render_template, request,abort

app = Flask(__name__)

##########################################################################

@app.route('/')
def init():
    return render_template("inicio.html")

@app.route('/consulta',methods=["POST"])
def sesion():
    
    user = request.form['usuario']
    passwd = request.form['contra']
   
    while True:
        
        try:

            connection = psycopg2.connect(
                host = "192.168.122.9",
                database = "inter2",
                user = user,
                password = passwd)

            cursor = connection.cursor()
            cursor.execute("select deptno from emp")
            row = cursor.fetchall()        
            return (str(row))

        except psycopg2.DatabaseError:
            return ("(ノ°益°)ノ EL USUARIO TA HORRIBLE BOLUDO ٩(╬ʘ益ʘ╬)۶ NO EXISTE WACHO (°ㅂ°╬)")
    
    return(row)

##########################################################################

#webserver

if __name__ == '__main__':

    app.run (port = int(os.environ.get('PORT', '8080'))) 