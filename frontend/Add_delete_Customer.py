#This File will handle the building and maintaining of the "Maintenance" Entity
from backend.db import connect
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import datetime
import tkinter as tk 
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel

class Vehicle_Sells(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Sales")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Set the geometry of the window to the full size of the screen
        self.geometry(f"{screen_width}x{screen_height}")
        self.configure(bg='#36454F')
        self.connection = connect()
        #Parameters to build the maintenance item
        self.vin = StringVar()
        self.c_name = StringVar()
        self.c_email = StringVar()
        self.e_id = IntVar()
        self.c_addr = StringVar()
        self.phone = IntVar()
        self.year = IntVar()
        self.month = IntVar()
        self.day = IntVar()
        self.value = True

        # Customize the font size for labels and entry fields
        label_font = ("Verdana", 14)
        entry_font = ("Verdana", 14)

        # Define background and foreground colors for labels
        bg_color = "#36454F"
        fg_color = "white"

        # Build the outline of the date requirements
        self.customer_date_label = Label(self, text="Enter The DOB in day-month-year using numbers: dd-mm-yyyy:", font=label_font, bg=bg_color, fg=fg_color)
        self.customer_date_label.grid(column=0, row=0, padx=(30, 0), pady=(30, 0), sticky="W")

        # Configure the DOB entry fields to be horizontally aligned and the same size
        self.customer_date_entry = Entry(self, width=2, textvariable=self.day, font=entry_font)
        self.customer_date_entry.grid(column=0, row=1, padx=(30, 0), pady=(10, 0), sticky="W")

        self.customer_month_entry = Entry(self, width=2, textvariable=self.month, font=entry_font)
        self.customer_month_entry.grid(column=0, row=1, padx=(90, 0), pady=(10, 0), sticky="W")

        self.customer_year_entry = Entry(self, width=4, textvariable=self.year, font=entry_font)
        self.customer_year_entry.grid(column=0, row=1, padx=(150, 0), pady=(10, 0), sticky="W")

        self.customer_name_label = Label(self, text="Enter Customer Name:", font=label_font, bg=bg_color, fg=fg_color)
        self.customer_name_label.grid(column=0, row=2, padx=(30,0), pady=(30,0), sticky="W")

        self.customer_name_entry = Entry(self, width=40, textvariable=self.c_name, font=entry_font)
        self.customer_name_entry.grid(column=0, row=3, padx=(30, 0), pady=(10, 0), sticky="W")

        self.customer_email_label = Label(self, text="Enter Customer Email:", font=label_font, bg=bg_color, fg=fg_color)
        self.customer_email_label.grid(column=0, row=4, padx=(30,0), pady=(30,0), sticky="W")

        self.customer_email_entry = Entry(self, width=40, textvariable=self.c_email, font=entry_font)
        self.customer_email_entry.grid(column=0, row=5, padx=(30, 0), pady=(10, 0), sticky="W")

        self.customer_addr_label = Label(self, text="Enter Customer Address:", font=label_font, bg=bg_color, fg=fg_color)
        self.customer_addr_label.grid(column=0, row=6, padx=(30,0), pady=(30,0), sticky="W")

        self.customer_addr_entry = Entry(self, width=30, textvariable=self.c_addr, font=entry_font)
        self.customer_addr_entry.grid(column=0, row=7, padx=(30,0), pady=(10,0), sticky="W")

        self.customer_phone_label = Label(self, text="Enter Customer Phone Number:", font=label_font, bg=bg_color, fg=fg_color)
        self.customer_phone_label.grid(column=0, row=8, padx=(30,0), pady=(30,0), sticky="W")

        self.customer_phone_entry = Entry(self, width=30, textvariable=self.phone, font=entry_font)
        self.customer_phone_entry.grid(column=0, row=9, padx=(30,0), pady=(10,0), sticky="W")
                
        self.customer_button = Button(self, text="Create", command=self.create_Customer)
        self.customer_button.grid(column=0, row=10, padx=(30,0), pady=(30,0), sticky="W")

        self.maintenance_button_del = Button(self, text="Delete", command=self.delete_Customer)
        self.maintenance_button_del.grid(column=0, row=10, padx=(120,0), pady=(30,0), sticky="W")


    def create_Customer(self):
        #name, address, email, dob, p_no
        date = datetime.date(self.year.get(), self.month.get(), self.day.get())
        value = add_customer(self.connection, self.c_name, self.c_addr, self.c_email, date, self.phone)
        if value is True:
            self.add_confirmed = Label(self, text="Customer Add Successfully", bg="36454F", fg="white")
            self.add_confirmed.grid(column=2, row=11, padx=(30,0), pady=(30,0))
        else:
            self.add_failed = Label(self, text="Failed To added Customer", bg="36454F", fg="white")
            self.add_failed.grid(column=2, row=11, padx=(30,0), pady=(30,0))
    def delete_Customer(self):
        delete_customer(self.connection, self.c_name, self.c_email)