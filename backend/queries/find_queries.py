#This File will, with help of the Database, locate and return data
#that is requested

#Find 1 Vehicle
def find_vehicle(connection, vin):
	cur = connection.cursor()
	#look up vehicle
	find ="""SELECT VIN, Make, Model, Year, Mileage FROM Vehicle WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchone()
#vehicle-interior
def find_vehicle_interior(connection, vin=None):
	cur = connection.cursor()
	#look up vehicle
	find ="""SELECT Type, description FROM Vehicle NATURAL JOIN HasInterior NATURAL JOIN Interior WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchall()
#vehicle-exterior
def find_vehicle_exterior(connection, vin=None):
	cur = connection.cursor()
	find ="""SELECT Type, description FROM Vehicle NATURAL JOIN HasExterior NATURAL JOIN Exterior WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchall()
#vehicle-control
def find_vehicle_control(connection, vin=None):
	cur = connection.cursor()
	find ="""SELECT Type, description FROM Vehicle NATURAL JOIN HasControls NATURAL JOIN Control WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchall()
#vehicle-features
def find_vehicle_features(connection, vin=None):
	cur = connection.cursor()
	find ="""SELECT Name, description FROM Vehicle NATURAL JOIN HasFeatures NATURAL JOIN Feature WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchall()
#vehicle-maintenance
def find_vehicle_maintenance(connection, vin=None):
	cur = connection.cursor()
	find ="""SELECT Date, Service FROM Vehicle NATURAL JOIN HasMaintence NATURAL JOIN Maintenance WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchall()
#vehicle-safety
def find_vehicle_safety(connection, vin=None):
	cur = connection.cursor()
	find ="""SELECT Name, description FROM Vehicle NATURAL JOIN HasSafety NATURAL JOIN Safety WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchall()
#vehicle-warranties
def find_vehicle_warranties(connection, vin=None):
	cur = connection.cursor()
	find ="""SELECT Type, description FROM Vehicle NATURAL JOIN HasWarranties NATURAL JOIN Warranty WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchall()
#vehicle-audio
def find_vehicle_audio(connection, vin=None):
	cur = connection.cursor()
	find ="""SELECT Type, description FROM Vehicle NATURAL JOIN Audio WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchone()
#vehicle-preformance
def find_vehicle_preformance(connection, vin=None):
	cur = connection.cursor()
	find ="""SELECT Type, description FROM Vehicle INNER JOIN Performance ON perform_id = preform_id WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchone()
