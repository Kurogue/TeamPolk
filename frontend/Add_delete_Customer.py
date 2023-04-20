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
        self.c_addr = StringVar()
        self.phone = IntVar()
        self.year = IntVar()
        self.month = IntVar()
        self.day = IntVar()
        self.value = True
        #Build the outline of the date requirements
        self.customer_date_label = Label(self, text="Enter The DOB in day-month-year using numbers: dd-mm-yyyy:")
        self.customer_date_label.grid(column=2, row=4, padx=(30,0), pady=(30,0))
        self.customer_date_entry = Entry(self, width=2, textvariable=self.day)
        self.customer_date_entry.grid(column=2,row=5,padx=(10,0),pady=(10,0))
        self.customer_month_entry = Entry(self, width=2, textvariable=self.month)
        self.customer_month_entry.grid(column=2, row=6, padx=(10,0), pady=(10,0))
        self.customer_year_entry = Entry(self, width=4, textvariable=self.year)
        self.customer_year_entry.grid(column=2, row=7, padx=(30,0), pady=(30,0))
        self.customer_name_label = Label(self, text="Enter Customer Name:")
        self.customer_name_label.grid(column=2, row=8, padx=(30,0), pady=(30,0))
        self.customer_name_entry = Entry(self, width=30, textvariable=self.c_name)
        self.customer_name_entry.grid(column=3, row=8, padx=(30,0), pady=(30,0))
        self.customer_email_label = Label(self, text="Enter Customer Email:")
        self.customer_email_label.grid(column=2, row=9, padx=(30,0), pady=(30,0))
        self.customer_email_entry = Entry(self, width=30, textvariable=self.c_email)
        self.customer_email_entry.grid(column=3, row=9, padx=(30,0), pady=(30,0))
        self.customer_addr_label = Label(self, text="Enter Customer Address:")
        self.customer_addr_label.grid(column=2, row=9, padx=(30,0), pady=(30,0))
        self.customer_addr_entry = Entry(self, width=30, textvariable=self.c_email)
        self.customer_addr_entry.grid(column=3, row=9, padx=(30,0), pady=(30,0))
        self.customer_phone_label = Label(self, text="Enter Customer Phone Numnber:")
        self.customer_phone_label.grid(column=2, row=9, padx=(30,0), pady=(30,0))
        self.customer_phone_entry = Entry(self, width=30, textvariable=self.c_email)
        self.customer_phone_entry.grid(column=3, row=9, padx=(30,0), pady=(30,0))
        
        self.customer_button = Button(self, text="Create", command=self.create_Customer)
        self.customer_button.grid(column=2, row=10, padx=(30,0), pady=(30,0))
        self.maintenance_button_del = Button(self, text="Delete", command=self.delete_Customer)
        self.customer_button.grid(column=2, row=10, padx=(30,0), pady=(30,0))
    def create_Customer(self):
        #name, address, email, dob, p_no
        date = datetime.date(self.year.get(), self.month.get(), self.day.get())
        value = add_customer(self.connection, self.c_name, self.c_addr, self.c_email, date, self.phone)
        if value is True:
            self.add_confirmed = Label(self, text="Customer Add Successfully")
            self.add_confirmed.grid(column=2, row=11, padx=(30,0), pady=(30,0))
        else:
            self.add_failed = Label(self, text="Failed To added Customer")
            self.add_failed.grid(column=2, row=11, padx=(30,0), pady=(30,0))
    def delete_Customer(self):
        delete_customer(self.connection, self.c_name, self.c_email)