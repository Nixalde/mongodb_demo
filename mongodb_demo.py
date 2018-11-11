# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
import pymongo
from pymongo import MongoClient
import os
app = Flask(__name__)

@app.route('/')
def index(query=None):
	return render_template('Index.html',query=query)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method=="POST":
		db_usuario = request.form['name']
		db_pass = request.form['pass']
		db_base = request.form['Base']
		db_coleccion = request.form['Coleccion']
		myclient = MongoClient('mongodb://172.22.200.178:27017/')
#		Este es el metodo de autentificacion por usuario
#		pero no consigue autenticar en el servidor.
#		myclient = MongoClient('mongodb://%s:%s@172.22.200.178:27017/' % (db_usuario,db_pass))
		mydb = myclient[db_base]
		mycol = mydb[db_coleccion]
		query = mycol.find({})
		if query == None:
			error="No es posible realizar la conexión."
			return render_template("Index.html",query=None)
		else:
			return render_template("Index.html",query=query)
	else:
		return render_template("Index.html")

app.run('0.0.0.0', port=8080, debug=False)
