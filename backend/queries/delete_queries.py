#This file will handle the deletion of entries or relationships from the database
#Will have to account for the various many to one Or many to many relationships that may need to be checked

#Delete Vehicle that also has error handling check for all the other tables that have a relationship with vehicle
def delete_vehicle(connection, vin):
    try:
        cur = connection.cursor()
        # lookup to make sure the vehicle doesn't exist
        find = """SELECT VIN FROM Vehicle WHERE VIN = %s;"""
        data = (vin,)
        cur.execute(find, data)
        if cur.fetchone() is None:
            # print("Vehicle Not in Table") # Need to print to the window
            return
        else:
            delete_hasInterior(connection, vin, None)
            delete_hasExterior(connection, vin, None)
            delete_hasFeature(connection, vin, None)
            delete_hasSafety(connection, vin, None)
            delete_hasWarranty(connection, vin, None)
            delete_hasMaintenance(connection, vin, None)
			delete_hasControl(connection, vin, None)
            add = """DELETE FROM Vehicle WHERE VIN = %s;"""
            car_values = (vin,)
            cur.execute(add, car_values)
            connection.commit()
            # check the instock or backorder to remove those too
            find_instock = """SELECT VIN FROM Instock WHERE VIN = %s;"""
            cur.execute(find_instock, data)
            if cur.fetchone() is not None:
                del_instock = """DELETE FROM Instock WHERE VIN = %s;"""
                values = (vin,)
                cur.execute(del_instock, values)
                connection.commit()
            find_backorder = """ SELECT VIN FROM Backorder WHERE VIN = %s;"""
            cur.execute(find_backorder, data)
            if cur.fetchone() is not None:
                backorder = """DELETE FROM Backorder WHERE VIN = %s;"""
                values = (vin,)
                cur.execute(backorder, values)
                connection.commit()
            return
    except Exception as e:
        print("Error deleting vehicle:", e)
        return
    finally:
        connection.close()

def delete_hasInterior(connection, vin=None, int_id=None):
	cur = connection.cursor()
	find = """SELECT * FROM hasInterior WHERE VIN = %s;"""
	cur.execute(find, (vin,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM HasInterior WHERE VIN = %s;"""
		cur.execute(delete, (vin,))
		connection.commit()
		return

def delete_hasExterior(connection, vin=None, ext_id=None):
	cur = connection.cursor()
	find = """SELECT * FROM hasExterior WHERE VIN = %s OR Exterior_id = %;s"""
	cur.execute(find, (vin, ext_id,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM HasExterior WHERE VIN = %s OR Exterior_id = %s;"""
		cur.execute(delete, (vin,))
		connection.commit()
		return

def delete_hasSafety(connection, vin=None, s_id=None):
	cur = connection.cursor()
	find = """SELECT * FROM hasSafety WHERE VIN = %s OR Safety_id = %s;"""
	cur.execute(find, (vin, s_id,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM HasSafety WHERE VIN = %s OR Safety_id = %s;"""
		cur.execute(delete, (vin, s_id,))
		connection.commit()
		return

def delete_hasWarranty(connection, vin=None, w_no=None):
	cur = connection.cursor()
	find = """SELECT * FROM hasWarranties WHERE VIN = %s OR Warranty_no = %s;"""
	cur.execute(find, (vin, w_no))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM hasWarranties Where VIN = %s OR Warranty_no = %s;"""
		cur.execute(delete, (vin, w_no,))
		connection.commit()
		return

def delete_hasFeature(connection, vin=None, f_id=None):
	cur = connection.cursor()
	find = """SELECT * FROM hasFeatures WHERE VIN = %s OR Feature_id = %s;"""
	cur.execute(find, (vin, f_id,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM hasFeatures WHERE VIN = %s OR Feature_id = %s;"""
		cur.execute(delete, (vin, f_id,))
		connection.commit()
		return

def delete_hasMaintenance(connection, vin=None, main_no=None):
	cur = connection.cursor()
	find = """SELECT * FROM hasMaintence WHERE VIN = %s OR Main_no = %s;"""
	cur.execute(find, (vin, main_no,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM hasMaintence WHERE VIN = %s OR Main_no = %s;"""
		cur.execute(delete, (vin, main_no,))
		connection.commit()
		return

def delete_hasControl(connection, vin=None, c_id=None):
	cur = connection.cursor()
	find = """SELECT * FROM hasControl WHERE VIN = %s OR Control_id = %s;"""
	cur.execute(find, (vin, c_id,))
	if cur.fetchall() is None:
		return
	else:
		delete = """DELETE FROM hasControl WHERE VIN = %s OR Control_id = %s;"""
		cur.execute(delete, (vin, c_id,))
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
		delete_hasInterior(connection, None, int_id)
		delete = """DELETE FROM Interior WHERE Interior_id = %s AND Type = %s;"""
		del_data = (int_id, type_,)
		cur.execute(delete, del_data)
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
		delete_hasSafety(connection, None, safety_id)
		delete = """DELETE FROM Safety WHERE Safety_id = %s AND Name = %s;"""
		del_data = (safety_id, name)
		cur.execute(delete, del_data)
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
		delete_hasWarranty(connection, None, w_no)
		delete = """DELETE FROM Warranty WHERE Warranty_no = %s AND Type = %s;"""
		del_data = (w_no, type_,)
		cur.execute(delete, del_data)
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
		data = (audio_id, type_)
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
		delete_hasFeature(connection, None, f_id)
		delete = """DELETE FROM Feature WHERE Feature_id = %s AND Name = %s;"""
		del_data = (f_id, name,)
		cur.execute(delete, data)
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
		delete_hasControl(connection, None, control_id)
		delete = """DELETE FROM Control WHERE Control_id = %s AND Type = %s;"""
		del_data = (control_id, type_,)
		cur.execute(delete, del_data)
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
		delete_hasExterior(connection, None, exterior_id)
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
		delete_hasMaintenance(connection,None, main_no)
		del_delete = """DELETE FROM Maintenance WHERE Main_no = %s;"""
		cur.execute(del_delete, data)
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
		data = (e_id, ssn)
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