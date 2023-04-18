# python code to add values to tables
#  Author: Albert Rosa
#   U#: 41681484 
import tkinter as tk
import psycopg2
import datetime

def add_vehicle(connection, vin, make, model, year, instock):
    cur = connection.cursor()
    try:
        #lookup to make sure the vehicle doesn't exist
        find = """SELECT VIN FROM Vehicle WHERE VIN = %s;"""
        data = (vin, )
        cur.execute(find, data)
        if cur.fetchone() is not None:
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
    except (Exception, psycopg2.Error) as error:
        print("Error while adding vehicle to database", error)
        connection.rollback()
    finally:
        cur.close()
        return 
 

def find_vehicle(connection, vin):
	cur = connection.cursor()
	#look up vehicle
	find ="""SELECT * FROM Vehicle WHERE VIN = %s;"""
	attr = (vin, )
	cur.execute(find, attr)
	return cur.fetchone()

def find_all_vehicles(connection, make=None, model=None, year=None):
	cur = connection.cursor()
	if make is None and model is None and year is None:
		find = """SELECT * FROM Vehicle"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Vehicle WHERE Make = %s OR Model = %s OR year = %s"""
		attr = (make, model, year)
		cur.execute(find, attr)
		return cur.fetchall()

def find_Instock(connection, vin=None):
	cur = connection.cursor()
	if vin is None:
		find = """SELECT * FROM Vehicle"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Instock WHERE VIN = %s;"""
		value = (vin,)
		cur.execute(find, value)
		return cur.fetchone()

def find_BackOrder(connection, vin=None):
	cur = connection.cursor()
	if vin is None:
		find = """SELECT * FROM BackOrder"""
		cur.execute(find)
		return cur.fetchall()
	else:
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