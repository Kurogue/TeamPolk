from backend.db import connect
#from backend.queries.vehicle_queries import *
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel

class Vehicle_add_delete(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Vehicle Add/Delete")
        self.configure(bg='#36454F')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
# Set the geometry of the window to the full size of the screen
        self.geometry(f"{screen_width}x{screen_height}")
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
        self.stock = StringVar()
        self.int_lst = StringVar()
        self.ext_lst = StringVar()
        self.safe_lst = StringVar()
        self.warr_lst = StringVar()
        self.feat_lst = StringVar()
        self.control_lst = StringVar()
        self.lot = StringVar()
        self.spot = IntVar()

        addVehicle_vin = Label(self, text="VIN: ", bg='#36454F', fg='white')
        addVehicle_vin.grid(column=0, row=0, pady=(150,0), padx=(150, 0))
        addVehicle_vin_entry = Entry(self, width=30, textvariable=self.vin)  
        addVehicle_vin_entry.grid(column=1, row=0, pady=(150,0), padx=(0, 150))
        
        self.vin_validation_label = Label(self, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.vin_validation_label.grid(column=1, row=1, pady=(37.5, 0,))
        
        addVehicle_make= Label(self, text="Make: ", bg='#36454F', fg='white')
        addVehicle_make.grid(column=0, row=2, pady=(37.5,0), padx=(150, 0))
        addVehicle_make_entry = tk.Entry(self, width=30, textvariable=self.make)
        addVehicle_make_entry.grid(column=1, row=2, pady=(37.5,0), padx=(0, 150))

        self.make_validation_label = Label(self, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.make_validation_label.grid(column=1, row=3, pady=(37.5, 0,))

        addVehicle_model = Label(self, text="Model: ", bg='#36454F', fg='white')
        addVehicle_model.grid(column=0, row=4, pady=(37.5,0), padx=(150, 0))
        addVehicle_model_entry = tk.Entry(self, width=30, textvariable=self.model)
        addVehicle_model_entry.grid(column=1, row=4, pady=(37.5,0), padx=(0, 150))

        self.model_validation_label = Label(self, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.model_validation_label.grid(column=1, row=5, pady=(37.5, 0,))

        addVehicle_year = Label(self, text="Year: ", bg='#36454F', fg='white')
        addVehicle_year.grid(column=0, row=6, pady=(37.5,0), padx=(150, 0))
        addVehicle_year_entry = tk.Entry(self, width=30, textvariable=self.year)
        addVehicle_year_entry.grid(column=1, row=6, pady=(37.5,0), padx=(0, 150))

        self.year_validation_label = Label(self, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.year_validation_label.grid(column=1, row=7, pady=(37.5, 0,))

        addVehicle_mileage = Label(self, text="Mileage: ", bg='#36454F', fg='white')
        addVehicle_mileage.grid(column=0, row=8, pady=(37.5,0), padx=(150, 0))
        addVehicle_mileage_entry = tk.Entry(self, width=30, textvariable=self.mileage)
        addVehicle_mileage_entry.grid(column=1, row=8, pady=(37.5,0), padx=(0, 150))

        addVehicle_package = Label(self, text="Package ID: ", bg='#36454F', fg='white')
        addVehicle_package.grid(column=0, row=9, pady=(37.5,0), padx=(150, 0))
        addVehicle_package_entry = tk.Entry(self, width=30, textvariable=self.package_id)
        addVehicle_package_entry.grid(column=1, row=9, pady=(37.5,0), padx=(0, 150))

        addVehicle_audio = Label(self, text="Audio ID: ", bg='#36454F', fg='white')
        addVehicle_audio.grid(column=0, row=10, pady=(37.5,0), padx=(150, 0))
        addVehicle_audio_entry = tk.Entry(self, width=30, textvariable=self.audio_id)
        addVehicle_audio_entry.grid(column=1, row=10, pady=(37.5,0), padx=(0, 150))

        addVehicle_preformance = Label(self, text="Preformance ID: ", bg='#36454F', fg='white')
        addVehicle_preformance.grid(column=0, row=11, pady=(37.5,0), padx=(150, 0))
        addVehicle_preformance_entry = tk.Entry(self, width=30, textvariable=self.preform_id)
        addVehicle_preformance_entry.grid(column=1, row=11, pady=(37.5,0), padx=(0, 150))

        addVehicle_interior = Label(self, text="Interior IDs: ", bg='#36454F', fg='white')
        addVehicle_interior.grid(column=2, row=0, pady=(150,0), padx=(150, 0))
        addVehicle_interior_entry = tk.Entry(self, width=30, textvariable=self.int_lst)
        addVehicle_interior_entry.grid(column=3, row=0, pady=(150,0), padx=(0, 150))

        addVehicle_exterior = Label(self, text="Exterior IDs: ", bg='#36454F', fg='white')
        addVehicle_exterior.grid(column=2, row=1, pady=(37.5,0), padx=(150, 0))
        addVehicle_exterior_entry = tk.Entry(self, width=30, textvariable=self.ext_lst)
        addVehicle_exterior_entry.grid(column=3, row=1, pady=(37.5,0), padx=(0, 150))

        addVehicle_safety = Label(self, text="Safety IDs: ", bg='#36454F', fg='white')
        addVehicle_safety.grid(column=2, row=2, pady=(37.5,0), padx=(150, 0))
        addVehicle_safety_entry = tk.Entry(self, width=30, textvariable=self.safe_lst)
        addVehicle_safety_entry.grid(column=3, row=2, pady=(37.5,0), padx=(0, 150))

        addVehicle_warranty = Label(self, text="Warranty IDs: ", bg='#36454F', fg='white')
        addVehicle_warranty.grid(column=2, row=3, pady=(37.5,0), padx=(150, 0))
        addVehicle_year_entry = tk.Entry(self, width=30, textvariable=self.warr_lst)
        addVehicle_year_entry.grid(column=3, row=3, pady=(37.5,0), padx=(0, 150))

        addVehicle_feature = Label(self, text="Features IDs: ", bg='#36454F', fg='white')
        addVehicle_feature.grid(column=2, row=4, pady=(37.5,0), padx=(150, 0))
        addVehicle_feature_entry = tk.Entry(self, width=30, textvariable=self.feat_lst)
        addVehicle_feature_entry.grid(column=3, row=4, pady=(37.5,0), padx=(0, 150))

        addVehicle_control = Label(self, text="Control Type IDs: ", bg='#36454F', fg='white')
        addVehicle_control.grid(column=2, row=5, pady=(37.5,0), padx=(150, 0))
        addVehicle_control_entry = tk.Entry(self, width=30, textvariable=self.control_lst)
        addVehicle_control_entry.grid(column=3, row=5, pady=(37.5,0), padx=(0, 150))

        addVehicle_location = Label(self, text="Is it in stock? Enter Yes or No: ", bg='#36454F', fg='white')
        addVehicle_location.grid(column=2, row=6, pady=(37.5,0), padx=(150, 0))
        addVehicle_location_box = tk.Entry(self, width=30, textvariable=self.stock)
        addVehicle_location_box.grid(column=3, row=6, pady=(37.5,0), padx=(0, 150))
        
        self.stock_validation_label = Label(self, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.stock_validation_label.grid(column=3, row=7, pady=(10, 10))
        
        addVehicle_lot = Label(self, text="Lot #: ", bg='#36454F', fg='white')
        addVehicle_lot.grid(column=2, row=8, pady=(37.5,0), padx=(150, 0))
        addVehicle_lot_entry = tk.Entry(self, width=30, textvariable=self.lot)
        addVehicle_lot_entry.grid(column=3, row=8, pady=(37.5,0), padx=(0, 150))

        addVehicle_spot = Label(self, text="Space #: ", bg='#36454F', fg='white')
        addVehicle_spot.grid(column=2, row=9, pady=(37.5,0), padx=(150, 0))
        addVehicle_spot_entry = tk.Entry(self, width=30, textvariable=self.spot)
        addVehicle_spot_entry.grid(column=3, row=9, pady=(37.5,0), padx=(0, 150))

        addVehicle_button = Button(self, text="Add Vehicle", command=self.add_vehicle)
        addVehicle_button.grid(column=2, row=10, pady=(37.5,0), padx=(150, 0))
        
        deleteVehicle_button = Button(self, text="Delete Vehicle", command=self.delete_vehicle)
        deleteVehicle_button.grid(column=3, row=10, pady=(37.5,0), padx=(150, 0))

    def add_vehicle(self):
        #add_vehicle(self.connection, self.vin, self.make, self.model, self.year, self.mileage, self.package_id, self.audio_id, self.preform_id, self.int_id, self.ext_id, self.safe_id, self.warr_no, self.feat_id, self.contr_id, self.stock)
        if len(self.vin.get()) != 17 or self.vin.get().isalnum() is False:
            vin_error = f"VIN IS IN INCORRECT FORMATION: MUST BE 17 characters long\n and only use a-z or 0-9 values"
            self.vin_validation_label.config(text=vin_error)   
            return
        if self.make.get() is None:
            make_error = f"Make can't be empty"
            self.make_validation_label.config(text=make_error) 
            return
        if self.model.get() is None:
            model_error = f"Model can't be empty"
            self.model_validation_label.config(text=model_error) 
            return
        if self.year.get() is None:
            year_error = f"YEAR MUST BE in range from 0 to 9999 can't be empty"
            self.year_validation_label.config(text=year_error) 
            return
        if self.stock.get().lower() != 'yes' and self.stock.get().lower() != 'no':
            instock_error = f"ERROR PLEASE ENTER A YES OR NO"
            self.stock_validation_label.config(text=instock_error)
            return
        else:
            add_vehicle(self.connection, self.vin.get().lower(), self.make.get(), self.model.get(), self.year.get(), self.mileage.get(), self.package_id.get(), self.audio_id.get(), self.preform_id.get(),  self.stock.get(), self.lot.get(), self.spot.get())
            self.i_list = self.int_lst.get().split(',')
            self.e_list = self.ext_lst.get().split(',')
            self.s_list = self.safe_lst.get().split(',')
            self.w_list = self.warr_lst.get().split(',')
            self.f_list = self.feat_lst.get().split(',')
            self.c_list = self.control_lst.get().split(',')
        
            for i in self.i_list:
                add_hasInterior(self.connection, self.vin.get(), int(i))
            for e in self.e_list:
                add_hasExterior(self.connection, self.vin.get(), int(e))
            for s in self.s_list:
                add_hasSafety(self.connection, self.vin.get(), int(s))
            for w in self.w_list:
                add_hasWarranty(self.connection, self.vin.get(), int(w))
            for f in self.f_list:
                add_hasFeature(self.connection, self.vin.get(), int(f))
            for c in self.c_list:
                add_hasControl(self.connection, self.vin.get(), int(c))
            self.connection = connect() #restablish connection
        
    def delete_vehicle(self):
        delete_vehicle(self.connection, self.vin.get())