from backend.db import connect
#from backend.queries.vehicle_queries import *
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import tkinter as tk
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel

class Vehicle_search(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Vehicle Search")
        self.geometry("600x600")
        self.vin =  StringVar()
        self.make =  StringVar()
        self.model =  StringVar()
        self.year =  IntVar()
        self.connection = connect()
        self.data = None
        self.stock = 0
        # find Vehicle
        findVehicle_vin = Label(self, text="VIN: ")
        findVehicle_vin.grid(column=0, row=0, pady=(150,0), padx=(150, 0))
        findVehicle_vin_entry = Entry(self, width=30, textvariable=self.vin)  
        findVehicle_vin_entry.grid(column=1, row=0, pady=(150,0), padx=(0, 150))

        findVehicle_make= Label(self, text="Make: ")
        findVehicle_make.grid(column=0, row=1, pady=(37.5,0), padx=(150, 0))
        findVehicle_make_entry = tk.Entry(self, width=30, textvariable=self.make)
        findVehicle_make_entry.grid(column=1, row=1, pady=(37.5,0), padx=(0, 150))

        findVehicle_model = Label(self, text="Model: ")
        findVehicle_model.grid(column=0, row=2, pady=(37.5,0), padx=(150, 0))
        findVehicle_model_entry = tk.Entry(self, width=30, textvariable=self.model)
        findVehicle_model_entry.grid(column=1, row=2, pady=(37.5,0), padx=(0, 150))

        findVehicle_year = Label(self, text="Year: ")
        findVehicle_year.grid(column=0, row=3, pady=(37.5,0), padx=(150, 0))
        findVehicle_year_entry = tk.Entry(self, width=30, textvariable=self.year)
        findVehicle_year_entry.grid(column=1, row=3, pady=(37.5,0), padx=(0, 150))

        findVehicle_button = Button(self, text="Find Vehicle", command=self.locate_vehicle)
        findVehicle_button.grid(column=0, row=4, pady=(37.5,0), padx=(37.5, 0), columnspan = 2)

         # Add a label to display the search result message
        self.search_result_label = Label(self, text="")
        self.search_result_label.grid(column=0, row=5, pady=(37.5, 0), columnspan=2)

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

    def locate_all(self):
        make = self.make.get()
        model = self.model.get()
        year = self.year.get()
        self.data = find_all_vehicles(self.connection, model, make, year)

    def find_instock(self):
        self.data = find_Instock(self.connection, self.vin)

    def find_onbackorder(self):
        self.data = find_BackOrder(self.connection, self.vin)

    def check_instock(self):
        self.data = check_inStock(self.connection)

    def check_onbackorder(self):
        self.data = check_backorder(self.connection)

    def add_vehicle(self):
        add_vehicle(self.connection, self.vin, self.make, self.model, self.year, self.stock)
    def delete_vehicle(self):
        delete_vehicle(self.connection, self.vin)