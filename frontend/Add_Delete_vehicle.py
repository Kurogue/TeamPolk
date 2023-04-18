from backend.db import connect
#from backend.queries.vehicle_queries import *
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import tkinter as tk
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel

class Vehicle_add_delete(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Vehicle Search")
        self.geometry("900x900")
        self.vin = StringVar()
        self.make = StringVar()
        self.model = StringVar()
        self.year = IntVar()
        self.mileage = IntVar()
        self.package_id = IntVar()
        self.audio_id = IntVar()
        self.preform_id = IntVar()
        self.int_id = IntVar()
        self.ext_id = IntVar()
        self.safe_id = IntVar()
        self.warr_no = IntVar()
        self.feat_id = IntVar()
        self.contr_id = IntVar()
        self.connection = connect()
        self.data = None
        self.stock = 0
        self.int_lst = StringVar()
        self.ext_lst = StringVar()
        self.safe_lst = StringVar()
        self.warr_lst = StringVar()
        self.feat_lst = StringVar()
        self.control_lst = StringVar()
        self.lot = IntVar()
        self.spot = IntVar()
        #Add Vehicle
        addVehicle_vin = Label(self, text="VIN: ")
        addVehicle_vin.grid(column=0, row=0, pady=(150,0), padx=(150, 0))
        addVehicle_vin_entry = Entry(self, width=30, textvariable=self.vin)  
        addVehicle_vin_entry.grid(column=1, row=0, pady=(150,0), padx=(0, 150))

        addVehicle_make= Label(self, text="Make: ")
        addVehicle_make.grid(column=0, row=1, pady=(37.5,0), padx=(150, 0))
        addVehicle_make_entry = tk.Entry(self, width=30, textvariable=self.make)
        addVehicle_make_entry.grid(column=1, row=1, pady=(37.5,0), padx=(0, 150))

        addVehicle_model = Label(self, text="Model: ")
        addVehicle_model.grid(column=0, row=2, pady=(37.5,0), padx=(150, 0))
        addVehicle_model_entry = tk.Entry(self, width=30, textvariable=self.model)
        addVehicle_model_entry.grid(column=1, row=2, pady=(37.5,0), padx=(0, 150))

        addVehicle_year = Label(self, text="Year: ")
        addVehicle_year.grid(column=0, row=3, pady=(37.5,0), padx=(150, 0))
        addVehicle_year_entry = tk.Entry(self, width=30, textvariable=self.year)
        addVehicle_year_entry.grid(column=1, row=3, pady=(37.5,0), padx=(0, 150))

        addVehicle_mileage = Label(self, text="Mileage: ")
        addVehicle_mileage.grid(column=0, row=4, pady=(37.5,0), padx=(150, 0))
        addVehicle_mileage_entry = tk.Entry(self, width=30, textvariable=self.mileage)
        addVehicle_mileage_entry.grid(column=1, row=4, pady=(37.5,0), padx=(0, 150))

        addVehicle_package = Label(self, text="Package ID: ")
        addVehicle_package.grid(column=0, row=5, pady=(37.5,0), padx=(150, 0))
        addVehicle_package_entry = tk.Entry(self, width=30, textvariable=self.package_id)
        addVehicle_package_entry.grid(column=1, row=5, pady=(37.5,0), padx=(0, 150))

        addVehicle_audio = Label(self, text="Audio ID: ")
        addVehicle_audio.grid(column=0, row=6, pady=(37.5,0), padx=(150, 0))
        addVehicle_audio_entry = tk.Entry(self, width=30, textvariable=self.audio_id)
        addVehicle_audio_entry.grid(column=1, row=6, pady=(37.5,0), padx=(0, 150))

        addVehicle_preformance = Label(self, text="Preformance ID: ")
        addVehicle_preformance.grid(column=0, row=7, pady=(37.5,0), padx=(150, 0))
        addVehicle_preformance_entry = tk.Entry(self, width=30, textvariable=self.preform_id)
        addVehicle_preformance_entry.grid(column=1, row=7, pady=(37.5,0), padx=(0, 150))

        addVehicle_interior = Label(self, text="Interior IDs: ")
        addVehicle_interior.grid(column=0, row=8, pady=(37.5,0), padx=(150, 0))
        addVehicle_interior_entry = tk.Entry(self, width=30, textvariable=self.int_lst)
        addVehicle_interior_entry.grid(column=1, row=8, pady=(37.5,0), padx=(0, 150))

        addVehicle_exterior = Label(self, text="Exterior IDs: ")
        addVehicle_exterior.grid(column=0, row=9, pady=(37.5,0), padx=(150, 0))
        addVehicle_exterior_entry = tk.Entry(self, width=30, textvariable=self.ext_lst)
        addVehicle_exterior_entry.grid(column=1, row=9, pady=(37.5,0), padx=(0, 150))

        addVehicle_safety = Label(self, text="Safety IDs: ")
        addVehicle_safety.grid(column=0, row=10, pady=(37.5,0), padx=(150, 0))
        addVehicle_safety_entry = tk.Entry(self, width=30, textvariable=self.safe_lst)
        addVehicle_safety_entry.grid(column=1, row=10, pady=(37.5,0), padx=(0, 150))

        addVehicle_warranty = Label(self, text="Warranty IDs: ")
        addVehicle_warranty.grid(column=0, row=11, pady=(37.5,0), padx=(150, 0))
        addVehicle_year_entry = tk.Entry(self, width=30, textvariable=self.warr_lst)
        addVehicle_year_entry.grid(column=1, row=11, pady=(37.5,0), padx=(0, 150))

        addVehicle_feature = Label(self, text="Features IDs: ")
        addVehicle_feature.grid(column=0, row=12, pady=(37.5,0), padx=(150, 0))
        addVehicle_feature_entry = tk.Entry(self, width=30, textvariable=self.feat_lst)
        addVehicle_feature_entry.grid(column=1, row=12, pady=(37.5,0), padx=(0, 150))

        addVehicle_control = Label(self, text="Control Type IDs: ")
        addVehicle_control.grid(column=0, row=13, pady=(37.5,0), padx=(150, 0))
        addVehicle_control_entry = tk.Entry(self, width=30, textvariable=self.control_lst)
        addVehicle_control_entry.grid(column=1, row=13, pady=(37.5,0), padx=(0, 150))


        addVehicle_lot = Label(self, text="Lot #: ")
        addVehicle_lot.grid(column=0, row=14, pady=(37.5,0), padx=(150, 0))
        addVehicle_lot_entry = tk.Entry(self, width=30, textvariable=self.lot)
        addVehicle_lot_entry.grid(column=1, row=14, pady=(37.5,0), padx=(0, 150))

        
        addVehicle_spot = Label(self, text="Space #: ")
        addVehicle_spot.grid(column=0, row=15, pady=(37.5,0), padx=(150, 0))
        addVehicle_spot_entry = tk.Entry(self, width=30, textvariable=self.spot)
        addVehicle_spot_entry.grid(column=1, row=15, pady=(37.5,0), padx=(0, 150))

        addVehicle_button = Button(self, text="Add Vehicle", command=self.add_vehicle)
        addVehicle_button.grid(column=0, row=16, pady=(37.5,0), padx=(150, 0))
        
        deleteVehicle_button = Button(self, text="Delete Vehicle", command=self.delete_vehicle)
        deleteVehicle_button.grid(column=1, row=16, pady=(37.5,0), padx=(150, 0))
    def add_vehicle(self):
        add_vehicle(self.connection, self.vin, self.make, self.model, self.year, self.mileage, self.package_id, self.audio_id, self.preform_id, self.int_id, self.ext_id, self.safe_id, self.warr_no, self.feat_id, self.contr_id, self.stock)
        self.i_list = self.int_lst.split(',')
        self.e_list = self.ext_lst.split(',')
        self.s_list = self.safe_lst.split(',')
        self.w_list = self.add_vehiclewarr_lst.split(',')
        self.f_list = self.feat_lst.split(',')
        self.c_list = self.control_lst.split(',')

        add_vehicle(self.connection, self.vin, self.make, self.model, self.year, self.mileage, self.package_id, self.audio_id, self.preform_id,  self.stock, self.lot, self.spot)
        self.i_list = self.int_lst.split(',')
        self.e_list = self.ext_lst.split(',')
        self.s_list = self.safe_lst.split(',')
        self.w_list = self.warr_lst.split(',')
        self.f_list = self.feat_lst.split(',')
        self.c_list = self.control_lst.split(',')

        for i in self.i_list:
            add_hasInterior(self.connection, self.vin, int(i))
        for e in self.e_list:
            add_hasExterior(self.connection, self.vin, int(e))
        for s in self.s_list:
            add_hasSafety(self.connection, self.vin, int(s))
        for w in self.w_list:
            add_hasWarranty(self.connection, self.vin, int(w))
        for f in self.f_list:
            add_hasFeature(self.connection, self.vin, int(f))
        for c in self.c_list:
            add_hasControl(self.connection, self.vin, int(c))

    def delete_vehicle(self):
        delete_vehicle(self.connection, self.vin)