#vehicle-package
def find_vehicle_package(connection, vin=None):
	cur = connection.cursor()
	find ="""SELECT Name, description FROM Vehicle NATURAL JOIN Package WHERE VIN = %s;"""
	attr = (vin,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find all vehicles 
def find_all_vehicles(connection, make=None, model=None, year=None):
	cur = connection.cursor()
	if make is None and model is None and year is None:
		find = """SELECT VIN, Make, Model, Year, Mileage FROM Vehicle"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT VIN, Make, Model, Year, Mileage FROM Vehicle WHERE Make = %s OR Model = %s OR year = %s;"""
		attr = (make, model, year,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find Vehicle Sold
def find_sold_vehicles(connection):
	cur = connection.cursor()
	#look up vehicle
	find ="""SELECT VIN, Make, Model, Year, Mileage, Customer_name, Customer_email FROM Vehicle WHERE Customer_name IS NOT NULL AND Customer_email IS NOT NULL;"""
	cur.execute(find)
	return cur.fetchall()

#Find InStock
def find_Instock(connection, vin=None):
	cur = connection.cursor()
	if vin is None:
		find = """SELECT VIN, Make, Model, Year, Date_added FROM Instock NATURAL JOIN Vehicle"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT VIN, Make, Model, Year, Date_added FROM Instock NATURAL JOIN Vehicle WHERE VIN = %s;"""
		value = (vin,)
		cur.execute(find, value)
		return cur.fetchone()

#Find In BackOrder
def find_BackOrder(connection, vin=None):
	cur = connection.cursor()
	if vin is None:
		find = """SELECT VIN, Make, Model, Year, Date_added FROM BackOrder NATURAL JOIN Vehicle;"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT VIN, Make, Model, Year, Date_added FROM BackOrder NATURAL JOIN Vehicle WHERE VIN = %s"""
		value = (vin,)
		cur.execute(find, value)
		return cur.fetchone()

#Find 1 Interior
def find_interior(connection, int_id):
	cur = connection.cursor()
	find ="""SELECT * FROM Interior WHERE Interior_id = %s;"""
	attr = (int_id,)
	cur.execute(find, attr)
	return cur.fetchone()
#Find All Interior
def find_all_interiors(connection, type_=None, color=None):
	cur = connection.cursor()
	if type_ is None and color is None:
		find = """SELECT * FROM Interior"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Interior WHERE Type = %s OR Color = %s;"""
		attr = (type_, color,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find 1 Package
def find_package(connection, p_id):
	cur = connection.cursor()
	find ="""SELECT * FROM Package WHERE Package_id = %s;"""
	attr = (p_id,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Package
def find_all_packages(connection, name=None):
	cur = connection.cursor()
	if name is None:
		find = """SELECT * FROM Package"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Package WHERE Name = %s;"""
		attr = (name,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find 1 Preformance
def find_preformance(connection, per_id):
	cur = connection.cursor()
	find ="""SELECT * FROM Performance WHERE Perform_id = %s;"""
	attr = (per_id,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Preformance
def find_all_preformance(connection, type_=None):
	cur = connection.cursor()
	if type_ is None:
		find = """SELECT * FROM Performance"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Performance WHERE Type = %s;"""
		attr = (type_,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find 1 Safety/Security
def find_safety(connection, s_id):
	cur = connection.cursor()
	find ="""SELECT * FROM Safety WHERE Safety_id = %s;"""
	attr = (s_id,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Safety/Security
def find_all_safety(connection, name=None):
	cur = connection.cursor()
	if name is None:
		find = """SELECT * FROM Safety"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Safety WHERE name = %s;"""
		attr = (name,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find 1 Warranty
def find_warranty(connection, w_no):
	cur = connection.cursor()
	find ="""SELECT * FROM Warranty WHERE Warranty_no = %s;"""
	attr = (w_no,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Warranty
def find_all_warranty(connection, type_=None):
	cur = connection.cursor()
	if type_ is None:
		find = """SELECT * FROM Warranty"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Warranty WHERE Type = %s;"""
		attr = (type_,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find 1 Audio
def find_audio(connection, audio_id):
	cur = connection.cursor()
	find ="""SELECT * FROM Audio WHERE Audio_id = %s;"""
	attr = (audio_id,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Audio
def find_all_audio(connection, type_=None):
	cur = connection.cursor()
	if type_ is None:
		find = """SELECT * FROM Audio"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Audio WHERE Type = %s;"""
		attr = (type_,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find 1 Comfort Features
def find_feature(connection, f_id):
	cur = connection.cursor()
	find ="""SELECT * FROM Feature WHERE Feature_id = %s;"""
	attr = (f_id,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Features
def find_all_feature(connection, name=None):
	cur = connection.cursor()
	if name is None:
		find = """SELECT * FROM Feature"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Feature WHERE Name = %s;"""
		attr = (name,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find 1 Controls
def find_controls(connection, con_id):
	cur = connection.cursor()
	find ="""SELECT * FROM Control WHERE Control_id = %s;"""
	attr = (con_id,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Controls
def find_all_controls(connection, type_=None):
	cur = connection.cursor()
	if type_ is None:
		find = """SELECT * FROM Control"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Control WHERE Type = %s;"""
		attr = (type_,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find 1 Exterior
def find_exterior(connection, ex_id):
	cur = connection.cursor()
	find ="""SELECT * FROM Exterior WHERE Exterior_id = %s;"""
	attr = (ex_id,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Exterior
def find_all_exterior(connection, type_=None, color=None):
	cur = connection.cursor()
	if type_ is None and color is None:
		find = """SELECT * FROM Exterior"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Exterior WHERE Type = %s OR Color = %s;"""
		attr = (type_, color,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find 1 Handling
def find_handling(connection, h_id):
	cur = connection.cursor()
	find ="""SELECT * FROM Handling WHERE handling_id = %s;"""
	attr = (h_id,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Handling
def find_all_handling(connection, type_=None):
	cur = connection.cursor()
	if type_ is None:
		find = """SELECT * FROM Handling"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Handling WHERE Type = %s;"""
		attr = (type_,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find 1 Maintenance
def find_maintence(connection, main_no):
	cur = connection.cursor()
	find ="""SELECT * FROM Maintenance WHERE Main_no = %s;"""
	attr = (main_no,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Maintenance
def find_all_Maintenance(connection, date=None, service=None):
	cur = connection.cursor()
	if date is None and service is None:
		find = """SELECT * FROM Maintenance"""
		cur.execute(find)
		return cur.fetchall()
	else:
		find = """SELECT * FROM Maintenance WHERE Date = %s OR Service = %s;"""
		attr = (date, service,)
		cur.execute(find, attr)
		return cur.fetchall()

#Find All Employee
def find_all_employees(connection):
	cur = connection.cursor()
	find = """SELECT employ_id,  FROM Manager OUTER JOIN Maintence_employ OUTER JOIN Sales_employ;"""
	cur.execute(find)
	return cur.fetchall()

#Find Employee-Maintenance
def find_maintence_employee(connection, e_id=None, fname=None, lname=None):
	cur = connection.cursor()
	find ="""SELECT * FROM Maintence_employ WHERE e_id = %s OR (SELECT * FROM Maintence_employ WHERE fname = %s AND lname = %s);"""
	attr = (e_id, fname, lname,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find 1 employee
def find_employee(connection, e_id, fname=None, lname=None, ssn=None):
	cur = connection.cursor()
	find ="""SELECT * FROM Manager NATURAL JOIN Sales_employ NATURAL JOIN Maintence_employ WHERE employ_id = %s OR (fname =%s AND lname = %s) OR ssn = %s;"""
	cur.execute(find, (e_id, fname, lname, ssn))
	return cur.fetchall()

#Find Employee-Manager
def find_manager_employee(connection, e_id=None, fname=None, lname=None):
	cur = connection.cursor()
	find ="""SELECT * FROM Manager WHERE e_id = %s OR (SELECT * FROM Manager WHERE fname = %s AND lname = %s);"""
	attr = (e_id, fname, lname,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Customer
def find_customer(connection):
	cur = connection.cursor()
	find ="""SELECT * FROM Manager;"""
	cur.execute(find)
	return cur.fetchall()

#Find Employee-Sales
def find_sales_employee(connection, e_id=None, fname=None, lname=None):
	cur = connection.cursor()
	find ="""SELECT * FROM Sales_employ WHERE e_id = %s OR (SELECT * FROM Sales_employ WHERE fname = %s AND lname = %s);"""
	attr = (e_id, fname, lname,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Employee-Sales
def find_all_sales(connection):
	cur = connection.cursor()
	find ="""SELECT * FROM Sale_employ;"""
	cur.execute(find)
	return cur.fetchall()

#Find Customer
def find_customer(connection, name=None, email=None):
	cur = connection.cursor()
	find ="""SELECT * FROM Customer WHERE Customer_name = %s AND Customer_email = %s;"""
	attr = (name, email,)
	cur.execute(find, attr)
	return cur.fetchone()

#Find All Customers
#Error handling check 
def find_all_customers(connection):
    try:
        cur = connection.cursor()
        find = """SELECT * FROM Customer;"""
        cur.execute(find)
        return cur.fetchall()
    except Exception as e:
        print(f"Error while trying to find all customers: {e}")

def locate_vehicle(self):
    vin = self.vin.get()
    make = self.make.get()
    model = self.model.get()
    year = self.year.get()

    vehicle = find_vehicle(self.connection, vin)

    if vehicle:
        vehicle_info = f"Vehicle found:\nVIN: {vehicle[0]}\nMake: {vehicle[1]}\nModel: {vehicle[2]}\nYear: {vehicle[3]}"
        self.search_result_label.config(text=vehicle_info)
    else:
        self.search_result_label.config(text="Vehicle not found.")
