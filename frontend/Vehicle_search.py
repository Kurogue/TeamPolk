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

        self.interior = find_vehicle_interior(self.connection)
        self.interior_list = tk.Listbox(form_frame, width=20, height=20)
        self.interior_list.grid(column=0, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)

        self.exterior = find_vehicle_exterior(self.connection)
        self.exterior_list = tk.Listbox(form_frame, width=20, height=20)
        self.exterior_list.grid(column=0, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)

        self.control = find_vehicle_control(self.connection)
        self.control_list = tk.Listbox(form_frame, width=20, height=20)
        self.control_list.grid(column=1, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)

        self.features = find_vehicle_features(self.connection)
        self.features_list = tk.Listbox(form_frame, width=20, height=20)
        self.features_list.grid(column=2, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)

        self.maintenance = find_vehicle_maintenance(self.connection)
        self.maintenance_list = tk.Listbox(form_frame, width=20, height=20)
        self.maintenance_list.grid(column=3, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)

        self.safety = find_vehicle_safety(self.connection)
        self.safety_list = tk.Listbox(form_frame, width=20, height=20)
        self.safety_list.grid(column=4, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)

        self.warranty = find_vehicle_warranties(self.connection)
        self.warranty_list = tk.Listbox(form_frame, width=20, height=20)
        self.warranty_list.grid(column=5, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)

        self.audio = find_vehicle_audio(self.connection)
        self.audio_list = tk.Listbox(form_frame, width=20, height=20)
        self.audio_list.grid(column=6, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)

        self.preform = find_vehicle_preformance(self.connection)
        self.preform_list = tk.Listbox(form_frame, width=20, height=20)
        self.preform_list.grid(column=7, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)

        self.package = find_vehicle_package(self.connection)
        self.package_list = tk.Listbox(form_frame, width=20, height=20)
        self.package_list.grid(column=8, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)
        # Add a label to display the search result message
        self.search_result_label = Label(form_frame, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.search_result_label.grid(column=0, row=5, pady=(10, 10))

    def locate_vehicle(self):
        vin = self.vin.get()

        vehicle = find_vehicle(self.connection, vin)

        self.interior = find_vehicle_interior(self.connection, vin)
        if self.interior is not None:
            for item in self.interior:
                self.interior_list.insert(tk.END, item)
        self.exterior = find_vehicle_exterior(self.connection, vin)
        if self.exterior is not None:
            for item in self.exterior:
                self.exterior_list.insert(tk.END, item)
        self.control = find_vehicle_control(self.connection, vin)
        if self.control is not None:
            for item in self.control:
                self.control_list.insert(tk.END, item)
        self.features = find_vehicle_features(self.connection, vin)
        if self.features is not None:
            for item in self.features:
                self.features_list.insert(tk.END, item)
        self.maintenance = find_vehicle_maintenance(self.connection, vin)
        if self.maintenance is not None:
            for item in self.maintenance:
                self.maintenance_list.insert(tk.END, item)
        self.safety = find_vehicle_safety(self.connection)
        if self.safety is not None:
            for item in self.safety:
                self.safety_list.insert(tk.END, item)
        self.warranty = find_vehicle_warranties(self.connection)
        if self.warranty is not None:
            for item in self.warranty:
                self.warranty_list.insert(tk.END, item)
        self.audio = find_vehicle_audio(self.connection)
        if self.audio is not None:
            for item in self.audio:
                self.audio_list.insert(tk.END, item)
        self.package = find_vehicle_package(self.connection)
        if self.package is not None:
            for item in self.package:
                self.package_list.insert(tk.END, item)
        self.preform = find_vehicle_preformance(self.connection)
        if self.preform is not None:
            for item in self.preform:
                self.preform_list.insert(tk.END, item)
        if vehicle:
            vehicle_info = f"Vehicle found:\nVIN: {vehicle[0]}\nMake: {vehicle[1]}\nModel: {vehicle[2]}\nYear: {vehicle[3]}"
            self.search_result_label.config(text=vehicle_info)
        else:
            self.search_result_label.config(text="Vehicle not found.")


