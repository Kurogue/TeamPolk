# python code to add values to tables
#  Author: Albert Rosa
#   U#: 41681484 
import tkinter as tk
import psycopg2
import datetime

def add_vehicle(connection, vin, make, model, year, instock):
	cur = connection.cursor()
	#lookup to make sure the vehicle doesn't exist
	find = """SELECT VIN FROM Vehicle WHERE VIN = %s;"""
	data = (vin, )
	cur.execute(find, data)
	if cur.fetchone() is None:
		print("Vehicle Already in Table")
		return
	else:
		add = """INSERT INTO Vehicle (VIN, Make, Model, Year) VALUES (%s, %s, %s, %s);"""
		car_values = (vin, make, model, year)
		cur.execute(add, car_values)
	#add to either the instock list or back order
	if instock == 1:
		instock = """INSERT INTO Instock (VIN, Date, Available) VALUES (%s, %s, %s);"""
		date = datetime.date
		values =(vin, date, True)
		cur.execute(instock, values)
	else:
		Backorder = """INSERT INTO Backorder (VIN, Date, Available) VALUES (%s, %s, %s);"""
		date = datetime.date
		values =(vin, date, False)
		cur.execute(instock, values)
	connection.commit()
	return 

def find_vehicle(connection, vin):
	cur = connection.cursor()
	#look up vehicle
	vin = ""
	make = ""
	model = ""
	year = ""
	find ="""SELECT * FROM Vehicle WHERE VIN = %s;"""
	attr = (vin, )
	cur.execute(find, attr)
	return cur.fetchone()

def find_all_vehicles(connection):
	cur = connection.cursor()
	find = """SELECT * FROM Vehicle"""
	cur.execute(find)
	return cur.fetchall()

def find_Instock(connection, vin):
	cur = connection.cursor()
	find = """SELECT * FROM Instock WHERE VIN = %s;"""
	value = (vin,)
	cur.execute(find, value)
	return cur.fetchone()

def find_BackOrder(connection, vin):
	cur = connection.cursor()
	find = """SELECT * FROM BackOrder WHERE VIN = %s;"""
	value = (vin,)
	cur.execute(find, value)
	return cur.fetchone()

def delete_vehicle(connection, vin):
	cur = connection.cursor()
	delete = """DELETE FROM Vehicle WHERE VIN = %s;
	"""
	value = (vin, )
	cur.execute(delete, value)

	cur.commit()
	return

def check_inStock(connection):
	cur = connection.cursor()
	getStock ="""SELECT * FROM Instock"""
	cur.execute(getStock)
	return cur.fetchall()

def check_backorder(connection):
	cur = connection.cursor()
	getBackOrder = """SELECT * FROM BackOrder"""
	cur.execute(getBackOrder)
	return cur.fetchall()