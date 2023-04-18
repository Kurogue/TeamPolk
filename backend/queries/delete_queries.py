#This file will handle the deletion of entries or relationships from the database
#Will have to account for the various many to one Or many to many relationships that may need to be checked

#Delete Vehicle
def delete_vehicle(connection, vin):
	cur = connection.cursor()
	#lookup to make sure the vehicle doesn't exist
	find = """SELECT VIN FROM Vehicle WHERE VIN = %s;"""
	data = (vin,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		#print("Vehicle Not in Table")#Need to print to the window
		return
	else:
		delete_hasInterior(connection, vin)
		delete_hasExterior(connection, vin)
		delete_hasFeature(connection, vin)
		delete_hasSafety(connection, vin)
		delete_hasWarranty(connection, vin)
		delete_hasMaintenance(connection, vin)
		add = """DELETE FROM Vehicle WHERE VIN = %s;"""
		car_values = (vin,)
		cur.execute(add, car_values)
		connection.commit()
	#check the instock or backorder to remove those too
	find_instock = """SELECT VIN FROM Instock WHERE VIN = %s;"""
	cur.execute(find_instock, data)
	if cur.fetchone() is not None:
		del_instock = """DELETE FROM Instock WHERE VIN = %s;"""
		values = (vin,)
		cur.execute(instock, values)
		connection.commit()
	find_backorder = """ SELECT VIN FROM Backorder WHERE VIN = %s;"""
	cur.execute(find_backorder, data)
	if cur.fetchone() is not None:
		backorder = """DELETE FROM Backorder WHERE VIN = %s;"""
		values =(vin,)
		cur.execute(backorder, values)
		connection.commit()
	return 
def delete_hasInterior(connection, vin):
	cur = connection.cursor()
	find = """SELECT * FROM hasInterior WHERE VIN = %s"""
	cur.execute(find, (vin,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM HasInterior WHERE VIN = %s;"""
		cur.execute(delete, (vin,))
		connection.commit()
		return

def delete_hasExterior(connection, vin):
	cur = connection.cursor()
	find = """SELECT * FROM hasExterior WHERE VIN = %s"""
	cur.execute(find, (vin,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM HasExterior WHERE VIN = %s;"""
		cur.execute(delete, (vin,))
		connection.commit()
		return

def delete_hasSafety(connection, vin):
	cur = connection.cursor()
	find = """SELECT * FROM hasSafety WHERE VIN = %s"""
	cur.execute(find, (vin,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM HasSafety WHERE VIN = %s;"""
		cur.execute(delete, (vin,))
		connection.commit()
		return

def delete_hasWarranty(connection, vin):
	cur = connection.cursor()
	find = """SELECT * FROM hasWarranties WHERE VIN = %s"""
	cur.execute(find, (vin,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM hasWarranties Where VIN = %s;"""
		cur.execute(delete, (vin,))
		connection.commit()
		return

def delete_hasFeature(connection, vin):
	cur = connection.cursor()
	find = """SELECT * FROM hasFeatures WHERE VIN = %s"""
	cur.execute(find, (vin,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM hasFeatures WHERE VIN = %s;"""
		cur.execute(delete, (vin,))
		connection.commit()
		return

def delete_hasMaintenance(connection, vin):
	cur = connection.cursor()
	find = """SELECT * FROM hasMaintence WHERE VIN = %s"""
	cur.execute(find, (vin,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM hasMaintence WHERE VIN = %s;"""
		cur.execute(delete, (vin,))
		connection.commit()
		return
#Delete Interior ###HasInterior
def delete_interior(connection, int_id, type_):
	cur = connection.cursor()
	find = """SELECT Interior_id FROM Interior WHERE Interior_id = %s;"""
	data = (int_id,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Interior WHERE Interior_id = %s AND Type = %s;"""
		del_data = (int_id, type_,)
		cur.execute(delete, del_data)
		#Find the HasInterior Table
		find_Has = """SELECT Interior_id FROM HasInterior WHERE Interior_id = %s;"""
		cur.execute(find_Has, data)
		#If any found then delete all that have the same interior id
		if cur.fetchone() is not None:
			delete_has = """DELETE FROM HasInterior WHERE Interior_id = %s"""
			cur.execute(delete_has, data)
		connection.commit()
	return
#Delete Package 
def delete_package(connection, pack_id, name):
	cur = connection.cursor()
	find = """SELECT Package_id FROM Package WHERE Package_id = %s;"""
	data = (pack_id,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Package WHERE Package_id = %s AND Name = %s;"""
		data = (pack_id, name,)
		cur.execute(delete, data)
		connection.commit()
	return
#Delete Preformance
def delete_performance(connection, perform_id, type_):
	cur = connection.cursor()
	find = """SELECT Perform_id FROM Performance WHERE Perform_id = %s;"""
	data = (perform_id,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Performance WHERE Perform_id = %s AND Type = %s;"""
		data = (perform_id, type_,)
		cur.execute(delete, data)
		connection.commit()
	return
#Delete Safety/Security ###HasSafety
def delete_safe_security(connection, safety_id, name):
	cur = connection.cursor()
	find = """SELECT Safety_id FROM Safety WHERE Safety_id = %s;"""
	data = (safety_id,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Safety WHERE Safety_id = %s AND Name = %s;"""
		del_data = (safety_id, name)
		cur.execute(delete, del_data)
		find_has = """SELECT Safety_id FROM HasSafety WHERE Safety_id = %s;"""
		cur.execute(find_has, data)
		if cur.fetchone() is not None:
			delete_has = """DELETE FROM HasSafety WHERE Safety_id = %s;"""
			cur.execute(delete_has, data)
		connection.commit()
	return
#Delete Warranty ###HasWarranties
def delete_warranty(connection, w_no, type_, descript):
	cur = connection.cursor()
	find = """SELECT Warranty_no FROM Warranty WHERE Warranty_no = %s;"""
	data = (w_no,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Warranty WHERE Warranty_no = %s AND Type = %s;"""
		del_data = (w_no, type_,)
		cur.execute(delete, del_data)
		find_has = """SELECT FROM HasWarranty WHERE Warranty_no = %s;"""
		cur.execute(find_has, data)
		if cur.fetchone() is not None:
			delete_has = """DELETE FROM HasWarranty WHERE Warranty_no = %s;"""
			cur.execute(delete_has, data)
		connection.commit()
	return
#Delete Audio 
def delete_audio(connection, audio_id, type_):
	cur = connection.cursor()
	find = """SELECT Audio_id FROM Audio WHERE Audio_id = %s;"""
	data = (audio_id,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Audio WHERE Audio_id = %s AND Type = %s;"""
		data = (int_id, type_)
		cur.execute(delete, data)
		connection.commit()
	return
#Delete Comfort Feature ###HasFeature
def delete_features(connection, f_id, name):
	cur = connection.cursor()
	find = """SELECT Feature_id FROM Feature WHERE Feature_id = %s;"""
	data = (f_id,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Feature WHERE Feature_id = %s AND Name = %s;"""
		del_data = (f_id, name,)
		cur.execute(delete, data)
		find_has = """SELECT Feature_id FROM HasFeature WHERE Feature_id = %s;"""
		cur.execute(find_has, del_data)
		if cur.fetchone() is not None:
			delete_has = """DELETE FROM HasFeature WHERE Feature_id = %s;"""
			cur.execute(delete_has, data)
		connection.commit()
	return

#Delete Controls ###HasControl
def delete_control(connection, control_id, type_):
	cur = connection.cursor()
	find = """SELECT Control_id FROM Control WHERE Control_id = %s;"""
	data = (control_id,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Control WHERE Control_id = %s AND Type = %s;"""
		del_data = (control_id, type_,)
		cur.execute(delete, del_data)
		find_has = """SELECT Control_id FROM HasControl WHERE Control_id = %s;"""
		cur.execute(find_has, data)
		if cur.fetchone() is not None:
			delete_has = """DELETE FROM HasControl WHERE Control_id = %s;"""
			cur.execute(delete_has, data)
		connection.commit()
	return

#Delete Exterior 
def delete_exterior(connection, exterior_id, type_):
	cur = connection.cursor()
	find = """SELECT Exterior_id FROM Exterior WHERE Exterior_id = %s;"""
	data = (exterior_id,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Exterior WHERE Exterior_id = %s AND Type = %s;"""
		data = (exterior_id, type_,)
		cur.execute(delete, data)
		connection.commit()
	return
#Delete Handling 
def delete_handling(connection, h_id, type_):
	cur = connection.cursor()
	find = """SELECT Handling_id FROM Handling WHERE Handling_id = %s;"""
	data = (h_id,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Handling WHERE Handling_id = %s AND Type = %s;"""
		data = (h_id, type_,)
		cur.execute(delete, data)
		connection.commit()
	return

#Delete Maintenance ###HasMaintenance relationship
def delete_maintenance(connection, main_no):
	cur = connection.cursor()
	find = """SELECT Main_no FROM Maintenance WHERE Main_no = %s;"""
	data = (main_no,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		del_delete = """DELETE FROM Maintenance WHERE Main_no = %s;"""
		data = (main_no, date_time, service, e_id,)
		cur.execute(del_delete, del_data)
		find_has = """SELECT Main_no FROM HasMaintenance WHERE Main_no = %s;"""
		cur.execute(find_has, data)
		if cur.fetchone() is not None:
			delete_has = """DELETE FROM HasMaintenance WHERE Main_no = %s;"""
			cur.execute(delete_has, data)
		connection.commit()
	return

#Delete Employee-Maintenance
def delete_maintenance_employee(connection, e_id=None, ssn=None):
	cur = connection.cursor()
	find = """SELECT Employ_id FROM Maintence_employ WHERE Employ_id = %s OR SSN = %s;"""
	data = (e_id, ssn,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Maintence_employ WHERE Employ_id = %s OR SSN = %s;"""
		data = (e_id, ssn,)
		cur.execute(delete, data)
		connection.commit()
	return

#Delete Employee-Manager
def delete_manager_employee(connection, e_id=None, ssn=None):
	cur = connection.cursor()
	find = """SELECT Employ_id FROM Manager WHERE Employ_id = %s OR SSN = %s;"""
	data = (e_id, ssn,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Manager WHERE Employ_id = %s OR SSN = %s;"""
		data = (e_id, ssn,)
		cur.execute(delete, data)
		connection.commit()
	return

#Delete Employee-Sales
def delete_sales_employee(connection, e_id=None, ssn=None):
	cur = connection.cursor()
	find = """SELECT Employ_id FROM Sales_employ WHERE Employ_id = %s OR SSN = %s;"""
	data = (e_id, ssn,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Sales_employ WHERE Employ_id = %s OR SSN = %s;"""
		data = (e_id, ssn, fname, lname, start, address,)
		cur.execute(delete, data)
		connection.commit()
	return

#Delete Customer
def delete_customer(connection, name, email):
	cur = connection.cursor()
	find = """SELECT Name, Email FROM Customer WHERE Name = %s AND Email = %s;"""
	data = (name, email,)
	cur.execute(find, data)
	if cur.fetchone() is None:
		return
	else:
		delete = """DELETE FROM Customer WHERE Name = %s AND Email = %s;"""
		cur.execute(delete, data)
		connection.commit()
	return