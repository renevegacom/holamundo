#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.pythondiario.com/2013/12/python-y-sqlite3-como-base-de-datos.html

import sqlite3

con = sqlite3.connect('C:\Python27\pruebas\prueba')
#coneccion = sqlite3.connect(':memory:')

cursor = con.cursor()

print u"La base de datos se abrio correctamente"

cursor.execute( ''' CREATE TABLE EMPRESA
        (ID INT PRIMARY KEY       NOT NULL,
         NOMBRE         TEXT	  NOT NULL,
         EDAD           INT       NOT NULL,
         DIRECCION      CHART(50),
		 SALARIO        REAL)''')

print u"Tabla creada con exito"












