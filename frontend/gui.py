'''
This is the main file for the frontend of the application. It is used to create the GUI and connect to the backend.
'''

#add all the necessary backend functions here
from backend.db import connect
from backend.queries.exteriorQueries import add_exterior, lookup_exterior, delete_exterior
from frontend.Vehicle_search import *
import tkinter as tk

#call postgresql connection function from backend
connection = connect()

root = tk.Tk()
root.title("Vehicle Tracking Service")
root.geometry("800x600")

'''
No longer needed since the backend searches the databse for the vehicle
'''
# def update(data):
#     my_list.delete(0, tk.END)
#     for item in data:
#         my_list.insert(tk.END, item)

# def search_button_clicked():
#     typed = search.get()
#     if typed == '':
#         data = lst
#     else:
#         data = []
#         for item in lst:
#             if typed.lower() in [str(elem).lower() for elem in item]:
#                 data.append(item)
#     print("Search results:", data)
#     update(data)

def v_search():
    
    Vehicle_search(root)
   
#move to locate a Vehicle

locate_vehicle_label = tk.Label(root, width=50, text="Do you wish to find a Vehicle?")
locate_vehicle_label.grid(column=0, row=0, padx=(140, 0), pady=(100, 20))
locate_vehicle_button = tk.Button(text="Yes", command=v_search)
locate_vehicle_button.grid(column=1, row=0, pady=(100, 20))


#Buttons and stuff for search functionality

#Add commands for add and remove buttons
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