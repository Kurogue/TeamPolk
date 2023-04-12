

from backend.db import connect
from backend.queries.vehicle_queries import *

import tkinter as tk

class Vehicle_search:
    def __init__(self, root):
        root.title("Vehicle Tracking Service")
        root.geometry("400x400")

        self.vin = ""
        self.make = ""
        self.model = ""
        self.year = ""
        self.connection = connect()
        self.data = None
        self.stock = 0;
        # find Vehicle
        findVehicle_vin = tk.Label(root, text="VIN: ")
        findVehicle_vin.grid(column=0, row=0)
        findVehicle_vin_entry = tk.Entry(root, width=10, textvariable=self.vin)  
        findVehicle_vin_entry.grid(column=1, row=0)

        findVehicle_make= tk.Label(root, text="Make: ")
        findVehicle_make.grid(column=0, row=1)
        findVehicle_make_entry = tk.Entry(root, width=10, textvariable=self.make)
        findVehicle_make_entry.grid(column=1, row=1)

        findVehicle_model = tk.Label(root, text="Model: ")
        findVehicle_model.grid(column=0, row=2)
        findVehicle_model_entry = tk.Entry(root, width=10, textvariable=self.model)
        findVehicle_model_entry.grid(column=1, row=2)

        findVehicle_year = tk.Label(root, text="Year: ")
        findVehicle_year.grid(column=0, row=3)
        findVehicle_year_entry = tk.Entry(root, width=10, textvariable=self.year)
        findVehicle_year_entry.grid(column=1, row=3)

        findVehicle_button = tk.Button(text="Find Vehicle", commmand=self.locate_vehicle)
        findVehicle_button.grid(column=0, row=4)
        root.mainloop()
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