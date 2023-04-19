import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from backend.db import connect
from backend.queries.exteriorQueries import add_exterior, lookup_exterior, delete_exterior
from frontend.Vehicle_search import *
from frontend.Add_Delete_vehicle import *
from frontend.Advanced_search import *
from backend.queries.find_queries import *
import datetime
from PIL import ImageTk, Image

connection = connect()

root = tk.Tk()
root.title("Vehicle Tracking Service")
root.geometry("1024x768")
root.configure(bg="#36454F")

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

locate_vehicle_label = tk.Label(root, width=50, text="Do you wish to find a Vehicle?", font=("Verdana", 12), fg="white", bg="#36454F")
locate_vehicle_label.grid(column=0, row=0, padx=(400, 0), pady=(160, 20))
locate_vehicle_button = tk.Button(text="Yes", command=v_search, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")
locate_vehicle_button.grid(column=1, row=0, pady=(160, 20))

advLocate_vehicle_label = tk.Label(root, width=50, text="Here is an advanced vehicle search.", font=("Verdana", 12), fg="white", bg="#36454F")
advLocate_vehicle_label.grid(column=0, row=1, padx=(400, 0), pady=(0, 20))
advLocate_vehicle_button = tk.Button(text="Yes", command=a_search, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")
advLocate_vehicle_button.grid(column=1, row=1, pady=(0, 20))

addBar = tk.Label(root, text="Add/Delete Vehicle", font=("Verdana", 12), fg="white", bg="#36454F")
addButton = tk.Button(text="Yes", command=add_delete, width=7, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")

def on_entry_click(event):
    if removeBar.get() == "Enter vehicle ID to remove":
        removeBar.delete(0, "end")
        removeBar.configure(foreground="black")

def on_focus_out(event):
    if removeBar.get() == "":
        removeBar.insert(0, "Enter vehicle ID to remove")
        removeBar.configure(foreground="gray")

removeBar = tk.Entry(root, bg="white", font=("Verdana", 12), foreground="gray", width=20)
removeBar.insert(0, "Enter vehicle ID to remove")
removeBar.bind('<FocusIn>', on_entry_click)
removeBar.bind('<FocusOut>', on_focus_out)
removeButton = tk.Button(text="Remove", width=10, font=("Verdana", 10, "bold"), bg="white", fg="#36454F")

addBar.grid(column=0, row=5, padx=(400, 0), pady=(0, 20))
addButton.grid(column=1, row=5, padx=10, pady=(0, 20))

removeBar.grid(column=0, row=6, padx=(400, 0), pady=(0, 20))
removeButton.grid(column=1, row=6, padx=10, pady=(0, 20))
instock = find_Instock(connection)
instock_list = tk.Listbox(root, width=80, height=20)
instock_list.grid(column=0, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)
for item in instock:
    instock_list.insert(tk.END, item)

backorder = find_BackOrder(connection)
backorder_list = tk.Listbox(root, width=80, height=20)
backorder_list.grid(column=3, row=7, padx=(30, 0), pady=(10, 0), columnspan=2)
for item in backorder:
    backorder_list.insert(tk.END, item)

def run_app():
    root.mainloop()
