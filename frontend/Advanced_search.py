from backend.db import connect
#from backend.queries.vehicle_queries import *
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import tkinter as tk
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel, Listbox

handling = ["Power Steering", "Anti-Lock brakes"]
features = ["Keyless", "Cruise Control"]
audioTypes = ["AM", "FM", "SiriusXM"]
transmissionList = ["Automatic", "Manual"]
engineTypeList = ["I4", "V6", "V8"]
paintList = ["Matte", "Metalic", "Lacquer", "Acrylic", "Metalic", "Pearlescent"]
rimList = ["Steel Rims", "Alloy Rims", "Chrome Rims", "Spinners"]
interiorList = ["Cloth Seasts", "Leather Seats", "Automatic Seats", "Manual Seats", "Sun/Moon Roof"]
safteyList = ["Front Airbags", "Passenger Airbags", "Side Airbags", "Automatic Fuel Cutoff", "Collision Warning", "Backup Cameras", "Turning Cameras"]
instrumentsList = ["Hydrosurfing Indicator", "Brake Lights Indicator", "Oil Change Indicator", "Service Indicator"]
comfortList = ["Keyless Locking", "Cruise Control", "Steering Mounted Controls", "Power Windows", "USB System", "Bluetooth System", "Auto Locks", "Navigation System", "Heated Seats", "Remote Startup"]

