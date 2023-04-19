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
        super().__init__(master=master)
        self.title("Vehicle Search")
        self.geometry("600x600")
        self.configure(bg='#36454F')
        self.vin = StringVar()
        self.make = StringVar()
        self.model = StringVar()
        self.year = IntVar()
        self.connection = connect()
        self.data = None
        self.stock = 0

        # Create a Frame to hold the form
        form_frame = Frame(self, bg='#36454F')
        form_frame.pack(expand=True)

        # find Vehicle
        findVehicle_vin = Label(form_frame, text="VIN: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        findVehicle_vin.grid(column=0, row=0)
        findVehicle_vin_entry = Entry(form_frame, width=30, textvariable=self.vin, font=("Arial", 16, "bold"))  
        findVehicle_vin_entry.grid(column=1, row=0, pady=(10, 10))

        findVehicle_make= Label(form_frame, text="Make: ", bg='#36454F',fg='white', font=("Arial", 16, "bold"), width=20)
        findVehicle_make.grid(column=0, row=1)
        findVehicle_make_entry = tk.Entry(form_frame, width=30, textvariable=self.make, font=("Arial", 16, "bold"))
        findVehicle_make_entry.grid(column=1, row=1, pady=(10, 10))

        findVehicle_model = Label(form_frame, text="Model: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        findVehicle_model.grid(column=0, row=2)
        findVehicle_model_entry = tk.Entry(form_frame, width=30, textvariable=self.model, font=("Arial", 16, "bold"))
        findVehicle_model_entry.grid(column=1, row=2, pady=(10, 10))

        findVehicle_year = Label(form_frame, text="Year: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        findVehicle_year.grid(column=0, row=3)
        findVehicle_year_entry = tk.Entry(form_frame, width=30, textvariable=self.year, font=("Arial", 16, "bold"))
        findVehicle_year_entry.grid(column=1, row=3, pady=(10, 10))

        findVehicle_button = Button(form_frame, text="Find Vehicle", command=self.locate_vehicle)
        findVehicle_button.grid(column=0, row=4, pady=(10, 10))

        # Add a label to display the search result message
        self.search_result_label = Label(form_frame, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.search_result_label.grid(column=0, row=5, pady=(10, 10))

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


