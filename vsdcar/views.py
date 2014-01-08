from flask import flash, session, redirect, url_for, escape, request, render_template
import pymongo
import os
from vsdcar import app

app.secret_key = os.urandom(24)

def busca_registros(filtros={}):
    #conecta ao mongodb local
    client = pymongo.MongoClient('localhost', 27017)
    #define a base utilizada
    db = client.carscrud
    if filtros == {}:
        #busca todos registros na base e coloca em uma lista
    	registros = db.cars.find()
	cars_list = []
        for i in registros:
            # "decodifica" unicode retornado pelo mongodb
            cars_list.append(dict([(str(k), str(v)) for k, v in i.items()]))
	return cars_list
    return []


@app.route('/')
def index():
    carros = busca_registros()
    if request.method == 'POST' and form.validate():
	#resultados da busca
	fabricante = search_fields['Fabricante'].value
        modelo = search_fields['Modelo'].value
        ano = search_fields['Ano'].value
        filtros = {'Fabricante':fabricante , 'Modelo':modelo , 'Ano':ano}

    if 'username' in session:
        return render_template('index.html', entries=carros, username=escape(session['username']))
    return render_template('index.html', entries=carros)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
	if request.form['username'] == request.form['password']:
            session['username'] = request.form['username']
   	    session['logged_in'] = True
	    flash('Logado com sucesso, '+session['username'])
            return redirect(url_for('index'))
	else:
	    error = 'usuario ou senha incorretos'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    # remove o nome do usuario da sessao, se estiver la
    session.pop('username', None)
    session['logged_in'] = False
    flash('Logout com sucesso')
    return redirect(url_for('index'))
