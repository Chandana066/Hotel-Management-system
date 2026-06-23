from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x500+230+220")

        # ================================ Variables ===============================
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_pincode = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()

        # ============================== Title ======================================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"),
                          bg="skyblue", fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ============================== Logo =======================================
        img2 = Image.open(r"C:\Users\chandana chandu\Downloads\logo3.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg_logo = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg_logo.place(x=5, y=2, width=100, height=40)

        # ========================== Label Frame =====================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                     font=("arial", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ======================== Labels and Entries ================================
        # Customer Ref
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        enty_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("arial", 13, "bold"), state="readonly")
        enty_ref.grid(row=0, column=1)

        # Customer Name
        cname = Label(labelframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, width=29, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # Father Name
        lblfname = Label(labelframeleft, text="Father Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblfname.grid(row=2, column=0, sticky=W)
        txtfname = ttk.Entry(labelframeleft, textvariable=self.var_father_name, width=29, font=("arial", 13, "bold"))
        txtfname.grid(row=2, column=1)

        # Gender
        lbl_gender = Label(labelframeleft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Pincode
        lblPincode = Label(labelframeleft, text="Pincode:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPincode.grid(row=4, column=0, sticky=W)
        txtPincode = ttk.Entry(labelframeleft, textvariable=self.var_pincode, width=29, font=("arial", 13, "bold"))
        txtPincode.grid(row=4, column=1)

        # Mobile Number
        lblmobile = Label(labelframeleft, text="Mobile:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmobile.grid(row=5, column=0, sticky=W)
        txtmobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"))
        txtmobile.grid(row=5, column=1)

        # Email
        lblEmail = Label(labelframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        txtEmail.grid(row=6, column=1)

        # Nationality
        lblNationality = Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        combo_Nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_Nationality["values"] = ("Indian", "American", "British", "Other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        # ID Proof Type
        lblIdproof = Label(labelframeleft, text="Id Proof Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdproof.grid(row=8, column=0, sticky=W)
        combo_IdProof = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_IdProof["values"] = ("Aadhar Card", "Driving License", "Passport", "Other")
        combo_IdProof.current(0)
        combo_IdProof.grid(row=8, column=1)

        # ID Number
        lblIdNumber = Label(labelframeleft, text="Id Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number, width=29, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(labelframeleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font=("arial", 13, "bold"))
        txtAddress.grid(row=10, column=1)

        # ============================= Buttons ======================================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnadd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="sky blue", width=10)
        btnadd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 11, "bold"), bg="black", fg="sky blue", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="sky blue", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("arial", 11, "bold"), bg="black", fg="sky blue", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # ======================== Table Frame search system =======================================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("arial", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="green", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()
        combo_Search = ttk.Combobox(Table_Frame,textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Search["values"] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        txtSearch = ttk.Entry(Table_Frame,textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search",command=self.search, font=("arial", 11, "bold"), bg="black", fg="sky blue", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowall = Button(Table_Frame, text="Show All",command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="sky blue", width=10)
        btnShowall.grid(row=0, column=4, padx=1)

        #=========================show data table========================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, columns=("Ref", "Name", "Father_name", "Gender", "Pincode", "Mobile",
                                                                        "Email", "Nationality", "Id_proof", "Id_number", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref", text="Refer No")
        self.Cust_Details_Table.heading("Name", text="Name")
        self.Cust_Details_Table.heading("Father_name", text="Father Name")
        self.Cust_Details_Table.heading("Gender", text="Gender")
        self.Cust_Details_Table.heading("Pincode", text="Pincode")
        self.Cust_Details_Table.heading("Mobile", text="Mobile")
        self.Cust_Details_Table.heading("Email", text="Email")
        self.Cust_Details_Table.heading("Nationality", text="Nationality")
        self.Cust_Details_Table.heading("Id_proof", text="Id Proof")
        self.Cust_Details_Table.heading("Id_number", text="Id Number")
        self.Cust_Details_Table.heading("Address", text="Address")
        self.Cust_Details_Table["show"] = "headings"

        
        self.Cust_Details_Table.column("Ref",width=100)
        self.Cust_Details_Table.column("Name",width=100)
        self.Cust_Details_Table.column("Father_name",width=100)
        self.Cust_Details_Table.column("Gender",width=100)
        self.Cust_Details_Table.column("Pincode",width=100)
        self.Cust_Details_Table.column("Mobile",width=100)
        self.Cust_Details_Table.column("Email",width=100)
        self.Cust_Details_Table.column("Nationality",width=100)
        self.Cust_Details_Table.column("Id_proof",width=100)
        self.Cust_Details_Table.column("Id_number",width=100)
        self.Cust_Details_Table.column("Address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_father_name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_pincode.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_father_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_pincode.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("""Update customer set Name=%s, Father_name=%s, Gender=%s, Pincode=%s, Mobile=%s, Email=%s,
                Nationality=%s, Id_proof=%s, Id_number=%s, Address=%s WHERE Ref=%s
            """, (
                self.var_cust_name.get(),
                self.var_father_name.get(),
                self.var_gender.get(),
                self.var_pincode.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Customer details updated successfully.", parent=self.root)
        
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System", "Do you want to delete this Customer info", parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="management")
            my_cursor = conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_father_name.set(""),
        #self.var_gender.set(""),
        self.var_pincode.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
      
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()        

            
        

# ===================== Run App ===========================
if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
