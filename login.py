from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pillow_avif
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem
import random
from time import strftime
from datetime import datetime
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        image = Image.open(r"C:\Users\chandana chandu\Downloads\login.avif")
        image = image.resize((1550, 800), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(image)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\chandana chandu\Downloads\login logo.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimg1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        img2 = Image.open(r"C:\Users\chandana chandu\Downloads\login logo.jpg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimg2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\chandana chandu\Downloads\pass logo.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimg3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=394, width=25, height=25)

        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="blue", activeforeground="white", activebackground="blue")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text="New User Register", command=self.register_window,
                             font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black",
                             activeforeground="white", activebackground="blue")
        registerbtn.place(x=15, y=350, width=160)

        forgetpasswordbtn = Button(frame, text="Forgot Password", command=self.forgot_password_window,
                                   font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black",
                                   activeforeground="white", activebackground="blue")
        forgetpasswordbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txtuser.get() == "chan" and self.txtpass.get() == "123":
            messagebox.showinfo("Success", "Welcome to Hotel management System", parent=self.root)
            self.new_window = Toplevel(self.root)
            self.app = HotelManagementSystem(self.new_window)
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password", parent=self.root)
            else:
                open_main = messagebox.askyesno("YesNo", "Access granted to only admin", parent=self.root)
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
           


    # ============================= reset password ===================================
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select Security Question", parent=self.root2)
        elif self.txt_security_A.get() == "":
            messagebox.showerror("Error", "Please enter the Answer", parent=self.root2)
        elif self.txt_new_password.get() == "":
            messagebox.showerror("Error", "Please enter the new Password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="management")
            my_cursor = conn.cursor()

            query = "SELECT * FROM register WHERE Email=%s AND SecurityQ=%s AND SecurityA=%s"
            value = (
                self.txtuser.get(),                      # email from login field
                self.combo_security_Q.get(),             # selected security question
                self.txt_security_A.get()                # security answer entered
            )
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please enter the correct Answer", parent=self.root2)
            else:
                update_query = "UPDATE register SET Password=%s WHERE Email=%s"
                update_value = (
                    self.txt_new_password.get(),         # new password entered
                    self.txtuser.get()                   # email to update
                )
                my_cursor.execute(update_query, update_value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your Password has been reset, Please login using new Password", parent=self.root2)
                self.root2.destroy()


    #===================================forgot password window========================
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the Email address to reset the password",  parent=self.root)
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="management")
            my_cursor = conn.cursor()
            query = ("select * from register where Email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("My Error", "Please enter the valid user name", parent=self.root)
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                Label(self.root2, text="Forgot Password", font=("times new roman", 15, "bold"),
                      fg="red", bg="white").place(x=50, y=40)

                self.var_securityQ = StringVar()
                self.var_securityA = StringVar()
                self.var_newpass = StringVar()

                security = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),
                                 bg="white", fg="black")
                security.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, textvariable=self.var_securityQ,
                                                     font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Vehicle No")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"),
                                   bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security_A = ttk.Entry(self.root2, textvariable=self.var_securityA,
                                                font=("times new roman", 15))
                self.txt_security_A.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),
                                     bg="white", fg="black")
                new_password.place(x=50, y=220)

                self.txt_new_password = ttk.Entry(self.root2, textvariable=self.var_newpass,
                                                  font=("times new roman", 15))
                self.txt_new_password.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset",command=self.reset_pass,  font=("times new roman", 15, "bold"),
                             bg="green", fg="white")
                btn.place(x=130, y=290)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        image = Image.open(r"C:\Users\chandana chandu\Downloads\register.avif")
        image = image.resize((1550, 900), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(image)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        image = Image.open(r"C:\Users\chandana chandu\Downloads\reg3.png")
        self.bg1 = ImageTk.PhotoImage(image)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE ", font=("times new roman", 20, "bold"),
                             fg="darkblue", bg="white")
        register_lbl.place(x=20, y=20)

        fname = Label(frame, text="First name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        security = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"),
                         bg="white", fg="black")
        security.place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                             font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Vehicle No")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"),
                             bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15),
                                          show="*")
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check,
                               text="I Agree To The Terms And Conditions", font=("times new roman", 11, "bold"),
                               onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        image = Image.open(r"C:\Users\chandana chandu\Downloads\regi22.jpeg")
        image = image.resize((200, 70), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(image)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0,
                    font=("times new roman", 14, "bold"), cursor="hand2", bg="white")
        b1.place(x=10, y=420, width=300)

        image1 = Image.open(r"C:\Users\chandana chandu\Downloads\log1.png")
        image1 = image1.resize((200, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(image1)
        b1 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0,
                    font=("times new roman", 14, "bold"), cursor="hand2")
        b1.place(x=330, y=430, width=200)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms & conditions", parent=self.root)
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="management")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
