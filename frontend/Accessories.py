from backend.db import connect
#from backend.queries.vehicle_queries import *
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from tkinter import *
import tkinter as tk
from tkinter import StringVar, IntVar, Button, Label, Entry, Toplevel

class Add_Delete_Accessory(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Accessories")
        # Get the width and height of the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Set the geometry of the window to the full size of the screen
        self.geometry(f"{screen_width}x{screen_height}")
        self.configure(bg='#36454F')
        self.int_id = IntVar()
        self.int_type = StringVar()
        self.int_desc = StringVar()
        self.int_color = StringVar()
        self.connection = connect()
        self.ext_id = IntVar()
        self.ext_type = StringVar()
        self.ext_desc = StringVar()
        self.ext_color = StringVar()
        self.feat_id = IntVar()
        self.feat_type = StringVar()
        self.feat_desc = StringVar()
        self.con_id = IntVar()
        self.con_type = StringVar()
        self.con_desc = StringVar()
        self.hand_id = IntVar()
        self.hand_type = StringVar()
        self.hand_desc = StringVar()
        self.preform_id = IntVar()
        self.preform_type = StringVar()
        self.preform_desc = StringVar()
        self.pack_id = IntVar()
        self.pack_type = StringVar()
        self.pack_desc = StringVar()
        self.warr_id = IntVar()
        self.warr_type = StringVar()
        self.warr_desc = StringVar()
        self.safe_id = IntVar()
        self.safe_type = StringVar()
        self.safe_desc = StringVar()
        self.audio_id = IntVar()
        self.audio_type = StringVar()
        self.audio_desc = StringVar()
        
        interior_frame = tk.Frame(self, bg='#36454F', bd=5)
        interior_frame.grid(column=0, row=0, padx=(10, 0), pady=(20, 0), sticky="nsew")

        self.interior_id_label = tk.Label(interior_frame, text="Interior ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.interior_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.interior_id_entry = tk.Entry(interior_frame, width=10, textvariable=self.int_id)
        self.interior_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.interior_type_label = tk.Label(interior_frame, text="Interior Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.interior_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.interior_type_entry = tk.Entry(interior_frame, width=10, textvariable=self.int_type)
        self.interior_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.interior_description_label = tk.Label(interior_frame, text="Interior Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.interior_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.interior_description_entry = tk.Entry(interior_frame, width=30, textvariable=self.int_desc)
        self.interior_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.interior_color_label = tk.Label(interior_frame, text="Interior Color: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.interior_color_label.grid(column=0, row=3, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.interior_color_entry = tk.Entry(interior_frame, width=10, textvariable=self.int_color)
        self.interior_color_entry.grid(column=1, row=3, pady=(20,0), padx=(20,0))

        self.interior_add_button = tk.Button(interior_frame, text="Add Interior", command=self.add_Interior)
        self.interior_add_button.grid(column=0, row=4, pady=(20,0), padx=(20,0))

        self.interior_del_button = tk.Button(interior_frame, text="Delete Interior", command=self.delete_Interior)
        self.interior_del_button.grid(column=1, row=4, pady=(20,0), padx=(20,0))

        exterior_frame = tk.Frame(self, bg='#36454F', bd=5)
        exterior_frame.grid(column=0, row=2, padx=(10, 5), pady=(5, 20), sticky="nsew")

        self.exterior_id_label = tk.Label(exterior_frame, text="Exterior ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.exterior_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.exterior_id_entry = tk.Entry(exterior_frame, width=10, textvariable=self.ext_id)
        self.exterior_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.exterior_type_label = tk.Label(exterior_frame, text="Exterior Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.exterior_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.exterior_type_entry = tk.Entry(exterior_frame, width=10, textvariable=self.ext_type)
        self.exterior_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.exterior_description_label = tk.Label(exterior_frame, text="Exterior Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.exterior_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.exterior_description_entry = tk.Entry(exterior_frame, width=30, textvariable=self.ext_desc)
        self.exterior_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.exterior_color_label = tk.Label(exterior_frame, text="Exterior Color: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.exterior_color_label.grid(column=0, row=3, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.exterior_color_entry = tk.Entry(exterior_frame, width=10, textvariable=self.ext_color)
        self.exterior_color_entry.grid(column=1, row=3, pady=(20,0), padx=(20,0))

        self.exterior_add_button = tk.Button(exterior_frame, text="Add Exterior", command=self.add_Exterior)
        self.exterior_add_button.grid(column=0, row=4, pady=(20,0), padx=(20,0))

        self.exterior_del_button = tk.Button(exterior_frame, text="Delete Exterior", command=self.delete_Exterior)
        self.exterior_del_button.grid(column=1, row=4, pady=(20,0), padx=(20,0))

        feature_frame = tk.Frame(self, bg='#36454F', bd=5)
        feature_frame.grid(column=0, row=0, padx=(10, 5), pady=(20, 5), sticky="nsew")

        self.feature_id_label = tk.Label(feature_frame, text="Feature ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.feature_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.feature_id_entry = tk.Entry(feature_frame, width=10, textvariable=self.feat_id)
        self.feature_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.feature_type_label = tk.Label(feature_frame, text="Feature Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.feature_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.feature_type_entry = tk.Entry(feature_frame, width=10, textvariable=self.feat_type)
        self.feature_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.feature_description_label = tk.Label(feature_frame, text="Feature Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.feature_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.feature_description_entry = tk.Entry(feature_frame, width=30, textvariable=self.feat_desc)
        self.feature_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.feature_add_button = tk.Button(feature_frame, text="Add Feature", command=self.add_Feature)
        self.feature_add_button.grid(column=0, row=3, pady=(20,0), padx=(20,0))

        self.feature_del_button = tk.Button(feature_frame, text="Delete Feature", command=self.delete_Feature)
        self.feature_del_button.grid(column=1, row=3, pady=(20,0), padx=(20,0))

        control_frame = tk.Frame(self, bg='#36454F', bd=5)
        control_frame.grid(column=1, row=2, padx=(5, 5), pady=(5, 20), sticky="nsew")

        self.control_id_label = tk.Label(control_frame, text="Control ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.control_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.control_id_entry = tk.Entry(control_frame, width=10, textvariable=self.con_id)
        self.control_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.control_type_label = tk.Label(control_frame, text="Control Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.control_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.control_type_entry = tk.Entry(control_frame, width=10, textvariable=self.con_type)
        self.control_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.control_description_label = tk.Label(control_frame, text="Control Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.control_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.control_description_entry = tk.Entry(control_frame, width=30, textvariable=self.con_desc)
        self.control_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.control_add_button = tk.Button(control_frame, text="Add Control", command=self.add_Control)
        self.control_add_button.grid(column=0, row=3, pady=(20,0), padx=(20,0))

        self.control_del_button = tk.Button(control_frame, text="Delete Control", command=self.delete_Control)
        self.control_del_button.grid(column=1, row=3, pady=(20,0), padx=(20,0))

        handling_frame = tk.Frame(self, bg='#36454F', bd=5)
        handling_frame.grid(column=1, row=0, padx=(5, 5), pady=(20, 5), sticky="nsew")

        self.handling_id_label = tk.Label(handling_frame, text="Feature ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.handling_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.handling_id_entry = tk.Entry(handling_frame, width=10, textvariable=self.hand_id)
        self.handling_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.handling_type_label = tk.Label(handling_frame, text="Handling Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.handling_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.handling_type_entry = tk.Entry(handling_frame, width=10, textvariable=self.hand_type)
        self.handling_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.handling_description_label = tk.Label(handling_frame, text="Handling Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.handling_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.handling_description_entry = tk.Entry(handling_frame, width=30, textvariable=self.hand_desc)
        self.handling_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.handling_add_button = tk.Button(handling_frame, text="Add Handling", command=self.add_Handling)
        self.handling_add_button.grid(column=0, row=3, pady=(20,0), padx=(20,0))

        self.handling_del_button = tk.Button(handling_frame, text="Delete Handling", command=self.delete_Handling)
        self.handling_del_button.grid(column=1, row=3, pady=(20,0), padx=(20,0))


        handling_frame = tk.Frame(self, bg='#36454F', bd=5)
        handling_frame.grid(column=2, row=0, padx=(10, 0), pady=(20, 0), sticky="nsew")

        self.handling_id_label = tk.Label(handling_frame, text="Feature ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.handling_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.handling_id_entry = tk.Entry(handling_frame, width=10, textvariable=self.hand_id)
        self.handling_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.handling_type_label = tk.Label(handling_frame, text="Handling Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.handling_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.handling_type_entry = tk.Entry(handling_frame, width=10, textvariable=self.hand_type)
        self.handling_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.handling_description_label = tk.Label(handling_frame, text="Handling Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.handling_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.handling_description_entry = tk.Entry(handling_frame, width=30, textvariable=self.hand_desc)
        self.handling_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.handling_add_button = tk.Button(handling_frame, text="Add Handling", command=self.add_Handling)
        self.handling_add_button.grid(column=0, row=3, pady=(20,0), padx=(20,0))

        self.handling_del_button = tk.Button(handling_frame, text="Delete Handling", command=self.delete_Handling)
        self.handling_del_button.grid(column=1, row=3, pady=(20,0), padx=(20,0))

        preform_frame = tk.Frame(self, bg='#36454F', bd=5)
        preform_frame.grid(column=1, row=0, padx=(5, 5), pady=(20, 5), sticky="nsew")

        self.preform_id_label = tk.Label(preform_frame, text="Preformance ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.preform_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.preform_id_entry = tk.Entry(preform_frame, width=10, textvariable=self.preform_id)
        self.preform_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.preform_type_label = tk.Label(preform_frame, text="Preformance Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.preform_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.preform_type_entry = tk.Entry(preform_frame, width=10, textvariable=self.preform_type)
        self.preform_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.preform_description_label = tk.Label(preform_frame, text="Preformance Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.preform_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.preform_description_entry = tk.Entry(preform_frame, width=30, textvariable=self.preform_desc)
        self.preform_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.preform_add_button = tk.Button(preform_frame, text="Add Preformance", command=self.add_Preformance)
        self.preform_add_button.grid(column=0, row=3, pady=(20,0), padx=(20,0))

        self.preform_del_button = tk.Button(preform_frame, text="Delete Preformance", command=self.delete_Preformance)
        self.preform_del_button.grid(column=1, row=3, pady=(20,0), padx=(20,0))



        package_frame = tk.Frame(self, bg='#36454F', bd=5)
        package_frame.grid(column=0, row=1, padx=(10, 5), pady=(5, 20), sticky="nsew")

        self.package_id_label = tk.Label(package_frame, text="Package ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.package_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.package_id_entry = tk.Entry(package_frame, width=10, textvariable=self.pack_id)
        self.package_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.package_type_label = tk.Label(package_frame, text="Package Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.package_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.package_type_entry = tk.Entry(package_frame, width=10, textvariable=self.pack_type)
        self.package_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.package_description_label = tk.Label(package_frame, text="Package Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.package_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.package_description_entry = tk.Entry(package_frame, width=30, textvariable=self.pack_desc)
        self.package_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.package_add_button = tk.Button(package_frame, text="Add Package", command=self.add_Package)
        self.package_add_button.grid(column=0, row=3, pady=(20,0), padx=(20,0))

        self.package_del_button = tk.Button(package_frame, text="Delete Package", command=self.delete_Package)
        self.package_del_button.grid(column=1, row=3, pady=(20,0), padx=(20,0))


        safety_frame = tk.Frame(self, bg='#36454F', bd=5)
        safety_frame.grid(column=1, row=1, padx=(5, 5), pady=(5, 20), sticky="nsew")

        self.safety_id_label = tk.Label(safety_frame, text="Safety/Security ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.safety_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.safety_id_entry = tk.Entry(safety_frame, width=10, textvariable=self.safe_id)
        self.safety_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.safety_type_label = tk.Label(safety_frame, text="Safety/Security Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.safety_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.safety_type_entry = tk.Entry(safety_frame, width=10, textvariable=self.safe_type)
        self.safety_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.safety_description_label = tk.Label(safety_frame, text="Safety/Security Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.safety_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.safety_description_entry = tk.Entry(safety_frame, width=30, textvariable=self.safe_desc)
        self.safety_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.safety_add_button = tk.Button(safety_frame, text="Add Safety/Security", command=self.add_Safety)
        self.safety_add_button.grid(column=0, row=3, pady=(20,0), padx=(20,0))

        self.safety_del_button = tk.Button(safety_frame, text="Delete Safety/Security", command=self.delete_Safety)
        self.safety_del_button.grid(column=1, row=3, pady=(20,0), padx=(20,0))


        warranty_frame = tk.Frame(self, bg='#36454F', bd=5)
        warranty_frame.grid(column=2, row=1, padx=(5, 10), pady=(5, 20), sticky="nsew")

        self.warranty_id_label = tk.Label(warranty_frame, text="Warranty ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.warranty_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.warranty_id_entry = tk.Entry(warranty_frame, width=10, textvariable=self.warr_id)
        self.warranty_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.warranty_type_label = tk.Label(warranty_frame, text="Warranty Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.warranty_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.warranty_type_entry = tk.Entry(warranty_frame, width=10, textvariable=self.warr_type)
        self.warranty_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.warranty_description_label = tk.Label(warranty_frame, text="Warranty Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.warranty_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.warranty_description_entry = tk.Entry(warranty_frame, width=30, textvariable=self.warr_desc)
        self.warranty_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.warranty_add_button = tk.Button(warranty_frame, text="Add Warranty", command=self.add_Warranty)
        self.warranty_add_button.grid(column=0, row=3, pady=(20,0), padx=(20,0))

        self.warranty_del_button = tk.Button(warranty_frame, text="Delete Warranty", command=self.delete_Warranty)
        self.warranty_del_button.grid(column=1, row=3, pady=(20,0), padx=(20,0))


        audio_frame = tk.Frame(self, bg='#36454F', bd=5)
        audio_frame.grid(column=2, row=2, padx=(5, 10), pady=(5, 20), sticky="nsew")

        self.audio_id_label = tk.Label(audio_frame, text="Audio ID: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.audio_id_label.grid(column=0, row=0, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.audio_id_entry = tk.Entry(audio_frame, width=10, textvariable=self.audio_id)
        self.audio_id_entry.grid(column=1, row=0, pady=(20,0), padx=(20,0))

        self.audio_type_label = tk.Label(audio_frame, text="Audio Type: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.audio_type_label.grid(column=0, row=1, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.audio_type_entry = tk.Entry(audio_frame, width=10, textvariable=self.audio_type)
        self.audio_type_entry.grid(column=1, row=1, pady=(20,0), padx=(20,0))

        self.audio_description_label = tk.Label(audio_frame, text="Audio Description: ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
        self.audio_description_label.grid(column=0, row=2, pady=(20,0), padx=(10,0), sticky=tk.W)

        self.audio_description_entry = tk.Entry(audio_frame, width=30, textvariable=self.audio_desc)
        self.audio_description_entry.grid(column=1, row=2, pady=(20,0), padx=(20,0))

        self.audio_add_button = tk.Button(audio_frame, text="Add Audio", command=self.add_Audio)
        self.audio_add_button.grid(column=0, row=3, pady=(20,0), padx=(20,0))

        self.audio_del_button = tk.Button(audio_frame, text="Delete Audio", command=self.delete_Audio)
        self.audio_del_button.grid(column=1, row=3, pady=(20,0), padx=(20,0))

    def add_Interior(self):
        value = add_interior(self.connection, self.int_id.get(), self.int_type.get(), self.int_desc.get(), self.int_color.get())
        int_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(int_frame, text="Failed To add Interior", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(int_frame, text="Successfully added to Interior", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def delete_Interior(self):
        value = delete_interior(self.connection, self.int_id.get(), self.int_type.get())
        int_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(int_frame, text="Failed To delete Interior", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(int_frame, text="Successfully deleted Interior", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def add_Exterior(self):
        value = add_exterior(self.connection, self.ext_id.get(), self.ext_type.get(), self.ext_desc.get(), self.ext_color.get())
        ext_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(ext_frame, text="Failed To add Exterior", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(ext_frame, text="Successfully added Exterior", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def delete_Exterior(self):
        value = delete_exterior(self.connection, self.ext_id.get(), self.ext_type.get())
        ext_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(ext_frame, text="Failed To delete Exterior", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(ext_frame, text="Successfully deleted Exterior", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def add_Feature(self):
        value = add_features(self.connection, self.feat_id.get(), self.feat_type.get(), self.feat_desc.get())
        feat_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(feat_frame, text="Failed To add Feature", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(feat_frame, text="Successfully added Feature", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def delete_Feature(self):
        value = delete_features(self.connection, self.feat_id.get(), self.feat_type.get())
        feat_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(feat_frame, text="Failed To delete Feature", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(feat_frame, text="Successfully deleted Feature", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def add_Control(self):
        value = add_control(self.connection, self.con_id.get(), self.con_type.get(), self.con_desc.get())
        control_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(control_frame, text="Failed To add Control", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(control_frame, text="Successfully added Control", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def delete_Control(self):
        value = delete_control(self.connection, self.con_id.get(), self.con_type.get())
        control_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(control_frame, text="Failed To delete Control", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(control_frame, text="Successfully deleted Control", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def add_Handling(self):
        value = add_handling(self.connection, self.hand_id.get(), self.hand_type.get(), self.hand_desc.get())
        hand_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(hand_frame, text="Failed To add Handling", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(hand_frame, text="Successfully added Handling ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def delete_Handling(self):
        value = delete_handling(self.connection, self.hand_id.get(), self.hand_type.get())
        hand_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(hand_frame, text="Failed To delete Handling", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(hand_frame, text="Successfully deleted Handling", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def add_Audio(self):
        value = add_audio(self.connection, self.audio_id.get(), self.audio_type.get(), self.audio_desc.get())
        audio_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(audio_frame, text="Failed To add Audio", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(audio_frame, text="Successfully added Audio ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def delete_Audio(self):
        value = delete_audio(self.connection, self.audio_id.get(), self.audio_type.get())
        audio_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(audio_frame, text="Failed To delete Audio", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(audio_frame, text="Successfully deleted Audio", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def add_Preformance(self):
        value = add_performance(self.connection, self.preform_id.get(), self.preform_type.get(), self.preform_desc.get())
        preform_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(preform_frame, text="Failed To add Performance ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(preform_frame, text="Successfully added Performance", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def delete_Preformance(self):
        value = delete_performance(self.connection, self.preform_id.get(), self.preform_type.get())
        preform_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(preform_frame, text="Failed To delete Preformance", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(preform_frame, text="Successfully Deleted Preformance", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def add_Package(self):
        value = add_package(self.connection, self.pack_id.get(), self.pack_type.get(), self.pack_desc.get())
        pack_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(pack_frame, text="Failed To add Package", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(pack_frame, text="Successfully added Package", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def delete_Package(self):
        value = delete_package(self.connection, self.pack_id.get(), self.pack_type.get())
        pack_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(pack_frame, text="Failed To delete Package", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(pack_frame, text="Successfully added Package ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def add_Safety(self):
        value = add_safe_security(self.connection, self.safe_id.get(), self.safe_type.get(), self.safe_desc.get())
        safe_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(safe_frame, text="Failed To add Safety/Security", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(safe_frame, text="Successfully added Safety/Security", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def delete_Safety(self):
        value = delete_safe_security(self.connection, self.safe_id.get(), self.safe_type.get())
        safe_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(safe_frame, text="Failed To delete Safety/Security", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(safe_frame, text="Successfully deleted Safety/Security", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def add_Warranty(self):
        value = add_warranty(self.connection, self.warr_id.get(), self.warr_type.get(), self.warr_desc.get())
        warr_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(warr_frame, text="Failed To add Warranty", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(warr_frame, text="Successfully added Warranty ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
    def delete_Warranty(self):
        value = delete_warranty(self.connection, self.warr_id.get(), self.warr_type.get())
        warr_frame = tk.Frame(self, bg='#36454F', bd=5)
        if value is False:
            self.fail_label = tk.Label(warr_frame, text="Failed To delete Warranty ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.fail_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
        else:
            self.success_label = tk.Label(warr_frame, text="Successfully deleted Warranty ", bg='#36454F', fg='#FFFFFF', font=("Helvetica", 12))
            self.success_label.grid(column=0, row=4, pady=(20,0), padx=(10,0), sticky=tk.W)
            self.connection = connect()
