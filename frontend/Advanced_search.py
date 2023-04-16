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
        self.geometry("1100x800")
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
        self.connection = connect()
        self.data = None
        self.stock = 0

        # find Vehicle
        advSearch_vin = Label(self, text="VIN: ")
        advSearch_vin.grid(column=0, row=0, pady=(30,0), padx=(150, 0))
        advSearch_vin_entry = Entry(self, width=30, textvariable=self.vin)  
        advSearch_vin_entry.grid(column=1, row=0, pady=(30,0), padx=(0, 150))

        advSearch_make= Label(self, text="Make: ")
        advSearch_make.grid(column=2, row=0, pady=(30,0), padx=(0, 0))
        advSearch_make_entry = tk.Entry(self, width=30, textvariable=self.make)
        advSearch_make_entry.grid(column=3, row=0, pady=(30,0), padx=(0, 0))


        advSearch_model = Label(self, text="Model: ")
        advSearch_model.grid(column=0, row=1, pady=(10,0), padx=(150, 0))
        advSearch_model_entry = tk.Entry(self, width=30, textvariable=self.model)
        advSearch_model_entry.grid(column=1, row=1, pady=(10,0), padx=(0, 150))

        advSearch_year = Label(self, text="Year: ")
        advSearch_year.grid(column=2, row=1, pady=(10,0), padx=(0, 0))
        advSearch_year_entry = tk.Entry(self, width=30, textvariable=self.year)
        advSearch_year_entry.grid(column=3, row=1, pady=(10,0), padx=(0, 0))


        advSearch_transmission = Label(self, text="Transmission: ")
        advSearch_transmission.grid(column=0, row=2, pady=(10,0), padx=(150, 0))
        advSearch_transmission_entry = tk.Listbox(self, width=30, height=2, selectmode="single", exportselection=False)
        advSearch_transmission_entry.grid(column=1, row=2, pady=(10,0), padx=(0, 150))
        for eachItem in range(len(transmissionList)):
            advSearch_transmission_entry.insert(END, transmissionList[eachItem])

        advSearch_engineType = Label(self, text="Engine Type: ")
        advSearch_engineType.grid(column=2, row=2, pady=(10,0), padx=(0, 0))
        advSearch_engineType_entry = tk.Listbox(self, width=30, height=3, selectmode="single", exportselection=False)
        advSearch_engineType_entry.grid(column=3, row=2, pady=(10,0), padx=(0, 0))
        for eachItem in range(len(engineTypeList)):
            advSearch_engineType_entry.insert(END, engineTypeList[eachItem])


        advSearch_audio = Label(self, text="Audio: ")
        advSearch_audio.grid(column=0, row=3, pady=(10,0), padx=(150, 0))
        advSearch_audio_entry = tk.Listbox(self, width=30, height=3, selectmode="multiple", exportselection=False)
        advSearch_audio_entry.grid(column=1, row=3, pady=(10,0), padx=(0, 150))
        for eachItem in range(len(audioTypes)):
            advSearch_audio_entry.insert(END, audioTypes[eachItem])

        advSearch_extPaint = Label(self, text="External Paint: ")
        advSearch_extPaint.grid(column=2, row=3, pady=(10,0), padx=(0, 0))
        advSearch_extPaint_entry = tk.Listbox(self, width=30, height=6, selectmode="multiple", exportselection=False)
        advSearch_extPaint_entry.grid(column=3, row=3, pady=(10,0), padx=(0, 0))
        for eachItem in range(len(paintList)):
            advSearch_extPaint_entry.insert(END, paintList[eachItem])


        advSearch_extRim = Label(self, text="Rim Style: ")
        advSearch_extRim.grid(column=0, row=4, pady=(10,0), padx=(150, 0))
        advSearch_extRim_entry = tk.Listbox(self, width=30, height=4, selectmode="multiple", exportselection=False)
        advSearch_extRim_entry.grid(column=1, row=4, pady=(10,0), padx=(0, 150))
        for eachItem in range(len(rimList)):
            advSearch_extRim_entry.insert(END, rimList[eachItem])

        advSearch_interior = Label(self, text="Interior: ")
        advSearch_interior.grid(column=2, row=4, pady=(10,0), padx=(0, 0))
        advSearch_interior_entry = tk.Listbox(self, width=30, height=5, selectmode="multiple", exportselection=False)
        advSearch_interior_entry.grid(column=3, row=4, pady=(10,0), padx=(0, 0))
        for eachItem in range(len(interiorList)):
            advSearch_interior_entry.insert(END, interiorList[eachItem])


        advSearch_Saftey = Label(self, text="Saftey Features: ")
        advSearch_Saftey.grid(column=0, row=5, pady=(10,0), padx=(150, 0))
        advSearch_Saftey_entry = tk.Listbox(self, width=30, height=7, selectmode="multiple", exportselection=False)
        advSearch_Saftey_entry.grid(column=1, row=5, pady=(10,0), padx=(0, 150))
        for eachItem in range(len(safteyList)):
            advSearch_Saftey_entry.insert(END, safteyList[eachItem])

        advSearch_instrument = Label(self, text="Instruments: ")
        advSearch_instrument.grid(column=2, row=5, pady=(10,0), padx=(0, 0))
        advSearch_instrument_entry = tk.Listbox(self, width=30, height=4, selectmode="multiple", exportselection=False)
        advSearch_instrument_entry.grid(column=3, row=5, pady=(10,0), padx=(0, 0))
        for eachItem in range(len(instrumentsList)):
            advSearch_instrument_entry.insert(END, instrumentsList[eachItem])


        advSearch_comfort = Label(self, text="Comfrot Features: ")
        advSearch_comfort.grid(column=0, row=6, pady=(10,0), padx=(150, 0))
        advSearch_comfort_entry = tk.Listbox(self, width=30, height=10, selectmode="multiple", exportselection=False)
        advSearch_comfort_entry.grid(column=1, row=6, pady=(10,0), padx=(0, 150))
        for eachItem in range(len(comfortList)):
            advSearch_comfort_entry.insert(END, comfortList[eachItem])

        advSearch_packages = Label(self, text="Extra Packages: ")
        advSearch_packages.grid(column=2, row=6, pady=(10,0), padx=(0, 0))
        advSearch_packages_entry = tk.Entry(self, width=30, textvariable=self.packages)
        advSearch_packages_entry.grid(column=3, row=6, pady=(10,0), padx=(0, 0))

        # Search button below the extra packages code
        advSearch_button = Button(self, text="Find Vehicle")#, command=self.locate_vehicle)
        advSearch_button.grid(column=0, row=14, pady=(30,0), padx=(150, 0), columnspan=4)

        #  # Add a label to display the search result message
        # self.search_result_label = Label(self, text="")
        # self.search_result_label.grid(column=0, row=6, pady=(37.5, 0))