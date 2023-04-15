# This file will handle all the adding of entries to the db. 
# Will deal with mulitple entities and accout for errors

#Add To Vehicle
def add_vehicle(connection, vin, make, model, year, instock):
	cur = connection.cursor()
	#lookup to make sure the vehicle doesn't exist
	find = """SELECT VIN FROM Vehicle WHERE VIN = (%s);"""
	data = (vin)
	cur.execute(find, data)
	if cur.fetchone() is None:
		#print("Vehicle Already in Table")#Need to print to the window
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
		connection.commit()
	else:
		Backorder = """INSERT INTO Backorder (VIN, Date, Available) VALUES (%s, %s, %s);"""
		date = datetime.date
		values =(vin, date, False)
		cur.execute(instock, values)
		connection.commit()
	return 
#Add Interior 
def add_interior(connection, int_id, type_, descript, color):
	cur = connection.cursor()
	find = """SELECT Interior_id FROM Interior WHERE Interior_id = (%s);"""
	data = (int_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Interior (Interior_id, Type, Description) VALUES (%s, %s, %s, %s);"""
		data = (int_id, type_, descript, color)
		cur.execute(add, data)
		connection.commit()
	return

#Add Package
def add_package(connection, pack_id, name, descript):
	cur = connection.cursor()
	find = """SELECT Package_id FROM package WHERE Package_id = (%s);"""
	data = (pack_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Package (Package_id, Name, Description) VALUES (%s, %s, %s);"""
		data = (pack_id, name, descript)
		cur.execute(add, data)
		connection.commit()
	return
#Add Performance
def add_performance(connection, perform_id, type_, descript):
	cur = connection.cursor()
	find = """SELECT Perform_id FROM Performance WHERE Perform_id = (%s);"""
	data = (perform_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Performance (Perform_id, Type, Description) VALUES (%s, %s, %s);"""
		data = (perform_id, type_, descript)
		cur.execute(add, data)
		connection.commit()
	return

#Add Safety/Security
def add_safe_security(connection, safety_id, name, descript):
	cur = connection.cursor()
	find = """SELECT Safety_id FROM Safety WHERE Safety_id = (%s);"""
	data = (safety_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Safety (Safety_id, Name, Description) VALUES (%s, %s, %s);"""
		data = (safety_id, name, descript)
		cur.execute(add, data)
		connection.commit()
	return

#Add Warranty
def add_warranty(connection, w_no, type_, descript):
	cur = connection.cursor()
	find = """SELECT Warranty_no FROM Warranty WHERE Warranty_no = (%s);"""
	data = (w_no)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Warranty (Warranty_no, Type, Description) VALUES (%s, %s, %s);"""
		data = (w_no, type_, descript)
		cur.execute(add, data)
		connection.commit()
	return
#Add Audio
def add_audio(connection, audio_id, type_, descript):
	cur = connection.cursor()
	find = """SELECT Audio_id FROM Audio WHERE Audio_id = (%s);"""
	data = (audio_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Audio (Audio_id, Type, Description) VALUES (%s, %s, %s);"""
		data = (int_id, type_, descript)
		cur.execute(add, data)
		connection.commit()
	return

#Add Comfort Features
def add_features(connection, f_id, name, descript):
	cur = connection.cursor()
	find = """SELECT Feature_id FROM Feature WHERE Feature_id = (%s);"""
	data = (f_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Feature (Feature_id, Name, Description) VALUES (%s, %s, %s);"""
		data = (f_id, name, descript)
		cur.execute(add, data)
		connection.commit()
	return

#Add Exterior
def add_exterior(connection, exterior_id, type_, description, color):
    query = """
    INSERT INTO Exterior (Exterior_id, Type, Description, Color)
    VALUES (%s, %s, %s, %s);
    """
    data = (exterior_id, type_, description, color)
    execute_query(connection, query, data)
    return
def add_exterior(connection, exterior_id, type_, descript, color):
	cur = connection.cursor()
	find = """SELECT Exterior_id FROM Exterior WHERE Exterior_id = (%s);"""
	data = (exterior_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Exterior (Exterior_id, Type, Description, Color) VALUES (%s, %s, %s, %s);"""
		data = (exterior_id, type_, descript, color)
		cur.execute(add, data)
		connection.commit()
	return

#Add Handling
def add_handling(connection, h_id, type_, descript):
	cur = connection.cursor()
	find = """SELECT Handling_id FROM Handling WHERE Handling_id = (%s);"""
	data = (h_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Handling (Handling_id, Type, Description) VALUES (%s, %s, %s);"""
		data = (h_id, type_, descript)
		cur.execute(add, data)
		connection.commit()
	return
#Add Maintenance
def add_maintenance(connection, main_no, date_time, service, e_id=None):
	cur = connection.cursor()
	find = """SELECT Main_no FROM Maintenance WHERE Main_no = (%s);"""
	data = (main_no)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Maintenance (Main_no, Date, Service, Employ_id) VALUES (%s, %s, %s, %s);"""
		data = (main_no, date_time, service, e_id)
		cur.execute(add, data)
		connection.commit()
	return
#Add Employee - Maintenance
def add_maintenance_employee(connection, e_id, ssn, fname, lname, start, address):
	cur = connection.cursor()
	find = """SELECT Employ_id FROM Maintence_employ WHERE Employ_id = (%s);"""
	data = (e_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Maintence_employ (Employ_id, SSN, Fname, Lname, Date_started, address) VALUES (%s, %s, %s, %s, %s, %s);"""
		data = (e_id, ssn, fname, lname, start, address)
		cur.execute(add, data)
		connection.commit()
	return
#Add Employee - Manager
def add_manager_employee(connection, e_id, ssn, fname, lname, start, address):
	cur = connection.cursor()
	find = """SELECT Employ_id FROM Manager WHERE Employ_id = (%s);"""
	data = (e_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Manager (Employ_id, SSN, Fname, Lname, Date_started, address) VALUES (%s, %s, %s, %s, %s, %s);"""
		data = (e_id, ssn, fname, lname, start, address)
		cur.execute(add, data)
		connection.commit()
	return
#Add Employee - Sales
def add_sales_employee(connection, e_id, ssn, fname, lname, start, address):
	cur = connection.cursor()
	find = """SELECT Employ_id FROM Sales_employ WHERE Employ_id = (%s);"""
	data = (e_id)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Sales_employ (Employ_id, SSN, Fname, Lname, Date_started, address) VALUES (%s, %s, %s, %s, %s, %s);"""
		data = (e_id, ssn, fname, lname, start, address)
		cur.execute(add, data)
		connection.commit()
	return
#Add Customer
def add_customer(connection, name, address, email, dob, p_no):
	cur = connection.cursor()
	find = """SELECT Name, Email FROM Customer WHERE Name = (%s) AND Email = (%s);"""
	data = (name, email)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		add = """INSERT INTO Customer (Name, Address, Email, DOB, Phone_no) VALUES (%s, %s, %s, %s, %s);"""
		data = (name, address, email, dob, p_no)
		cur.execute(add, data)
		connection.commit()
	return