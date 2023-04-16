'''
This is the main file for the frontend of the application. It is used to create the GUI and connect to the backend.
'''

#add all the necessary backend functions here
from backend.db import connect
from backend.queries.exteriorQueries import add_exterior, lookup_exterior, delete_exterior
from frontend.Vehicle_search import *
import tkinter as tk
from frontend.Advanced_search import *

#call postgresql connection function from backend
connection = connect()

root = tk.Tk()
root.title("Vehicle Tracking Service")
root.geometry("800x600")

def v_search():
    Vehicle_search(root)

def a_search():
    Advanced_search(root)


#move to locate a Vehicle

locate_vehicle_label = tk.Label(root, width=50, text="Do you wish to find a Vehicle?")
locate_vehicle_label.grid(column=0, row=0, padx=(140, 0), pady=(100, 20))
locate_vehicle_button = tk.Button(text="Yes", command=v_search)
locate_vehicle_button.grid(column=1, row=0, pady=(100, 20))

advLocate_vehicle_label = tk.Label(root, width=50, text="Here is an advanced vehicle search.")
advLocate_vehicle_label.grid(column=0, row=1, padx=(140, 0), pady=(0, 20))
advLocate_vehicle_button = tk.Button(text="Yes", command=a_search)
advLocate_vehicle_button.grid(column=1, row=1, pady=(0, 20))

#Buttons and stuff for search functionality

#Add commands/functions for add and remove buttons
addBar = tk.Entry(root)
addButton = tk.Button(text="Add")

removeBar = tk.Entry(root)
removeButton = tk.Button(text="Remove")

# search = tk.Entry(root)
# searchButton = tk.Button(text="Search", command=search_button_clicked)

addBar.grid(column=0, row=5, padx=(140, 0), pady=(0, 20))
addButton.grid(column=1, row=5, padx=10, pady=(0, 20))

# search.grid(column=0, row=5, padx=10, pady=5)
# searchButton.grid(column=1, row=5, padx=10, pady=5)

removeBar.grid(column=0, row=6, padx=(140, 0), pady=(0, 20))
removeButton.grid(column=1, row=6, padx=10, pady=(0,20))

my_list = tk.Listbox(root, width=50)
my_list.grid(column=0, row=7, padx=(230, 0), pady=(10, 0), columnspan=2)   # Change from pack() to grid()
""""
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
update(lst)

search.bind("<KeyRelease>", search_button_clicked)
"""
def run_app():
    root.mainloop()
