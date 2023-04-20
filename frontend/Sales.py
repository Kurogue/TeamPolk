#This File will handle the building and maintaining of the "Maintenance" Entity
from backend.db import connect
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import datetime
import tkinter as tk 
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel

class Add_delete_Sales(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Sales")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Set the geometry of the window to the full size of the screen
        self.geometry(f"{screen_width}x{screen_height}")
        self.connection = connect()
        self.configure(bg="#36454F")
        #Parameters to build the maintenance item
        self.vin = StringVar()
        self.c_name = StringVar()
        self.c_email = StringVar()
        self.e_id = IntVar()
        self.vin_instock = StringVar()
        self.lot = StringVar()
        self.spot = IntVar()
        label_bg_color = "#36454F"
        label_fg_color = "white"
        font = ("Verdana", 12)

        self.customer_name_label = Label(self, text="Enter Customer Name:", bg=label_bg_color, fg=label_fg_color, font=font)
        self.customer_name_label.grid(column=2, row=2, padx=(30,0), pady=(30,0))
        self.customer_name_entry = Entry(self, width=30, textvariable=self.c_name, font=font)
        self.customer_name_entry.grid(column=3, row=2, padx=(30,0), pady=(30,0))

        self.customer_email_label = Label(self, text="Enter Customer Email:", bg=label_bg_color, fg=label_fg_color, font=font)
        self.customer_email_label.grid(column=2, row=3, padx=(30,0), pady=(30,0))
        self.customer_email_entry = Entry(self, width=30, textvariable=self.c_email, font=font)
        self.customer_email_entry.grid(column=3, row=3, padx=(30,0), pady=(30,0))

        self.saleperson_id_label = Label(self, text="Enter your employee id:", bg=label_bg_color, fg=label_fg_color, font=font)
        self.saleperson_id_label.grid(column=2, row=4, padx=(30,0), pady=(30,0))
        self.saleperson_id_entry = Entry(self, width=30, textvariable=self.e_id, font=font)
        self.saleperson_id_entry.grid(column=3, row=4, padx=(30,0), pady=(30,0))

        self.vehicle_id_label = Label(self, text="Enter the Vehicle VIN", bg=label_bg_color, fg=label_fg_color, font=font)
        self.vehicle_id_label.grid(column=2, row=5, padx=(30,0), pady=(30,0))
        self.vehicle_id_entry = Entry(self, width=30, textvariable=self.vin, font=font)
        self.vehicle_id_entry.grid(column=3, row=5, padx=(30,0), pady=(30,0))

        self.submit_button = Button(self, text="Submit", command=self.make_sale)
        self.submit_button.grid(column=2, row=6, padx=(30,0), pady=(30,0))

        self.arrival_label = Label(self, text="Move BackOrder to Instock?", bg=label_bg_color, fg=label_fg_color, font=font)
        self.arrival_label.grid(column=5, row=2, padx=(30,0), pady=(30,0))

        self.arrival_vin_label = Label(self, text="Enter VIN: ", bg=label_bg_color, fg=label_fg_color, font=font)
        self.arrival_vin_label.grid(column=5, row=3, padx=(30,0), pady=(30,0))
        self.arrival_vin_entry = Entry(self, width=30, textvariable=self.vin_instock, font=font)
        self.arrival_vin_entry.grid(column=6, row=3, padx=(30,0), pady=(30,0))
        self.arrival_lot_label = Label(self, text="Lot: ", bg=label_bg_color, fg=label_fg_color, font=font)
        self.arrival_lot_label.grid(column=5, row=4, padx=(30,0), pady=(30,0))
        self.arrival_lot_entry = Entry(self, width=30, textvariable=self.lot, font=font)
        self.arrival_lot_entry.grid(column=6, row=4, padx=(30,0), pady=(30,0))
        self.arrival_spot_label = Label(self, text="Spot: ", bg=label_bg_color, fg=label_fg_color, font=font)
        self.arrival_spot_label.grid(column=5, row=5, padx=(30,0), pady=(30,0))
        self.arrival_spot_entry = Entry(self, width=30, textvariable=self.spot, font=font)
        self.arrival_spot_entry.grid(column=6, row=5, padx=(30,0), pady=(30,0))
        self.arrival_stock_entry = Button(self, text="Move Stock", command=self.move_instock)
        self.arrival_stock_entry.grid(column=5, row=6, padx=(30,0), pady=(30,0))

    def make_sale(self):
        cur = self.connection.cursor()
        up_vehicle = """UPDATE Vehicle SET Customer_name = %s, Customer_email = %s WHERE VIN = %s;"""
        cur.execute(up_vehicle, (self.c_name.get(), self.c_email.get(), self.vin.get(),))
        up_customer = """UPDATE Customer Set Seller = %s, Vehicle = %s WHERE Name = %s AND Email = %s;"""
        cur.execute(up_customer, (self.e_id.get(), self.vin.get(), self.c_name.get(), self.c_email.get()))
        #remove from instock
        value = delete_Instock(self.connection, self.vin.get())
        if value is False:
            self.fail_label = Label(self, text="Failed to remove from Instock list")
            self.fail_label.grid(column=2, row=7, padx=(30,0), pady=(30,0))
            return
        self.success_label = Label(self, text="Sold")
        self.success_label.grid(column=2, row=7, padx=(30,0), pady=(30,0))
        self.connection.commit()
        return
    def move_instock(self):
        value = add_Instock(self.connection, self.vin_instock.get(), self.lot.get(), self.spot.get())
        if value is False:
            self.fail_label = Label(self, text="Failed to add to Instock list")
            self.fail_label.grid(column=2, row=7, padx=(30,0), pady=(30,0))
            return
        value = delete_backorder(self.connection, self.vin_instock.get())
        if value is False:
            self.fail_label = Label(self, text="Failed to Delete from BackOrder list")
            self.fail_label.grid(column=2, row=7, padx=(30,0), pady=(30,0))
            return
        self.success_label = Label(self, text="Confirmed")
        self.success_label.grid(column=2, row=7, padx=(30,0), pady=(30,0))
        self.connection = connect()
