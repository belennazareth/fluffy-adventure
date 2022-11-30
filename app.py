import os
import sys
import psycopg2 
from flask import Flask, render_template, request,abort

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/consulta',methods=["POST"])
def iniciosesion():
    usuario=request.form['usuario']
    contra=request.form['contra']
    #while True:
        #try:
    connection = psycopg2.connect(
        host="192.168.122.9",
        database="inter2",
        user=usuario,
        password=contra)
    cursor = connection.cursor()
    cursor.execute("select deptno from emp")
    res = cursor.fetchall()        
    return (str(res))
        #except psycopg2.DatabaseError:
        #    return ("Error en el usuario :(")
    

    #return(res)


#webserver

if __name__ == '__main__':

    app.run(port=int(os.environ.get('PORT', '8080'))) 