class Advanced_search(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Vehicle Search")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
# Set the geometry of the window to the full size of the screen
        self.geometry(f"{screen_width}x{screen_height}")
        self.configure(bg="#36454F")  # Set the background color of the window to charcoal gray
        self.vin = StringVar()
        self.make = StringVar()
        self.model = StringVar()
        self.year = IntVar()
        self.transmission = Listbox()
        self.engineType = Listbox()
        self.audio = Listbox()
        self.exteriorPaint = Listbox()
        self.exteriorRims = Listbox()
        self.handling = Listbox()
        self.instruments = StringVar()
        self.interior = StringVar()
        self.features = Listbox()
        self.warrenties = StringVar()
        self.packages = StringVar()
        self.safety = StringVar()
        self.connection = connect()
        self.data = None
        self.stock = 0

        ###Find Vehicle###
        # VIN
        advSearch_vin = Label(self, text="VIN: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_vin.grid(column=0, row=0, pady=(10,0), padx=(10, 0), sticky="W")
        advSearch_vin_entry = Entry(self, width=20, textvariable=self.vin, font=("Verdana", 14))  
        advSearch_vin_entry.grid(column=0, row=0, pady=(10,0), padx=(60, 0), sticky="W")

        # Make
        advSearch_make= Label(self, text="Make: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_make.grid(column=0, row=1, pady=(0,0), padx=(10, 0), sticky="W")
        advSearch_make_entry = tk.Entry(self, width=20, textvariable=self.make, font=("Verdana", 14))
        advSearch_make_entry.grid(column=0, row=1, pady=(0,0), padx=(60, 0), sticky="W")
        
        # Model 
        advSearch_model = Label(self, text="Model: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_model.grid(column=0, row=2, pady=(0,0), padx=(10, 0), sticky="W")
        advSearch_model_entry = tk.Entry(self, width=20, textvariable=self.model, font=("Verdana", 14))
        advSearch_model_entry.grid(column=0, row=2, pady=(0,0), padx=(60, 0), sticky="W")

        # Year
        advSearch_year = Label(self, text="Year: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_year.grid(column=0, row=3, pady=(0,0), padx=(10, 0), sticky="W")
        advSearch_year_entry = tk.Entry(self, width=20, textvariable=self.year, font=("Verdana", 14))
        advSearch_year_entry.grid(column=0, row=3, pady=(0,0), padx=(60, 0), sticky="W")

         ### Interior Features ###

        #Audio
        advSearch_audio = Label(self, text="Audio: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_audio.grid(column=2, row=0, pady=(30,0), padx=(0, 0), sticky="W")
        advSearch_audio_entry = tk.Listbox(self, width=30, height=3, selectmode="single", exportselection=False, font=("Verdana", 10))
        advSearch_audio_entry.grid(column=3, row=0, pady=(30,0), padx=(0, 0), sticky="W")
        for eachItem in range(len(audioTypes)):
            advSearch_audio_entry.insert(END, audioTypes[eachItem])
        self.audio_type = advSearch_audio_entry.get()

        # Interior
        advSearch_interior = Label(self, text="Interior: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_interior.grid(column=2, row=1, pady=(10,0), padx=(0, 0), sticky="W")
        advSearch_interior_entry = tk.Listbox(self, width=30, height=5, selectmode="single", exportselection=False, font=("Verdana", 10))
        advSearch_interior_entry.grid(column=3, row=1, pady=(10,0), padx=(0, 0), sticky="W")
        for eachItem in range(len(interiorList)):
            advSearch_interior_entry.insert(END, interiorList[eachItem])
        self.int_type = advSearch_interior_entry.get()
        # Safety Features
        advSearch_Saftey = Label(self, text="Safety Features: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_Saftey.grid(column=2, row=2, pady=(10,0), padx=(0, 0), sticky="W")
        advSearch_Saftey_entry = tk.Listbox(self, width=30, height=7, selectmode="single", exportselection=False, font=("Verdana", 10))
        advSearch_Saftey_entry.grid(column=3, row=2, pady=(10,0), padx=(0, 0), sticky="W")
        for eachItem in range(len(safteyList)):  # Note: You had a typo in this variable name (safteyList)
            advSearch_Saftey_entry.insert(END, safteyList[eachItem])
        self.safe_type = advSearch_Saftey_entry.get()
        # Comfort Features
        advSearch_comfort = Label(self, text="Comfort Features: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_comfort.grid(column=2, row=3, pady=(10,0), padx=(0, 0), sticky="W")
        advSearch_comfort_entry = tk.Listbox(self, width=30, height=10, selectmode="single", exportselection=False, font=("Verdana", 10))
        advSearch_comfort_entry.grid(column=3, row=3, pady=(10,0), padx=(0, 0), sticky="W")
        for eachItem in range(len(comfortList)):
            advSearch_comfort_entry.insert(END, comfortList[eachItem])
        self.feat_type = advSearch_comfort_entry.get()

        ### Exterior Features ###
        advSearch_extPaint = Label(self, text="External Paint: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_extPaint.grid(column=4, row=0, pady=(30,0), padx=(0, 0), sticky="W")
        advSearch_extPaint_entry = tk.Listbox(self, width=30, height=6, selectmode="multiple", exportselection=False, font=("Verdana", 10))
        advSearch_extPaint_entry.grid(column=5, row=0, pady=(30,0), padx=(0, 0), sticky="W")
        for eachItem in range(len(paintList)):
            advSearch_extPaint_entry.insert(END, paintList[eachItem])
        self.extPaint = advSearch_extPaint_entry.get()
        advSearch_extRim = Label(self, text="Rim Style: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_extRim.grid(column=4, row=1, pady=(10,0), padx=(0, 0), sticky="W")
        advSearch_extRim_entry = tk.Listbox(self, width=30, height=4, selectmode="multiple", exportselection=False, font=("Verdana", 10))
        advSearch_extRim_entry.grid(column=5, row=1, pady=(10,0), padx=(0, 0), sticky="W")
        for eachItem in range(len(rimList)):
            advSearch_extRim_entry.insert(END, rimList[eachItem])
        self.extRim = advSearch_extRim_entry.get()
        # Transmission
        advSearch_transmission = Label(self, text="Transmission: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_transmission.grid(column=4, row=2, pady=(10,0), padx=(0, 0))
        advSearch_transmission_entry = tk.Listbox(self, width=30, height=2, selectmode="single", exportselection=False, font=("Verdana", 10))
        advSearch_transmission_entry.grid(column=5, row=2, pady=(10,0), padx=(0, 0))
        for eachItem in range(len(transmissionList)):
            advSearch_transmission_entry.insert(END, transmissionList[eachItem])
        self.control = advSearch_transmission_entry.get()
        # Engine Type
        advSearch_engineType = Label(self, text="Engine Type: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_engineType.grid(column=4, row=3, pady=(10,0), padx=(0, 0))
        advSearch_engineType_entry = tk.Listbox(self, width=30, height=3, selectmode="single", exportselection=False, font=("Verdana", 10))
        advSearch_engineType_entry.grid(column=5, row=3, pady=(10,0), padx=(0, 0))
        for eachItem in range(len(engineTypeList)):
            advSearch_engineType_entry.insert(END, engineTypeList[eachItem])
        # Extra Packages
        advSearch_packages = Label(self, text="Extra Packages: ", bg="#36454F", fg="white", font=("Verdana", 12))
        advSearch_packages.grid(column=4, row=4, pady=(10,0), padx=(0, 0))
        advSearch_packages_entry = tk.Entry(self, width=30, textvariable=self.packages, font=("Verdana", 10))
        advSearch_packages_entry.grid(column=5, row=4, pady=(10,0), padx=(0, 0))
        self.pack = advSearch_packages_entry.get()
        # Add a label to display the search result message
        self.search_result_label = Label(self, text="", width=30, height=2)
        self.search_result_label.grid(column=0, row=4, columnspan=1, pady=(10, 0))

        # Search button below the extra packages code
        advSearch_button = Button(self, text="Find Vehicle", command=self.find_vehicle_specific)
        advSearch_button.grid(column=1, row=4, pady=(10,0), padx=(20, 0), columnspan=1)
    def find_vehicle_specific(self):
        cur = connection.cursor()
        self.ext_type = self.extPaint + " OR type = " + self.extRim
        find ="""SELECT VIN, Make, Model, Year FROM Vehicle NATURAL JOIN HasInterior NATURAL JOIN Interior WHERE type = %s AND audio_id = %s AND package_id = %s AND VIN IN (SELECT VIN FROM vehicle NATURAL JOIN HasExterior NATURAL JOIN Exterior WHERE type= %s AND VIN IN (SELECT VIN FROM Vehicle NATURAL JOIN HasControls NATURAL JOIN Control WHERE type = %s AND VIN IN (SELECT VIN FROM Vehicle NATURAL JOIN HasFeatures NATURAL JOIN Feature WHERE name = %s AND VIN IN (SELECT VIN FROM Vehicle NATURAL JOIN HasSafety NATURAL JOIN Safety WHERE name = %s))));"""
        cur.execute(find,(self.int_type, self.audio_type, self.pack, self.ext_type, self.control, self.feat_type, self.safe_type,))
        return cur.fetchall()