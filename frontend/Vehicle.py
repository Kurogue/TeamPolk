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

        addVehicle_vin = Label(self, text="VIN: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_vin.grid(column=0, row=0, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_vin_entry = Entry(self, width=30, textvariable=self.vin, font=("Arial", 16, "bold"))  
        addVehicle_vin_entry.grid(column=1, row=0, pady=(10,0), padx=(0, 30), sticky="W")
        
        self.vin_validation_label = Label(self, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.vin_validation_label.grid(column=1, row=1, pady=(20, 0), sticky="W")
        
        addVehicle_make= Label(self, text="Make: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_make.grid(column=0, row=2, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_make_entry = tk.Entry(self, width=30, textvariable=self.make, font=("Arial", 16, "bold"))
        addVehicle_make_entry.grid(column=1, row=2, pady=(10,0), padx=(0, 30), sticky="W")

        self.make_validation_label = Label(self, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.make_validation_label.grid(column=1, row=3, pady=(20, 0,), sticky="W")

        addVehicle_model = Label(self, text="Model: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_model.grid(column=0, row=4, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_model_entry = tk.Entry(self, width=30, textvariable=self.model, font=("Arial", 16, "bold"))
        addVehicle_model_entry.grid(column=1, row=4, pady=(10,0), padx=(0, 30), sticky="W")

        self.model_validation_label = Label(self, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.model_validation_label.grid(column=1, row=5, pady=(20, 0,), sticky="W")

        addVehicle_year = Label(self, text="Year: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_year.grid(column=0, row=6, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_year_entry = tk.Entry(self, width=30, textvariable=self.year, font=("Arial", 16, "bold"))
        addVehicle_year_entry.grid(column=1, row=6, pady=(10,0), padx=(0, 30), sticky="W")

        self.year_validation_label = Label(self, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.year_validation_label.grid(column=1, row=7, pady=(20, 0,), sticky="W")

        addVehicle_mileage = Label(self, text="Mileage: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_mileage.grid(column=0, row=8, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_mileage_entry = tk.Entry(self, width=30, textvariable=self.mileage, font=("Arial", 16, "bold"))
        addVehicle_mileage_entry.grid(column=1, row=8, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_package = Label(self, text="Package ID: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_package.grid(column=0, row=9, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_package_entry = tk.Entry(self, width=30, textvariable=self.package_id, font=("Arial", 16, "bold"))
        addVehicle_package_entry.grid(column=1, row=9, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_audio = Label(self, text="Audio ID: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_audio.grid(column=0, row=10, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_audio_entry = tk.Entry(self, width=30, textvariable=self.audio_id, font=("Arial", 16, "bold"))
        addVehicle_audio_entry.grid(column=1, row=10, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_preformance = Label(self, text="Preformance ID: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_preformance.grid(column=0, row=11, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_preformance_entry = tk.Entry(self, width=30, textvariable=self.preform_id, font=("Arial", 16, "bold"))
        addVehicle_preformance_entry.grid(column=1, row=11, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_interior = Label(self, text="Interior IDs: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_interior.grid(column=2, row=0, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_interior_entry = tk.Entry(self, width=30, textvariable=self.int_lst, font=("Arial", 16, "bold"))
        addVehicle_interior_entry.grid(column=3, row=0, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_exterior = Label(self, text="Exterior IDs: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_exterior.grid(column=2, row=1, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_exterior_entry = tk.Entry(self, width=30, textvariable=self.ext_lst, font=("Arial", 16, "bold"))
        addVehicle_exterior_entry.grid(column=3, row=1, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_safety = Label(self, text="Safety IDs: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_safety.grid(column=2, row=2, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_safety_entry = tk.Entry(self, width=30, textvariable=self.safe_lst, font=("Arial", 16, "bold"))
        addVehicle_safety_entry.grid(column=3, row=2, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_warranty = Label(self, text="Warranty IDs: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_warranty.grid(column=2, row=3, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_year_entry = tk.Entry(self, width=30, textvariable=self.warr_lst, font=("Arial", 16, "bold"))
        addVehicle_year_entry.grid(column=3, row=3, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_feature = Label(self, text="Features IDs: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_feature.grid(column=2, row=4, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_feature_entry = tk.Entry(self, width=30, textvariable=self.feat_lst, font=("Arial", 16, "bold"))
        addVehicle_feature_entry.grid(column=3, row=4, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_control = Label(self, text="Control Type IDs: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_control.grid(column=2, row=5, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_control_entry = tk.Entry(self, width=30, textvariable=self.control_lst, font=("Arial", 16, "bold"))
        addVehicle_control_entry.grid(column=3, row=5, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_location = Label(self, text="Is it in stock? Enter Yes or No: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_location.grid(column=2, row=6, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_location_box = tk.Entry(self, width=30, textvariable=self.stock, font=("Arial", 16, "bold"))
        addVehicle_location_box.grid(column=3, row=6, pady=(10,0), padx=(0, 30), sticky="W")
        
        self.stock_validation_label = Label(self, text="", bg='#36454F', fg='white', font=("Arial", 16, "bold"), width=20)
        self.stock_validation_label.grid(column=3, row=7, pady=(10, 10), sticky="W")
        
        addVehicle_lot = Label(self, text="Lot #: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_lot.grid(column=2, row=8, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_lot_entry = tk.Entry(self, width=30, textvariable=self.lot, font=("Arial", 16, "bold"))
        addVehicle_lot_entry.grid(column=3, row=8, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_spot = Label(self, text="Space #: ", bg='#36454F', fg='white', font=("Arial", 16, "bold"))
        addVehicle_spot.grid(column=2, row=9, pady=(10,0), padx=(30, 0), sticky="W")
        addVehicle_spot_entry = tk.Entry(self, width=30, textvariable=self.spot, font=("Arial", 16, "bold"))
        addVehicle_spot_entry.grid(column=3, row=9, pady=(10,0), padx=(0, 30), sticky="W")

        addVehicle_button = Button(self, text="Add Vehicle", command=self.add_vehicle)
        addVehicle_button.grid(column=2, row=10, pady=(20,0), padx=(30, 0))
        
        deleteVehicle_button = Button(self, text="Delete Vehicle", command=self.delete_vehicle)
        deleteVehicle_button.grid(column=3, row=10, pady=(20,0), padx=(30, 0))

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
            value = add_vehicle(self.connection, self.vin.get(), self.make.get(), self.model.get(), self.year.get(), self.mileage.get(), self.package_id.get(), self.audio_id.get(), self.preform_id.get(),  self.stock.get(), self.lot.get(), self.spot.get())
            if value is False:
                self.failed_vehicle = Label(self, text="Failed to add Vehicle to DB")
                self.failed_vehicle.grid(column=1, row=12, padx=(20,0), pady=(20,0))
                return
            self.i_list = self.int_lst.get().split(',')
            self.e_list = self.ext_lst.get().split(',')
            self.s_list = self.safe_lst.get().split(',')
            self.w_list = self.warr_lst.get().split(',')
            self.f_list = self.feat_lst.get().split(',')
            self.c_list = self.control_lst.get().split(',')
        
            for i in self.i_list:
                value = add_hasInterior(self.connection, self.vin.get(), int(i))
                if value is not True:
                    self.failed_interior = Label(self, text="Failed to add to HasInterior to DB")
                    self.failed_interior.grid(column=1, row=12, padx=(20,0), pady=(20,0))
                    return
            for e in self.e_list:
                value = add_hasExterior(self.connection, self.vin.get(), int(e))
                if value is not True:
                    self.failed_interior = Label(self, text="Failed to add to HasExterior to DB")
                    self.failed_interior.grid(column=1, row=12, padx=(20,0), pady=(20,0))
                    return
            for s in self.s_list:
                value = add_hasSafety(self.connection, self.vin.get(), int(s))
                if value is not True:
                    self.failed_interior = Label(self, text="Failed to add to HasSafety to DB")
                    self.failed_interior.grid(column=1, row=12, padx=(20,0), pady=(20,0))
                    return
            for w in self.w_list:
                value = add_hasWarranty(self.connection, self.vin.get(), int(w))
                if value is not True:
                    self.failed_interior = Label(self, text="Failed to add to HasWarranty to DB")
                    self.failed_interior.grid(column=1, row=12, padx=(20,0), pady=(20,0))
                    return
            for f in self.f_list:
                value = add_hasFeature(self.connection, self.vin.get(), int(f))
                if value is not True:
                    self.failed_interior = Label(self, text="Failed to add to HasFeatures to DB")
                    self.failed_interior.grid(column=1, row=12, padx=(20,0), pady=(20,0))
                    return
            for c in self.c_list:
                value = add_hasControl(self.connection, self.vin.get(), int(c))
                if value is not True:
                    self.failed_interior = Label(self, text="Failed to add to HasControl to DB")
                    self.failed_interior.grid(column=1, row=12, padx=(20,0), pady=(20,0))
                    return
            self.connection = connect() #restablish connection
            self.Success = Label(self, text="Succeeded Adding Vehicle")
            self.Success.grid(column=1, row=12, padx=(20,0), pady=(20,0))
    def delete_vehicle(self):
        value = delete_vehicle(self.connection, self.vin.get())
        if value is not True:
            self.failed_delete = Label(self, text="Failed to Delete From DB")
            self.failed_delete.grid(column=1, row=12, padx=(20,0), pady=(20,0))
        else:
            self.succeed_delete = Label(self, text="Successfully Deleted From DB")
            self.succeed_delete.grid(column=1, row=12, padx=(20,0), pady=(20,0))