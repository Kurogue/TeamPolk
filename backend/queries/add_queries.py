# This file will handle all the adding of entries to the db. 
# Will deal with mulitple entities and accout for errors
import datetime
import psycopg2
#Add To Vehicle
#error handling version
def add_vehicle(connection, vin, make, model, year, mileage, package_id, audio_id, preform_id, instock, lot, spot):
    cur = connection.cursor()
    try:
        # Check if the vehicle already exists in the database
        find_query = """SELECT VIN FROM Vehicle WHERE VIN = %s;"""
        cur.execute(find_query, (vin,))
        if cur.fetchone() is not None:
            print("Vehicle already exists in the database")
            return False

        # Insert vehicle into Vehicle table
        insert_query = """INSERT INTO Vehicle (VIN, Make, Model, Year, Mileage, Package_ID, Audio_ID, Preform_ID) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
        cur.execute(insert_query, (vin, make, model, year, mileage, package_id, audio_id, preform_id,))
		
        # Add the vehicle to either the Instock or Backorder table
        if instock.lower() == 'yes':
            instock_query = """INSERT INTO Instock (VIN, Date_added, Available, Lot, Spot) VALUES (%s, %s, %s, %s, %s);"""
            date = datetime.date.today()
            cur.execute(instock_query, (vin, date, True, lot, spot,))
            print("Vehicle added to instock")
        else:
            backorder_query = """INSERT INTO Backorder (VIN, Date_added, Available) VALUES (%s, %s, %s);"""
            date = datetime.date.today()
            cur.execute(backorder_query, (vin, date, False))
            print("Vehicle added to backorder")
        connection.commit()  # Commit the changes
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error occurred while adding vehicle to database:", error)
        connection.rollback()  # Rollback the changes if any error occurs
	
def add_hasInterior(connection, vin, int_id):
	cur = connection.cursor()
	add = """INSERT INTO HasInterior (VIN, Interior_id) VALUES (%s, %s);"""
	cur.execute(add, (vin, int_id,))
	connection.commit()
	return True

def add_hasExterior(connection, vin, ext_id):
	cur = connection.cursor()
	add = """INSERT INTO hasExterior (VIN, Exterior_id) VALUES (%s, %s);"""
	cur.execute(add, (vin, ext_id,))
	connection.commit()
	return True

def add_hasSafety(connection, vin, safe_id):
	cur = connection.cursor()
	add = """INSERT INTO hasSafety (VIN, Safety_id) VALUES (%s, %s);"""
	cur.execute(add, (vin, safe_id,))
	connection.commit()
	return True

def add_hasWarranty(connection, vin, warr_no):
	cur = connection.cursor()
	add = """INSERT INTO hasWarranties (VIN, Warranty_no) VALUES (%s, %s);"""
	cur.execute(add, (vin, warr_no,))
	connection.commit()
	return True

def add_hasFeature(connection, vin, feat_id):
	cur = connection.cursor()
	add = """INSERT INTO hasFeatures (VIN, Feature_id) VALUES (%s, %s);"""
	cur.execute(add, (vin, feat_id,))
	connection.commit()
	return True

def add_hasControl(connection, vin, control_id):
	cur = connection.cursor()
	add = """INSERT INTO hasControls (VIN, Control_id) VALUES (%s, %s);"""
	cur.execute(add, (vin, control_id,))
	connection.commit()
	return True

def add_hasMaintenance(connection, vin, main_no):
	cur = connection.cursor()
	add = """INSERT INTO HasMaintence (VIN, Main_no) VALUES (%s, %s);"""
	cur.execute(add, (vin, main_no,))
	connection.commit()
	return True

#Add Interior 
def add_interior(connection, int_id, type_, descript, color):
	cur = connection.cursor()
	find = """SELECT Interior_id FROM Interior WHERE Interior_id = %s;"""
	data = (int_id,)
	cur.execute(find, data)
	print("began looking")
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Interior (Interior_id, Type, Description, Color) VALUES (%s, %s, %s, %s);"""
		data = (int_id, type_, descript, color,)
		cur.execute(add, data)
		connection.commit()
	return True

