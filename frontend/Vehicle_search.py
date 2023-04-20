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
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
# Set the geometry of the window to the full size of the screen
        self.geometry(f"{screen_width}x{screen_height}")
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
        findVehicle_vin = Label(form_frame, text="VIN: ", bg='#36454F', fg='white', font=("Verdana", 12, "bold"), width=15)
        findVehicle_vin.grid(column=0, row=0)
        findVehicle_vin_entry = Entry(form_frame, width=30, textvariable=self.vin, font=("Verdana", 12, "bold"))  
        findVehicle_vin_entry.grid(column=1, row=0, pady=(10, 10))

        findVehicle_make= Label(form_frame, text="Make: ", bg='#36454F',fg='white', font=("Verdana", 12, "bold"), width=15)
        findVehicle_make.grid(column=0, row=1)
        findVehicle_make_entry = tk.Entry(form_frame, width=30, textvariable=self.make, font=("Verdana", 12, "bold"))
        findVehicle_make_entry.grid(column=1, row=1, pady=(20, 10))

        findVehicle_model = Label(form_frame, text="Model: ", bg='#36454F', fg='white', font=("Verdana", 12, "bold"), width=15)
        findVehicle_model.grid(column=0, row=2)
        findVehicle_model_entry = tk.Entry(form_frame, width=30, textvariable=self.model, font=("Verdana", 12, "bold"))
        findVehicle_model_entry.grid(column=1, row=2, pady=(20, 10))

        findVehicle_year = Label(form_frame, text="Year: ", bg='#36454F', fg='white', font=("Verdana", 12, "bold"), width=15)
        findVehicle_year.grid(column=0, row=3)
        findVehicle_year_entry = tk.Entry(form_frame, width=30, textvariable=self.year, font=("Verdana", 12, "bold"))
        findVehicle_year_entry.grid(column=1, row=3, pady=(20, 10))

        findVehicle_button = Button(form_frame, text="Find Vehicle", command=self.locate_vehicle)
        findVehicle_button.grid(column=0, row=4, pady=(10, 10))

        form_frame.pack(fill=tk.BOTH, expand=True)

        listbox_spacing = 0.1
        listbox_width = 0.1

        self.interior = find_vehicle_interior(self.connection)
        self.interior_list = tk.Listbox(form_frame, width=10, height=10)
        # self.interior_list.place(relx=0.05, rely=0.6, relwidth=listbox_width, anchor=tk.CENTER)

        self.exterior = find_vehicle_exterior(self.connection)
        self.exterior_list = tk.Listbox(form_frame, width=10, height=10)
        # self.exterior_list.place(relx=0.05 + listbox_spacing, rely=0.6, relwidth=listbox_width, anchor=tk.CENTER)

        self.control = find_vehicle_control(self.connection)
        self.control_list = tk.Listbox(form_frame, width=10, height=10)
        # self.control_list.place(relx=0.05 + 2 * listbox_spacing, rely=0.6, relwidth=listbox_width, anchor=tk.CENTER)

        self.features = find_vehicle_features(self.connection)
        self.features_list = tk.Listbox(form_frame, width=10, height=10)
        # self.features_list.place(relx=0.05 + 3 * listbox_spacing, rely=0.6, relwidth=listbox_width, anchor=tk.CENTER)

        self.maintenance = find_vehicle_maintenance(self.connection)
        self.maintenance_list = tk.Listbox(form_frame, width=10, height=10)
        # self.maintenance_list.place(relx=0.05 + 4 * listbox_spacing, rely=0.6, relwidth=listbox_width, anchor=tk.CENTER)

        self.safety = find_vehicle_safety(self.connection)
        self.safety_list = tk.Listbox(form_frame, width=10, height=10)
        # self.safety_list.place(relx=0.05 + 5 * listbox_spacing, rely=0.6, relwidth=listbox_width, anchor=tk.CENTER)

        self.warranty = find_vehicle_warranties(self.connection)
        self.warranty_list = tk.Listbox(form_frame, width=10, height=10)
        # self.warranty_list.place(relx=0.05 + 6 * listbox_spacing, rely=0.6, relwidth=listbox_width, anchor=tk.CENTER)

        self.audio = find_vehicle_audio(self.connection)
        self.audio_list = tk.Listbox(form_frame, width=10, height=10)
        # self.audio_list.place(relx=0.05 + 7 * listbox_spacing, rely=0.6, relwidth=listbox_width, anchor=tk.CENTER)

        self.preform = find_vehicle_preformance(self.connection)
        self.preform_list = tk.Listbox(form_frame, width=10, height=10)
        # self.preform_list.place(relx=0.05 + 8 * listbox_spacing, rely=0.6, relwidth=listbox_width, anchor=tk.CENTER)

        self.package = find_vehicle_package(self.connection)
        self.package_list = tk.Listbox(form_frame, width=10, height=10)
        # self.package_list.place(relx=0.05 + 9 * listbox_spacing, rely=0.6, relwidth=listbox_width, anchor=tk.CENTER)
        
        # Add a label to display the search result message
        self.search_result_label = Label(form_frame, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=15)
        self.search_result_label.grid(column=0, row=5, pady=(10, 10))
        self.after(1000, __init__)
    def locate_vehicle(self):
        vin = self.vin.get()
        #Clear current list
        self.interior_list.delete(0,END)
        self.exterior_list.delete(0,END)
        self.control_list.delete(0,END)
        self.features_list.delete(0,END)
        self.maintenance_list.delete(0,END)
        self.safety_list.delete(0,END)
        self.warranty_list.delete(0,END)
        self.audio_list.delete(0,END)
        self.preform_list.delete(0,END)
        self.package_list.delete(0,END)
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


