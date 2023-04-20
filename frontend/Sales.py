#This File will handle the building and maintaining of the "Maintenance" Entity
from backend.db import connect
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import datetime
import tkinter as tk 
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel



class Vehicle_Sells(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Sales")
        self.geometry("1500x1200")
        self.connection = connect()
        #Parameters to build the maintenance item
        self.vin = StringVar()
        self.c_name = StringVar()
        self.c_email = StringVar()
        self.e_id = IntVar()
        #Build the outline of the customer requirements
        self.customer_name_label = Label(self, text="Enter Customer Name:")
        self.customer_name_label.grid(column=2, row=2, padx=(30,0), pady=(30,0))
        self.customer_name_entry = Entry(self, width=30, textvariable=self.c_name)
        self.customer_name_entry.grid(column=3, row=3, padx=(30,0), pady=(30,0))
        self.customer_name_label = Label(self, text="Enter Customer Email:")
        self.customer_name_label.grid(column=2, row=3, padx=(30,0), pady=(30,0))
        self.customer_name_entry = Entry(self, width=30, textvariable=self.c_email)
        self.customer_name_entry.grid(column=3, row=3, padx=(30,0), pady=(30,0))
    
        self.saleperson_id_label = Label(self, text="Enter your employee id:")
        self.saleperson_id_label.grid(column=2, row=4, padx=(30,0), pady=(30,0))
        self.saleperson_id_entry = Entry(self, width=30, textvariable=self.e_id)
        self.saleperson_id_entry.grid(column=3, row=4, padx=(30,0), pady=(30,0))
    
        self.vehicle_id_label = Label(self, text="Enter the Vehicle VIN")
        self.vehicle_id_label.grid(column=2, row=5, padx=(30,0), pady=(30,0))
        self.vehicle_id_entry = Entry(self, width=30, textvariable=self.vin)
        self.vehicle_id_entry.grid(column=3, row=5, padx=(30,0), pady=(30,0))

        self.submit_button = Button(self, text="Submit", command=self.make_sale)
        self.submit_button.grid(column=2, row=6, padx=(30,0), pady=(30,0))

    def make_sale(self):
        cur = connection.cursor()
        up_vehicle = """UPDATE Vehicle SET Customer_name = %s, Customer_email = %s WHERE VIN = %s;"""
        cur.execute(up_vehicle, (self.c_name, self.c_email, self.vin,))
        up_customer = """UPDATE Customer Set Seller = %s WHERE Customer_name = %s AND Customer_email = %s"""
        cur.execute(up_customer, (self.e_id, self.c_name, self.c_email))
        connection.commit()
        return


