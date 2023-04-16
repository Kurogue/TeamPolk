from backend.db import connect
#from backend.queries.vehicle_queries import *
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import tkinter as tk
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel, Listbox, OptionMenu

handling = ["Power Steering", "Anti-Lock brakes"]
features = ["Keyless", "Cruise Control"]
audioTypes = ["AM", "FM", "SiriusXM"]
transmissionList = ["Automatic", "Manual"]

class Advanced_search(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Vehicle Search")
        self.geometry("600x600")
        self.vin = StringVar()
        self.make = StringVar()
        self.model = StringVar()
        self.year = IntVar()

        self.transmission = Listbox()
        self.engineType = Listbox()
        
        self.handling = Listbox()
        
        self.instruments = StringVar()
        self.exterior = StringVar()
        self.interior = StringVar()
        
        self.audio = Listbox()
        self.features = Listbox()
        self.warrenties = StringVar()

        self.connection = connect()
        self.data = None
        self.stock = 0

        # find Vehicle
        advSearch_vin = Label(self, text="VIN: ")
        advSearch_vin.grid(column=0, row=0, pady=(150,0), padx=(150, 0))
        advSearch_vin_entry = Entry(self, width=30, textvariable=self.vin)  
        advSearch_vin_entry.grid(column=1, row=0, pady=(150,0), padx=(0, 150))

        advSearch_make= Label(self, text="Make: ")
        advSearch_make.grid(column=0, row=1, pady=(37.5,0), padx=(150, 0))
        advSearch_make_entry = tk.Entry(self, width=30, textvariable=self.make)
        advSearch_make_entry.grid(column=1, row=1, pady=(37.5,0), padx=(0, 150))

        advSearch_model = Label(self, text="Model: ")
        advSearch_model.grid(column=0, row=2, pady=(37.5,0), padx=(150, 0))
        advSearch_model_entry = tk.Entry(self, width=30, textvariable=self.model)
        advSearch_model_entry.grid(column=1, row=2, pady=(37.5,0), padx=(0, 150))

        advSearch_year = Label(self, text="Year: ")
        advSearch_year.grid(column=0, row=3, pady=(37.5,0), padx=(150, 0))
        advSearch_year_entry = tk.Entry(self, width=30, textvariable=self.year)
        advSearch_year_entry.grid(column=1, row=3, pady=(37.5,0), padx=(0, 150))

        advSearch_audio = Label(self, text="Audio: ")
        advSearch_audio.grid(column=0, row=4, pady=(37.5,0), padx=(150, 0))
        advSearch_audio_entry = tk.Listbox(self, width=30, height=3, selectmode="multiple")
        advSearch_audio_entry.grid(column=1, row=4, pady=(37.5,0), padx=(0, 150))
        for eachItem in range(len(audioTypes)):
            advSearch_audio_entry.insert(END, audioTypes[eachItem])

        advSearch_transmission = Label(self, text="Transmission: ")
        advSearch_transmission.grid(column=0, row=5, pady=(37.5,0), padx=(150, 0))
        advSearch_transmission_entry = tk.Listbox(self, width=30, height=2, selectmode="single")
        advSearch_transmission_entry.grid(column=1, row=5, pady=(37.5,0), padx=(0, 150))
        for eachItem in range(len(transmissionList)):
            advSearch_transmission_entry.insert(END, transmissionList[eachItem])

        # advSearch_button = Button(self, text="Find Vehicle", command=self.locate_vehicle)
        # advSearch_button.grid(column=0, row=5, pady=(37.5,0), padx=(150, 0))

        #  # Add a label to display the search result message
        # self.search_result_label = Label(self, text="")
        # self.search_result_label.grid(column=0, row=6, pady=(37.5, 0))