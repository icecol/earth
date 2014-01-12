from flask import flash, session, redirect, url_for, escape, request, render_template
import pymongo
import os
from vsdcar import app
from flask_wtf import Form
from wtforms import TextField, IntegerField, FileField
from bson.objectid import ObjectId

#segredo para controle de sessao
app.secret_key = os.urandom(24)

#formulario de busca/filtro
class BuscaForm(Form):
    fabricante = TextField('Fabricante')
    modelo = TextField('Modelo')
    ano = IntegerField('Ano')

#formulario de Edicao/insercao de carros
class EditForm(Form):
    fabricante = TextField('Fabricante')
    modelo = TextField('Modelo')
    ano = IntegerField('Ano')
    foto = FileField('Foto')

def busca_registros(filtros={}):
    #conecta ao mongodb local
    client = pymongo.MongoClient('localhost', 27017)
    #define a base utilizada
    db = client.carscrud
    if filtros == {} or filtros == {'ano': 'None', 'modelo': '', 'fabricante': ''}: 
        #busca todos registros na base e coloca em uma lista
    	registros = db.cars.find()
	cars_list = []
        for i in registros:
            # "decodifica" unicode retornado pelo mongodb
            cars_list.append(dict([(str(k), str(v)) for k, v in i.items()]))
	return cars_list
    # busca apenas carros que combinem com os filtros
    dict_filtro={}
    if filtros['fabricante'] != '':
	dict_filtro['fabricante_lower']=filtros['fabricante']
    if filtros['modelo'] != '':
	dict_filtro['modelo_lower']=filtros['modelo']
    if filtros['ano'] != 'None':
        dict_filtro['ano']=filtros['ano']
    registros = db.cars.find(dict_filtro) # 'modelo_lower':filtros['modelo']})
    cars_list = []
    for i in registros:
        # "decodifica" unicode retornado pelo mongodb
        cars_list.append(dict([(str(k), str(v)) for k, v in i.items()]))
    return cars_list


@app.route('/', methods=['GET','POST'])
def index():
    carros = busca_registros()
    form = BuscaForm(request.form)
    if request.method == 'POST':
	#resultados da busca
	fabricante = str(form.fabricante.data).lower()
        modelo = str(form.modelo.data).lower()
        ano = str(form.ano.data)
        filtros = {'fabricante':fabricante , 'modelo':modelo , 'ano':ano}
	carros = busca_registros(filtros)
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

@app.route('/admin', methods=['GET','POST'])
def admin():
    if not 'username' in session:
	return redirect(url_for('login'))
    form = EditForm(request.form)
    carro = {}
    car = request.args.get('car','')
    if car:
	#conecta ao mongodb local
        client = pymongo.MongoClient('localhost', 27017)
        #define a base utilizada
        db = client.carscrud
	carro = db.cars.find_one({"_id":ObjectId(car)})
    if request.method == 'POST':
	# testar se o usuario quer Salvar ou Excluir o registro
	carro = {'ano': str(form.ano.data),
           	 'fabricante': str(form.fabricante.data),
           	 'modelo': str(form.modelo.data),
	         'fabricante_lower': str(form.fabricante.data).lower(),
	         'modelo_lower': str(form.modelo.data).lower(),
	         'foto': str(form.foto.data)}
	print(carro)
    # Edita , adiciona ou remove carro da base
    return render_template('admin.html', username=escape(session['username']), carro=carro)

