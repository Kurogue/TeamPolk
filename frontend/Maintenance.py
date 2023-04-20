#This File will handle the building and maintaining of the "Maintenance" Entity
from backend.db import connect
from backend.queries.add_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import datetime
import tkinter as tk 
from tkinter import ttk
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel


class Add_delete_Maintenance(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Maintenance")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Set the geometry of the window to the full size of the screen
        self.geometry(f"{screen_width}x{screen_height}")
        self.configure(bg='#36454F')
        self.connection = connect()
        #Parameters to build the maintenance item
        self.main_no = IntVar()
        self.year = IntVar()
        self.month = IntVar()
        self.day = IntVar()
        self.service = StringVar()
        self.e_id = IntVar()
        self.date = datetime.date.today()
        self.vin = StringVar()

        # Customize the font size for labels and entry fields
        label_font = ("Verdana", 14)
        entry_font = ("Verdana", 14)
        bg_color = "#36454F"
        fg_color = "white"

        # Build the outline of the date requirements
        self.maintenance_date_label = Label(self, text="Enter The date of service using numbers: dd-mm-yyyy:", font=label_font, bg=bg_color, fg=fg_color)
        self.maintenance_date_label.grid(column=0, row=0, padx=(30, 0), pady=(30, 0), sticky="W")

        # Configure the DOB entry fields to be horizontally aligned and the same size
        self.maintenance_date_label_date_entry = Entry(self, width=2, textvariable=self.day, font=entry_font)
        self.maintenance_date_label_date_entry.grid(column=1, row=0, padx=(10, 0), pady=(30, 0), sticky="W")

        self.maintenance_date_label_month_entry = Entry(self, width=2, textvariable=self.month, font=entry_font)
        self.maintenance_date_label_month_entry.grid(column=2, row=0, padx=(10, 0), pady=(30, 0), sticky="W")

        self.maintenance_date_label_year_entry = Entry(self, width=4, textvariable=self.year, font=entry_font)
        self.maintenance_date_label_year_entry.grid(column=3, row=0, padx=(10, 0), pady=(30, 0), sticky="W")

        self.maintenance_number_label = Label(self, text="Enter Maintenance ID: ",
                                            font=label_font, bg=bg_color, fg=fg_color)
        self.maintenance_number_label.grid(column=0, row=1, sticky=W, padx=(30,0), pady=(20,0))
        self.maintenance_number_entry = Entry(self, width=10, textvariable=self.main_no, font=("Helvetica", 12))
        self.maintenance_number_entry.grid(column=1, row=1, sticky=W, padx=(10,0), pady=(20,0), columnspan=3)

        self.maintenance_service_label = Label(self, text="Enter the type of service to perform: ",
                                            font=label_font, bg=bg_color, fg=fg_color)
        self.maintenance_service_label.grid(column=0, row=2, sticky=W, padx=(30,0), pady=(20,0))
        self.maintenance_service_entry = Entry(self, width=20, textvariable=self.service, font=("Helvetica", 12))
        self.maintenance_service_entry.grid(column=1, row=2, sticky=W, padx=(10,0), pady=(20,0), columnspan=3)

        self.maintenance_vin_label = Label(self, text="Enter the VIN of the vehicle being serviced: ",
                                        font=label_font, bg=bg_color, fg=fg_color)
        self.maintenance_vin_label.grid(column=0, row=3, sticky=W, padx=(30,0), pady=(20,0))
        self.maintenance_vin_entry = Entry(self, width=20, textvariable=self.vin, font=("Helvetica", 12))
        self.maintenance_vin_entry.grid(column=1, row=3, sticky=W, padx=(10,0), pady=(20,0), columnspan=3)

        self.maintenance_vin_label = Label(self, text="Enter the Employee id to work on it: ",
                                        font=label_font, bg=bg_color, fg=fg_color)
        self.maintenance_vin_label.grid(column=0, row=4, sticky=W, padx=(30,0), pady=(20,0))
        self.maintenance_vin_entry = Entry(self, width=20, textvariable=self.e_id, font=("Helvetica", 12))
        self.maintenance_vin_entry.grid(column=1, row=4, sticky=W, padx=(10,0), pady=(20,0), columnspan=3)

        self.maintenance_button = Button(self, text="Submit", command=self.create_Maintenance)
        self.maintenance_button.grid(column=0, row=5, sticky=W, padx=(30,0), pady=(20,0))

        self.day_maintenance_listbox = Listbox(self, width=150, height=20)
        self.day_maintenance_listbox.grid(column=0, row=6, padx=(30,0), pady=(30,0))
        self.values = self.all_maintenance_today()
        for i in self.values:
            self.day_maintenance_listbox.insert(tk.END, i)

        self.maintenance_button_del = Button(self, text="Delete", command=self.delete_Maintenance)
        self.maintenance_button_del.grid(column=1, row=6, pady=(20,0), padx=(20,0))
    def all_maintenance_today(self):
        cur = self.connection.cursor()
        date = datetime.date.today()
        find = """SELECT VIN, Make, Model, Year, Service FROM Vehicle NATURAL JOIN HasMaintence NATURAL JOIN Maintenance WHERE Date = %s;"""
        cur.execute(find, (date,))
        return cur.fetchall()
    def create_Maintenance(self):
        #create date object
        self.date = datetime.date(self.year.get(), self.month.get(), self.day.get())
        add_maintenance(self.connection, self.main_no.get(), self.date, self.service.get(), self.e_id.get())
        add_hasMaintenance(self.connection, self.vin.get(), self.main_no.get())

    def delete_Maintenance(self):
        delete_maintenance(self.connection, self.main_no.get())

