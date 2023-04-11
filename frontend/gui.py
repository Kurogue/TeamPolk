'''
This is the main file for the frontend of the application. It is used to create the GUI and connect to the backend.
'''

#add all the necessary backend functions here
from backend.db import connect
from backend.queries.exteriorQueries import add_exterior, lookup_exterior, delete_exterior

import tkinter as tk

#call postgresql connection function from backend
connect()

root = tk.Tk()
root.geometry("800x600")

def update(data):
    my_list.delete(0, tk.END)
    for item in data:
        my_list.insert(tk.END, item)

def search_button_clicked():
    typed = search.get()
    if typed == '':
        data = lst
    else:
        data = []
        for item in lst:
            if typed.lower() in [str(elem).lower() for elem in item]:
                data.append(item)
    print("Search results:", data)
    update(data)

#Buttons and stuff for search functionality
addBar = tk.Entry(root)
addButton = tk.Button(text="Add")

removeBar = tk.Entry(root)
removeButton = tk.Button(text="Remove")

search = tk.Entry(root)
searchButton = tk.Button(text="Search", command=search_button_clicked)

search.grid(column=0, row=0, padx=10, pady=5)
searchButton.grid(column=1, row=0, padx=10, pady=5)

addBar.grid(column=0, row=1, padx=10, pady=5)
addButton.grid(column=1, row=1, padx=10, pady=5)

removeBar.grid(column=0, row=2, padx=10, pady=5)
removeButton.grid(column=1, row=2, padx=10, pady=5)

my_list = tk.Listbox(root, width=50)
my_list.grid(column=0, row=3, padx=10, pady=5)   # Change from pack() to grid()

lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
update(lst)

search.bind("<KeyRelease>", search_button_clicked)

def run_app():
    root.mainloop()