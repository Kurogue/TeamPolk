import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from backend.db import connect
from backend.queries.exteriorQueries import add_exterior, lookup_exterior, delete_exterior
from frontend.Vehicle_search import *
from frontend.Vehicle import *
from frontend.Advanced_search import *
from backend.queries.find_queries import *
from frontend.Accessories import *
from frontend.Customer import *
from frontend.Employee import *
from frontend.Maintenance import *
from frontend.Sales import *
import datetime
from PIL import ImageTk, Image

connection = connect()

root = tk.Tk()
root.title("Vehicle Tracking Service")
# Get the width and height of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Set the geometry of the window to the full size of the screen
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="#36454F")

label_padding = int(screen_width * 0.05)

title_label = ttk.Label(root, text="ProTrack Automotive Systems", font=("Verdana", 28, "bold"), background="#36454F", foreground="white")
title_label.place(x=20, y=20)

# Create a photoimage object of the image in the path
image1 = Image.open("frontend/carLogo.png")
image1 = image1.resize((400, 400), Image.ANTIALIAS)  # Resize the image
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test, bg=root.cget('bg'))
label1.image = test

# Position image
label1.place(x=850, y=10)

style = ttk.Style()
style.configure("TButton", foreground="#2A2A2D", background="#36454F", padding=20, font=("Verdana", 12, "bold"))
style.map("TButton", background=[("active", "#36454F")])

def v_search():
    Vehicle_search(root)

def a_search():
    Advanced_search(root)

def add_delete():
    Vehicle_add_delete(root)

def add_accessory():
    Add_Delete_Accessory(root)

def add_customer():
    Add_delete_Customer(root)

def add_employee():
    Add_delete_Employee(root)

def add_maintenances():
    Add_delete_Maintenance(root)

def add_sales():
    Add_delete_Sales(root)

locate_vehicle_label = tk.Label(root, text="Do you wish to find a vehicle?", font=("Verdana", 12), fg="white", bg="#36454F")
locate_vehicle_label.grid(column=0, row=0, padx=(label_padding, 0), pady=(160, 20))
locate_vehicle_button = tk.Button(text="Yes", command=v_search, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")
locate_vehicle_button.grid(column=1, row=0, pady=(160, 20))

advLocate_vehicle_label = tk.Label(root, text="Want an advanced vehicle search?", font=("Verdana", 12), fg="white", bg="#36454F")
advLocate_vehicle_label.grid(column=0, row=1, padx=(label_padding, 0), pady=(0, 20))
advLocate_vehicle_button = tk.Button(text="Yes", command=a_search, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")
advLocate_vehicle_button.grid(column=1, row=1, pady=(0, 20))

addBar = tk.Label(root, text="Add/Delete Vehicle", font=("Verdana", 12), fg="white", bg="#36454F")
addBar.grid(column=0, row=2, padx=(label_padding, 0), pady=(0, 20))
addButton = tk.Button(text="Yes", command=add_delete, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")
addButton.grid(column=1, row=2, pady=(0, 20))

AccessoriesBar = tk.Label(root, text="Add/Delete Accessories", font=("Verdana", 12), fg="white", bg="#36454F")
AccessoriesBar.grid(column=0, row=3, padx=(label_padding, 0), pady=(0, 20))
AccessoriesButton = tk.Button(text="Yes", command=add_accessory, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")
AccessoriesButton.grid(column=1, row=3, pady=(0, 20))

CustomerBar = tk.Label(root, text="Add/Delete Customer", font=("Verdana", 12), fg="white", bg="#36454F")
CustomerBar.grid(column=0, row=4, padx=(label_padding, 0), pady=(0, 20))
CustomerButton = tk.Button(text="Yes", command=add_customer, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")
CustomerButton.grid(column=1, row=4, pady=(0, 20))

spacer = tk.Label(root, width=20, bg="#36454F")
spacer.grid(column=2, row=0)

EmployeeBar = tk.Label(root, text="Add/Delete Employee", font=("Verdana", 12), fg="white", bg="#36454F")
EmployeeBar.grid(column=3, row=0, padx=(label_padding / 2, 0), pady=(160, 20))
EmployeeButton = tk.Button(text="Yes", command=add_employee, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")
EmployeeButton.grid(column=4, row=0, pady=(160, 20))

MaintenanceBar = tk.Label(root, text="Add/Delete Maintenance", font=("Verdana", 12), fg="white", bg="#36454F")
MaintenanceBar.grid(column=3, row=1, padx=(label_padding / 2, 0), pady=(0, 20))
MaintenanceButton = tk.Button(text="Yes", command=add_maintenances, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")
MaintenanceButton.grid(column=4, row=1, pady=(0, 20))

SalesBar = tk.Label(root, text="Add/Delete Sales", font=("Verdana", 12), fg="white", bg="#36454F")
SalesBar.grid(column=3, row=2, padx=(label_padding / 2, 0), pady=(0, 20))
SalesButton = tk.Button(text="Yes", command=add_sales, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")
SalesButton.grid(column=4, row=2, pady=(0, 20))

list_padding = (screen_width - 880) // 2

instock = find_Instock(connection)
instock_list = tk.Listbox(root, width=60, height=20)
instock_list.grid(column=0, row=6, padx=(list_padding, 0), pady=(10, 0), columnspan=3)


for item in instock:
    instock_list.insert(tk.END, item)

backorder = find_BackOrder(connection)
backorder_list = tk.Listbox(root, width=60, height=20)
backorder_list.grid(column=3, row=6, padx=(list_padding, 10), pady=(10, 0), columnspan=3)

for item in backorder:
    backorder_list.insert(tk.END, item)
def run_app():
    root.mainloop()