#Add Package
def add_package(connection, pack_id, name, descript):
	cur = connection.cursor()
	find = """SELECT Package_id FROM Package WHERE Package_id = %s;"""
	data = (pack_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Package (Package_id, Name, Description, Color) VALUES (%s, %s, %s);"""
		data = (pack_id, name, descript,)
		cur.execute(add, data)
		connection.commit()
	return True
#Add Performance 
def add_performance(connection, perform_id, type_, descript):
	cur = connection.cursor()
	find = """SELECT Perform_id FROM Performance WHERE Perform_id = %s;"""
	data = (perform_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Performance (Perform_id, Type, Description) VALUES (%s, %s, %s);"""
		data = (perform_id, type_, descript,)
		cur.execute(add, data)
		connection.commit()
	return True

#Add Safety/Security
def add_safe_security(connection, safety_id, name, descript):
	cur = connection.cursor()
	find = """SELECT Safety_id FROM Safety WHERE Safety_id = %s;"""
	data = (safety_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Safety (Safety_id, Name, Description) VALUES (%s, %s, %s);"""
		data = (safety_id, name, descript,)
		cur.execute(add, data)
		connection.commit()
	return True

#Add Warranty
def add_warranty(connection, w_no, type_, descript):
	cur = connection.cursor()
	find = """SELECT Warranty_no FROM Warranty WHERE Warranty_no = %s;"""
	data = (w_no,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Warranty (Warranty_no, Type, Description) VALUES (%s, %s, %s);"""
		data = (w_no, type_, descript,)
		cur.execute(add, data)
		connection.commit()
	return True
#Add Audio
def add_audio(connection, audio_id, type_, descript):
	cur = connection.cursor()
	find = """SELECT Audio_id FROM Audio WHERE Audio_id = %s;"""
	data = (audio_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Audio (Audio_id, Type, Description) VALUES (%s, %s, %s);"""
		data = (audio_id, type_, descript,)
		cur.execute(add, data)
		connection.commit()
	return True

#Add Comfort Features
def add_features(connection, f_id, name, descript):
	cur = connection.cursor()
	find = """SELECT Feature_id FROM Feature WHERE Feature_id = %s;"""
	data = (f_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Feature (Feature_id, Name, Description) VALUES (%s, %s, %s);"""
		data = (f_id, name, descript,)
		cur.execute(add, data)
		connection.commit()
	return True
#Add Controls
def add_control(connection, control_id, type_, descript):
	cur = connection.cursor()
	find = """SELECT Control_id FROM Control WHERE Control_id = %s;"""
	data = (control_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Control (Control_id, Type, Description) VALUES (%s, %s, %s);"""
		data = (control_id, type_, descript,)
		cur.execute(add, data)
		connection.commit()
	return True

#Add Exterior
def add_exterior(connection, exterior_id, type_, descript, color):
	cur = connection.cursor()
	find = """SELECT Exterior_id FROM Exterior WHERE Exterior_id = %s;"""
	data = (exterior_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Exterior (Exterior_id, Type, Description, Color) VALUES (%s, %s, %s, %s);"""
		data = (exterior_id, type_, descript, color,)
		cur.execute(add, data)
		connection.commit()
	return True

#Add Handling
def add_handling(connection, h_id, type_, descript):
	cur = connection.cursor()
	find = """SELECT Handling_id FROM Handling WHERE Handling_id = %s;"""
	data = (h_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Handling (Handling_id, Type, Description) VALUES (%s, %s, %s);"""
		data = (h_id, type_, descript,)
		cur.execute(add, data)
		connection.commit()
	return True

#Add Maintenance
def add_maintenance(connection, main_no, date_time, service, e_id=None):
	cur = connection.cursor()
	find = """SELECT Main_no FROM Maintenance WHERE Main_no = %s;"""
	data = (main_no,)
	cur.execute(find, data,)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Maintenance (Main_no, Date, Service, Employ_id) VALUES (%s, %s, %s, %s);"""
		data = (main_no, date_time, service, e_id,)
		cur.execute(add, data)
		connection.commit()
	return True

#Add Employee - Maintenance
def add_maintenance_employee(connection, e_id, ssn, fname, lname, start, address):
	cur = connection.cursor()
	find = """SELECT Employ_id FROM Maintence_employ WHERE Employ_id = %s;"""
	data = (e_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Maintence_employ (Employ_id, SSN, Fname, Lname, Date_started, address) VALUES (%s, %s, %s, %s, %s, %s);"""
		data = (e_id, ssn, fname, lname, start, address,)
		cur.execute(add, data)
		connection.commit()
	return True
#Add Employee - Manager
def add_manager_employee(connection, e_id, ssn, fname, lname, start, address):
	cur = connection.cursor()
	find = """SELECT Employ_id FROM Manager WHERE Employ_id = %s;"""
	data = (e_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Manager (Employ_id, SSN, Fname, Lname, Date_started, address) VALUES (%s, %s, %s, %s, %s, %s);"""
		data = (e_id, ssn, fname, lname, start, address,)
		cur.execute(add, data)
		connection.commit()
	return True
#Add Employee - Sales
def add_sales_employee(connection, e_id, ssn, fname, lname, start, address):
	cur = connection.cursor()
	find = """SELECT Employ_id FROM Sales_employ WHERE Employ_id = %s;"""
	data = (e_id,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Sales_employ (Employ_id, SSN, Fname, Lname, Date_started, address) VALUES (%s, %s, %s, %s, %s, %s);"""
		data = (e_id, ssn, fname, lname, start, address,)
		cur.execute(add, data)
		connection.commit()
	return True
#Add Customer
def add_customer(connection, name, address, email, dob, p_no):
	cur = connection.cursor()
	find = """SELECT Name, Email FROM Customer WHERE Name = %s AND Email = %s;"""
	data = (name, email,)
	cur.execute(find, data)
	if cur.fetchone() is not None:
		return False
	else:
		add = """INSERT INTO Customer (Name, Address, Email, DOB, Phone_no) VALUES (%s, %s, %s, %s, %s);"""
		data = (name, address, email, dob, p_no,)
		cur.execute(add, data)
		connection.commit()
	return True
