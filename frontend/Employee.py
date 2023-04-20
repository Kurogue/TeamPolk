#This File will deal with creating and deleting employees
from backend.db import connect
from backend.queries.add_queries import *
from backend.queries.delete_queries import *
from backend.queries.find_queries import *
from tkinter import *
import datetime
import tkinter as tk 
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel

class Add_delete_Employee(Toplevel):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.title("Employee Management")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
# Set the geometry of the window to the full size of the screen
        self.geometry(f"{screen_width}x{screen_height}")
        self.configure(bg="#36454F")  # Set background color to charcoal gray
        self.connection = connect()
        #variables we need to add to the database
        self.employee_title = StringVar() # will store string for wohat role the employee will have, must be either manager, maintenance or sales
        self.employee_id = IntVar()
        self.employee_ssn = IntVar()
        self.employee_fname = StringVar()
        self.employee_lname = StringVar()
        self.employee_date = datetime.date.today()
        self.employee_addr = StringVar()
        self.employee_title_del = StringVar()
        self.employee_id_del = IntVar()
        self.employee_ssn_del = IntVar()

        label_font = ("Verdana", 12)
        label_fg = "white"
        label_bg = "#36454F"
        padx_value = 20

        ### ADD EMPLOYEE ###
        self.title_employee = Label(self, text="CREATE/LOCATE EMPLOYEE", bg=label_bg, fg=label_fg, font=("Verdana", 20))
        self.title_employee.grid(column=0, row=0)

        # enter the required fields
        # get the role of the employee
        self.employee_role = Label(self, text="ENTER EMPLOYEE ROLE:", bg=label_bg, fg=label_fg, font=label_font)
        self.employee_role.grid(column=0, row=1, pady=(20,0), padx=(20,0), sticky="W")
        self.employee_role_entry = Entry(self, width=10, textvariable=self.employee_title)
        self.employee_role_entry.grid(column=1, row=1, padx=(20,0), pady=(20,0))

        # enter the employee ID
        self.employ_id_label = Label(self, text="ENTER EMPLOYEE ID:", bg=label_bg, fg=label_fg, font=label_font)
        self.employ_id_label.grid(column=0, row=2, padx=(20,0), pady=(20,0), sticky="W")
        self.employ_id_entry = Entry(self, width=10, textvariable=self.employee_id)
        self.employ_id_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        # enter the employee SSN
        self.employ_ssn_label = Label(self, text="ENTER EMPLOYEE SSN:", bg=label_bg, fg=label_fg, font=label_font)
        self.employ_ssn_label.grid(column=0, row=3, padx=(20,0), pady=(20,0), sticky="W")
        self.employ_ssn_entry = Entry(self, width=10, textvariable=self.employee_ssn)
        self.employ_ssn_entry.grid(column=1, row=3, pady=(20,0), padx=(20,0))

        # enter the employee first name
        self.employ_fname_label = Label(self, text="ENTER EMPLOYEE First Name:", bg=label_bg, fg=label_fg, font=label_font)
        self.employ_fname_label.grid(column=0, row=4, padx=(20,0), pady=(20,0), sticky="W")
        self.employ_fname_entry = Entry(self, width=10, textvariable=self.employee_fname)
        self.employ_fname_entry.grid(column=1, row=4, pady=(20,0), padx=(20,0))

        # enter the employee last name
        self.employ_lname_label = Label(self, text="ENTER EMPLOYEE Last Name:", bg=label_bg, fg=label_fg, font=label_font)
        self.employ_lname_label.grid(column=0, row=5, padx=(20,0), pady=(20,0), sticky="W")
        self.employ_lname_entry = Entry(self, width=10, textvariable=self.employee_lname)
        self.employ_lname_entry.grid(column=1, row=5, pady=(20,0), padx=(20,0))

        # enter the employee address
        self.employ_addr_label = Label(self, text="ENTER EMPLOYEE Address:", bg=label_bg, fg=label_fg, font=label_font)
        self.employ_addr_label.grid(column=0, row=6, padx=(20,0), pady=(20,0), sticky="W")
        self.employ_addr_entry = Entry(self, width=10, textvariable=self.employee_addr)
        self.employ_addr_entry.grid(column=1, row=6, pady=(20,0), padx=(20,0))
        # Create Button to CREATE Employee
        self.add_employee_button = Button(self, text="Create", command=self.create_Employee)
        self.add_employee_button.grid(column=2, row=6, pady=(20,0), padx=(20,0))
                # Create Button to CREATE Employee
        self.add_employee_button = Button(self, text="Locate", command=self.locate_employee)
        self.add_employee_button.grid(column=7, row=6, pady=(20,0), padx=(20,0))
        ### DELETE EMPLOYEE section ###
        self.title_employee = Label(self, text="DELETE EMPLOYEE", bg=label_bg, fg=label_fg, font=("Verdana", 20))
        self.title_employee.grid(column=0, row=7, padx=(20, 0), pady=(40, 0))  

        # Enter the role of the deleted employee
        self.employee_role_del = Label(self, text="ENTER EMPLOYEE ROLE", bg=label_bg, fg=label_fg, font=label_font)
        self.employee_role_del.grid(column=0, row=8, pady=(20,0), padx=(20,0), sticky="W")
        self.employee_role_entry_del = Entry(self, width=10, textvariable=self.employee_title_del)
        self.employee_role_entry_del.grid(column=1, row=8, padx=(20,0), pady=(20,0))

        # enter the employee ID
        self.employ_id_label_del = Label(self, text="ENTER EMPLOYEE ID", bg=label_bg, fg=label_fg, font=label_font)
        self.employ_id_label_del.grid(column=0, row=9, padx=(20,0), pady=(20,0), sticky="W")
        self.employ_id_entry_del = Entry(self, width=10, textvariable=self.employee_id_del)
        self.employ_id_entry_del.grid(column=1, row=9, pady=(20,0), padx=(20,0))

        # enter the employee SSN
        self.employ_ssn_label_del = Label(self, text="ENTER EMPLOYEE SSN:", bg=label_bg, fg=label_fg, font=label_font)
        self.employ_ssn_label_del.grid(column=0, row=10, padx=(20,0), pady=(20,0), sticky="W")
        self.employ_ssn_entry_del = Entry(self, width=10, textvariable=self.employee_ssn_del)
        self.employ_ssn_entry_del.grid(column=1, row=10, pady=(20,0), padx=(20,0))

        # Create Button to delete data
        self.delete_employee_button = Button(self, text="Delete", command=self.delete_Employee)
        self.delete_employee_button.grid(column=2, row=10, pady=(20,0), padx=(20,0))
    def create_Employee(self):
        role = self.employee_title.get()
        if role == 'Manager':
            add_manager_employee(self.connection, self.employee_id.get(), self.employee_ssn.get(), self.employee_fname.get(), self.employee_lname.get(), self.employee_date, self.employee_addr.get())
            self.connection = connect()
        elif role == 'Sales':
            add_sales_employee(self.connection,self.employee_id.get(), self.employee_ssn.get(), self.employee_fname.get(), self.employee_lname.get(), self.employee_date, self.employee_addr.get() )
            self.connection = connect()
        elif role == 'Maintenance':
            add_maintenance_employee(self.connection, self.employee_id.get(), self.employee_ssn.get(), self.employee_fname.get(), self.employee_lname.get(), self.employee_date, self.employee_addr.get())
            self.connection = connect()
        else:
            #Need to print error message to the window
            print("ERROR") # placeholder
    def delete_Employee(self):
        role = self.employee_title.get()
        if role == 'Manager':
            value = delete_manager_employee(self.connection, self.employee_id_del.get(), self.employee_ssn_del.get())
            self.connection = connect()
        elif role == 'Sales':
            value = delete_sales_employee(self.connection, self.employee_id_del.get(), self.employee_ssn_del.get())
            self.connection = connect()
        elif role == 'Maintenance':
            value = delete_maintenance_employee(self.connection,  self.employee_id_del.get(), self.employee_ssn_del.get())
            self.connection = connect()
        else:
            #Need to print error message to the window
            print("ERROR") #placeholder

    def locate_employee(self):  
        label_font = ("Verdana", 12)
        label_fg = "white"
        label_bg = "#36454F"
        value = find_employee(self.connection, self.employee_id.get(), self.employee_fname.get(), self.employee_lname.get(), self.employee_ssn.get())
        if value is None:
            self.employ_Failed = Label(self, text="Failed To Find Employee", bg=label_bg, fg=label_fg, font=label_font)
            self.employ_Failed.grid(column=2, row=3, padx=(20,0), pady=(20,0), sticky="W")
        else:
            self.employ_Success = Label(self, text="Employee found", bg=label_bg, fg=label_fg, font=label_font)
            self.employ_Success.grid(column=0, row=10, padx=(20,0), pady=(20,0), sticky="W")
            employee_list = tk.Listbox(self, width=60, height=20)
            employee_list.grid(column=3, row=1, padx=(20, 0), pady=(20, 0), columnspan=3)
            for self.employ in value:
                employee_list.insert(END, self.employ)
