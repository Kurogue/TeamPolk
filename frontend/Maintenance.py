#This File will handle the building and maintaining of the "Maintenance" Entity
from backend.db import connect
from backend.queries.add_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import datetime
import tkinter as tk 
from tkinter import ttk
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel



class Vehicle_add_delete(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Maintenance")
        self.geometry("1500x1200")
        self.connection = connect()
        #Parameters to build the maintenance item
        self.main_no = IntVar()
        self.year = IntVar()
        self.month = IntVar()
        self.day = IntVar()
        self.service = StringVar()
        self.e_id = IntVar()
        self.date = datetime.date()
        self.vin = StringVar()

        #Build the outline of the maintenance requirements
        self.maintenance_date_label = Label(self, text="Enter The date in day-month-year using numbers: dd-mm-yyyy:")
        self.maintenance_date_label.grid(column=2, row=3, padx=(30,0), pady=(30,0))
        self.maintenance_date_entry = Entry(self, width=2, textvariable=self.day)
        self.maintenance_date_entry.grid(column=2,row=4,padx=(10,0),pady=(10,0))
        self.maintenance_month_entry = Entry(self, width=2, textvariable=self.month)
        self.maintenance_month_entry.grid(column=2, row=5, padx=(10,0), pady=(10,0))
        self.maintenance_year_entry = Entry(self, width=4, textvariable=self.year)

        self.maintenance_number_label = Label(self, text="Enter Maintenance ID: ")
        self.maintenance_number_label.grid(column=2, row=6, padx=(20,0), pady=(20,0))
        self.maintenance_number_entry = Entry(self, width=10, textvariable=self.e_id)
        self.maintenance_number_entry.grid(column=3, row=6, padx=(20,0), pady=(20,0))

        self.maintenance_service_label = Label(self, text="Enter the type of service to preform: ")
        self.maintenance_service_label.grid(column=2, row = 8, padx=(20,0), pady=(20,0))
        self.maintenance_service_entry = Entry(self, width=20, textvariable=self.service)
        self.maintenance_service_entry.grid(column=3, row=8, padx=(20,0), pady=(20,0))

        self.maintenance_vin_label = Label(self, text="Enter the VIN of the vehicle being serviced: ")
        self.maintenance_vin_label.grid(column=2, row = 8, padx=(20,0), pady=(20,0))
        self.maintenance_vin_entry = Entry(self, width=20, textvariable=self.vin)
        self.maintenance_vin_entry.grid(column=3, row=8, padx=(20,0), pady=(20,0))
        
        self.maintenance_button = Button(self, text="Submit", command=self.create_Maintenance)
        self.maintenance_button.grid(column=2, row=10, padx=(20,0), pady=(20,0))

        self.day_maintenance_listbox = Listbox(self, width=20, height=20)
        self.day_maintenance_listbox.grid(column=4, row=2, padx=(30,0), pady=(30,0))
        self.values = self.all_maintenance_today()
        for i in self.values:
            self.day_maintenance_listbox.insert(tk.END, i)


        self.maintenance_button_del = Button(self, text="Delete", command=self.delete_Maintenance)
    def all_maintenance_today(self):
        cur = connection.cursor()
        date = datetime.date.today()
        find = """SELECT VIN, Make, Model, Year, Service FROM Vehicle NATURAL HasMaintence NATURAL JOIN Maintenance WHERE Date = %s;"""
        cur.execute(find, (date,))
        return cur.fetchall()
    def create_Maintenance(self):
        #create date object
        self.date = datetime.date(self.year.get(), self.month.get(), self.day.get())
        add_maintenance(self.connection, self.main_no.get(), self.date, self.service.get(), self.e_id.get())
        add_hasMaintenance(self.connection, self.vin.get(), self.main_no.get())

    def delete_Maintenance(self):
        delete_maintenance(self.connection, self.main_no.get())

