#!/usr/bin/python

#Script de inicializcao da base de dados.
#Limpa e Insere registros de teste na base.
#27/12/2013

import pymongo

#conecta ao mongodb local
client = pymongo.MongoClient('localhost', 27017)
#define a base utilizada
db = client.carscrud
#limpa registros
db.drop_collection('cars')
#define a collection
cars = db.cars


#item a ser adicionado
fabricante = 'GM'
modelo = 'Vectra GT'
new_car = {'ano': 2009,
	   'fabricante': fabricante,
	   'modelo': modelo,
	   'fabricante_lower': fabricante.lower(),
	   'modelo_lower': modelo.lower(),
	   'foto': 'fotoVectra.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'VW'
modelo = 'GOL'
new_car = {'ano': '2010',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoGol.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Ford'
modelo = 'Focus'
new_car = {'ano': '2011',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoFocus.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'GM'
modelo = 'Cruze'
new_car = {'ano': '2012',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoCruze.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Ford'
modelo = 'Fusion'
new_car = {'ano': '2013',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoFusion.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Ford'
modelo = 'Ecosport'
new_car = {'ano': '2013',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoEco01.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Ford'
modelo = 'Fusion'
new_car = {'ano': '2012',
  	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoEco02.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Honda'
modelo = 'Civic'
new_car = {'ano': '2011',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoCivic.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Honda'
modelo = 'Fit'
new_car = {'ano': '2011',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoFit.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Ford'
modelo = 'Focus'
new_car = {'ano': '2012',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoFocus.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Ford'
modelo = 'Ecosport'
new_car = {'ano': '2013',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoEcoo.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'VW'
modelo = 'Golf'
new_car = {'ano': '2014',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoGolf.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'VW'
modelo = 'Golf'
new_car = {'ano': '2010',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoGolff.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'GM'
modelo = 'Sonic'
new_car = {'ano': '2013',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoSonic.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Ford'
modelo = 'Focus'
new_car = {'ano': '2010',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoFoocus.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Honda'
modelo = 'City'
new_car = {'ano': '2011',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoCity.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Ford'
modelo = 'Fiesta'
new_car = {'ano': '2009',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoFFiesta.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Ford'
modelo = 'Fiesta'
new_car = {'ano': '2010',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoFFiiesta.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Nissan'
modelo = 'Tiida'
new_car = {'ano': '2012',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoTiida.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Nissan'
modelo = 'Versa'
new_car = {'ano': '2011',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoVersa.jpg'}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
fabricante = 'Ford'
modelo = 'Fiesta'
new_car = {'ano': '2009',
	   'fabricante': fabricante,
           'modelo': modelo,
           'fabricante_lower': fabricante.lower(),
           'modelo_lower': modelo.lower(),
	   'foto': 'fotoFFiesta.jpg'}
#insere novo item
car_id = cars.insert(new_car)

