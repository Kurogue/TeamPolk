//Added description

from backend.db import connect
from backend.queries.vehicle_queries import *
from tkinter import *
import tkinter as tk

class Vehicle_search(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Vehicle Search")
        self.geometry("600x600")
        self.vin = ""
        self.make = ""
        self.model = ""
        self.year = ""
        self.connection = connect()
        self.data = None
        self.stock = 0;
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
    def locate_vehicle(self):
        self.data = find_vehicle(self.connection, self.vin)

    def locate_all(self):
        self.data = find_all_vehicles(self.connection)

    def find_instock(self):
        self.data = find_Instock(self.connection, self.vin)

    def find_onbackorder(self):
        self.data = find_BackOrder(self.connection, self.vin)

    def check_instock(self):
        self.data = check_inStock(self.connection)

    def check_onbackorder(self):
        self.data = check_BackOrder(self.connection)

    def add_vehicle(self):
        add_vehicle(self.connection, self.vin, self.make, self.model, self.year, self.stock)
    def delete_vehicle(self):
        delete_vehicle(self.connection, self.vin)
