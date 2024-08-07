from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3


#============================================================Window for home page=======================================
root = Tk()
root.title("Library Management System")
root.iconbitmap("l.ico")
root.geometry("700x700+100-100")
root.config(bg="#8AAAE5")
root.state("zoomed")


#===========================================================Function to define sign up window===========================
def open_signup_window():
    signup_window = Toplevel(root)
    signup_window.title("Library Management System - Signup")
    signup_window.iconbitmap("l.ico")
    signup_window.geometry("700x700+100-100")
    signup_window.config(bg="#8AAAE5")
    signup_window.state("zoomed")

    # ===================================Sign Up Page UI components
    colour1 = Label(signup_window, text="      Library Management System                                                                                                                                                                                       Signup now", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    colour1.pack()
    colour2 = Label(signup_window, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    Sign_Up_page = Label(signup_window, text="Signup Page", bg="#8AAAE5", font=("Bold Arial", "17"), width=13, height=1)
    Sign_Up_page.place(x=710, y=70)

    Label_Username = Label(signup_window, text="Username", bg="#8AAAE5", font=("Bold Arial", "20"))
    Label_Username.place(x=200, y=170)
    EntryUsername = Entry(signup_window, width=15, font=('Arial 20'))
    EntryUsername.place(x=350, y=170)

    date_of_birth_name = Label(signup_window, text="Date of Birth", bg="#8AAAE5", font=("Bold Arial", "20"))
    date_of_birth_name.place(x=180, y=225)
    Entry_date_of_birth = Entry(signup_window, width=15, font=('Arial 20'))
    Entry_date_of_birth.place(x=350, y=225)

    Contact_name = Label(signup_window, text="Contact", bg="#8AAAE5", font=("Bold Arial", "20"))
    Contact_name.place(x=230, y=280)
    Entry_contact = Entry(signup_window, width=15, font=('Arial 20'))
    Entry_contact.place(x=350, y=280)

    Addres_name = Label(signup_window, text="Address", bg="#8AAAE5", font=("Bold Arial", "20"))
    Addres_name.place(x=230, y=335)
    Addres_Entry = Entry(signup_window, width=15, font=('Arial 20'))
    Addres_Entry.place(x=350, y=335)

    Password_label = Label(signup_window, text="Password", bg="#8AAAE5", font=("Bold Arial", "20"))
    Password_label.place(x=230, y=390)
    Password_entry = Entry(signup_window, show="*", width=15, font=('Arial 20'))
    Password_entry.place(x=350, y=390)

    # ============================User type selection
    Role_label = Label(signup_window, text="Role", bg="#8AAAE5", font=("Bold Arial", "20"))
    Role_label.place(x=230, y=445)
    role_var = StringVar(value="user")
    Role_admin = Radiobutton(signup_window, text="Admin", variable=role_var, value="admin", bg="#8AAAE5", font=("Bold Arial", "20"))
    Role_admin.place(x=350, y=440)
    Role_user = Radiobutton(signup_window, text="User", variable=role_var, value="user", bg="#8AAAE5", font=("Bold Arial", "20"))
    Role_user.place(x=450, y=440)

    # =====================================================================Database connection and creation
    conn = sqlite3.connect('Library_management_system.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            dob TEXT NOT NULL,
            contact TEXT NOT NULL,
            address TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'user'))
        )
    ''')
    conn.commit()
    #=============================Function to handle the data connection with database
    def signup():
        username = EntryUsername.get()
        dob = Entry_date_of_birth.get()
        contact = Entry_contact.get()
        address = Addres_Entry.get()
        password = Password_entry.get()
        role = role_var.get()
        
        if username and dob and contact and address and password:
            try:
                c.execute("SELECT COUNT(*) FROM users WHERE role='admin'")
                if role == "admin" and c.fetchone()[0] > 0:
                    messagebox.showerror("Error", "Admin account already exists")
                    return

                c.execute("INSERT INTO users (username, dob, contact, address, password, role) VALUES (?, ?, ?, ?, ?, ?)", 
                          (username, dob, contact, address, password, role))
                conn.commit()
                messagebox.showinfo("Library Management System", "Sign up successfully")
                
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists")
        else:
            messagebox.showerror("Error", "Please fill out all fields")

    Sign_up_page_button = Button(signup_window, text="Signup", font=('Arial'), command=signup)
    Sign_up_page_button.place(x=350, y=500)
    #==================================Define the exit for sign up page
    def exit_app():
        signup_window.destroy()
        root.deiconify()

    Button_Exit = Button(signup_window, text="   Exit   ", font=('Arial'), command=exit_app)
    Button_Exit.place(x=1100, y=500)
#======================================================Toplevel Window for login page==============================
def open_login_window():
    login_window = Toplevel(root)
    login_window.title("Library Management System - Login")
    login_window.iconbitmap("l.ico")
    login_window.geometry("700x700+100-100")
    login_window.config(bg="#8AAAE5")
    login_window.state("zoomed")

    admin = Label(login_window, text="Library Login", font=("Bold Arial", "30"), bg="#8AAAE5", fg="#000000")
    admin.place(x=900, y=150)

    library_photo = Image.open("zbc.png")
    c = library_photo.resize((850, 690))
    r = ImageTk.PhotoImage(c)
    image1 = Label(login_window, image=r)
    image1.image = r  # ======================================Keep a reference to avoid garbage collection
    image1.place(x=0, y=50)

    colour1 = Label(login_window, text="    Library Management System", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    colour1.pack()

    colour2 = Label(login_window, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    def login():
        username = User_Entry.get()
        password = password_Entry.get()
        
        conn = sqlite3.connect("Library_management_system.db")
        c = conn.cursor()
        c.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        
        if result:
            role = result[0]
            if role == 'admin':
                messagebox.showinfo("Library Management System", "Welcome Admin!")
                login_window.destroy()
                open_admin_dashboard() # Redirect to the admin dashboard
            else:
                messagebox.showinfo("Library Management System", "Welcome User!")
                login_window.destroy()
                open_user_dashboard()  # Redirect to the user dashboard
        else:
            messagebox.showerror("Error", "Invalid credentials")

        conn.close()

    username = Label(login_window, text="Username", font="34", bg="#8AAAE5")
    username.place(x=900, y=270)

    password = Label(login_window, text="Password", font="34", bg="#8AAAE5", fg="black")
    password.place(x=900, y=360)

    log_inButton = Button(login_window, text="Login", font=("4"), fg="black", bg="white", command=login)
    log_inButton.place(x=900, y=550, height=35)

    def onclick(event, text):
        if event.widget.get() == text:
            event.widget.delete(0, END)
            event.widget.insert(0, '')

    def offclick(event, text):
        if event.widget.get() == '':
            event.widget.insert(0, text)

    
    
    def open_reset_password_window():
        reset_window = Toplevel(root)
        reset_window.state("zoomed")
        reset_window.title('Library Management System - Reset Password')
        reset_window.iconbitmap("l.ico")
        reset_window.geometry("700x700+100-100")
        reset_window.config(bg="#8AAAE5")
    
        colour1 = Label(reset_window, text="      Library Management System                                                                                                                                                                                   Reset Password", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
        colour1.pack()
        colour2 = Label(reset_window, bg="#6D7ACF", width=240, height=3)
        colour2.pack(side=BOTTOM)
    
        Label_reset_password = Label(reset_window, text="Reset Your Password?", font=("Arial Black", "25"), fg="blue", bg='#8AAAE5', width=50)
        Label_reset_password.pack(padx=20, pady=30)
    
        label_username = Label(reset_window, text="Username", font=("Arial", "20"), bg='#8AAAE5')
        label_username.place(x=150, y=170)
        username_Entry = Entry(reset_window, font=("Arial", "20"), fg="black", width=17)
        username_Entry.place(x=400, y=170)
    
        old_password = Label(reset_window, text="      Old Password", font=("Arial", "20"), bg='#8AAAE5')
        old_password.place(x=80, y=230)
        old_password_Entry = Entry(reset_window, font=("Arial", "20"), fg="black", width=17, show='*')
        old_password_Entry.place(x=400, y=230)
    
        type_new_password = Label(reset_window, text="Type New Password", font=("Arial", "20"), bg='#8AAAE5')
        type_new_password.place(x=80, y=290)
        type_new_password_Entry = Entry(reset_window, font=("Arial", "20"), fg="black", width=17, show='*')
        type_new_password_Entry.place(x=400, y=290)
    
        retype_password = Label(reset_window, text="  Retype password", bg='#8AAAE5', font=("Arial", "20"))
        retype_password.place(x=80, y=350)
        retype_Entry = Entry(reset_window, font=("Arial", "20"), width=17, show='*')
        retype_Entry.place(x=400, y=350)
    
        def confirm_fun():
            username = username_Entry.get()
            old_password = old_password_Entry.get()
            new_password = type_new_password_Entry.get()
            retype_password = retype_Entry.get()
            
            if username and old_password and new_password and retype_password:
                if new_password == retype_password:
                    conn = sqlite3.connect('Library_management_system.db')
                    c = conn.cursor()
                    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, old_password))
                    result = c.fetchone()
                    
                    if result:
                        c.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
                        conn.commit()
                        messagebox.showinfo("Library Management System", "Password Reset Successfully")
                        reset_window.destroy()  
                        login_window.deiconify()  #====================================== Redirect to the login window
                    else:
                        messagebox.showerror("Error", "Invalid username or old password")
                    conn.close()
                else:
                    messagebox.showerror("Error", "New password and retyped password do not match")
            else:
                messagebox.showerror("Error", "Please fill out all fields")
    
        confirm_button = Button(reset_window, text="Confirm", fg="green", bg="white", font=("Arial", "15"), width=8, command=confirm_fun)
        confirm_button.place(x=950, y=600)
    
        def exit_but():
            messagebox.showinfo("Library Management System", "Exited")
            reset_window.destroy()  
            login_window.deiconify()# ==================================================Redirect to the login window
    
        Exit_button = Button(reset_window, text="Exit", fg="red", bg="white", font=("Arial", "15"), width=8, command=exit_but)
        Exit_button.place(x=500, y=600)

    reset_Button = Button(login_window, text="Reset Password?", font=("4"), fg="black", bg="white", command=open_reset_password_window)
    reset_Button.place(x=1060, y=550, height=35)

    placeholder = 'Enter Username or Email'
    User_Entry = Entry(login_window, font="20", bg='white', fg="black")
    User_Entry.place(x=900, y=310, height=35, width=235)
    User_Entry.insert(0, placeholder)
    User_Entry.bind('<FocusIn>', lambda event, text=placeholder: onclick(event, text))
    User_Entry.bind('<FocusOut>', lambda event, text=placeholder: offclick(event, text))

    placeholder1 = 'Enter Password'
    password_Entry = Entry(login_window, font="20", show="*")
    password_Entry.place(x=900, y=397)
    password_Entry.insert(0, placeholder1)
    password_Entry.bind('<FocusIn>', lambda event, text=placeholder1: onclick(event, text))
    password_Entry.bind('<FocusOut>', lambda event, text=placeholder1: offclick(event, text))

    def add():
        if a.get() == 0:
            password_Entry.config(show="*")
        else:
            password_Entry.config(show="")

    a = IntVar()
    Show_Password_Button1 = Checkbutton(login_window, text="Show Password", variable=a, command=add, font="20")
    Show_Password_Button1.place(x=900, y=460)
       

colour1 = Label(text="    Library Management System                                                           Welcome to BookWarica Library",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)
colour2.pack(side=BOTTOM)

library_photo  = Image.open("y.png")
c=library_photo.resize((300,250))
r = ImageTk.PhotoImage(c)                
image1=Label(image=r,bg="#8AAAE5").pack()

name1 = Label(text="Library",font=("Arial Bold","20"),fg="#34A853",bg="#8AAAE5")
name1.place(x=600,y=200)

name2 = Label(text="Management",font=("Arial Bold","20"),fg="#FF7A00",bg="#8AAAE5")
name2.place(x=705,y=200)

name3 = Label(text="System",font=("Arial Bold","20"),fg="#34A853",bg="#8AAAE5")
name3.place(x=880,y=200)

label1 = Label(bg="#4285F4",height=3,width=100)
label1.place(x=440,y=245)

yet_name = Label(text="Don't have a account yet?",font=("Arial Bold","15"),fg="black",bg="#4285F4")
yet_name.place(x=450,y=258)

sign_up_button = Button(text="Sign up",font=("Arial Bold","10"),fg="black",bg="#4285F4",command=open_signup_window)
sign_up_button.place(x=1050,y=258)

introduction_label = Label(text="Introduction",font=("Arial Bold","20"),fg="#CC0000",bg="#8AAAE5")
introduction_label.place(x=700,y=320)

intRo_text =  Label(text="Libraries store the energy that fuels the imagination \n        They open up windows to the world and inspire us to explore and achieve,\n and contribute to improving our quality of life.",font=("Arial","15"),fg="black",bg="#8AAAE5")
intRo_text.place(x=440,y=360)

intRo_text2 =  Label(text="Nothing is pleasanter than exploring a library \n So for exploring more click Sign up/Sign in ",font=("Arial","15"),fg="black",bg="#8AAAE5")
intRo_text2.place(x=600,y=450)

btn_Sign_in = Button(text="Sign in",font=("Arial","15"),bg="#6D7ACF",command=open_login_window)
btn_Sign_in.place(x=1520,y=80,anchor="e")

Bottom_text = Label(text="BookWarica  LiBrarY",font=("Arial Bold","15"),fg="black",bg="#6D7ACF")
Bottom_text.place(x=680,y=750)


#=================================================           Function to open admin dashboard           ==========================
def open_admin_dashboard():
    admin_dashboard = Toplevel()
    admin_dashboard.title("Admin Dashboard")
    admin_dashboard.geometry("700x700")
    admin_dashboard.config(bg="#8AAAE5")
    admin_dashboard.iconbitmap("l.ico")

    colour2 = Label(admin_dashboard, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    Name_label = Label(admin_dashboard, text="Library Management System", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    Name_label.pack()
    Admin_Dasboard = Label(admin_dashboard, text="ADMIN DASHBOARD", font=("Arial Black", "20"), fg="black", bg='#8AAAE5', width=50)
    Admin_Dasboard.place(x=280, y=60)

    def open_add_book():
        admin_dashboard.destroy()
        import a5_Admin_add_book

    Add_Book_Button = Button(admin_dashboard, text="    +Add Book    ", bg="white", font="50", command=open_add_book)
    Add_Book_Button.place(x=100, y=220)

    def open_book_list():
        admin_dashboard.destroy()
        import a6_admin_booklist

    BookList_Button = Button(admin_dashboard, text="     Book List      ", bg="white", font="50", command=open_book_list)
    BookList_Button.place(x=100, y=280)

    def open_add_member():
        admin_dashboard.destroy()
        import a7_admin_add_memebers_

    Add_Member_Button = Button(admin_dashboard, text="  +Add Member ", bg="white", font="50", command=open_add_member)
    Add_Member_Button.place(x=100, y=340)

    def logout():
        messagebox.showinfo("Library Management System", "Log Out Successfully")
        admin_dashboard.destroy()
        open_login_window()

    logout_button = Button(admin_dashboard, text="Log Out", fg="red", bg="white", font=("Arial", "15"), width=8, command=logout)
    logout_button.place(x=1050, y=450)

    frame1 = Frame(admin_dashboard, bg="#7fa5e8", height=220, width=1600)
    frame1.place(x=0, y=520)

    Enquiry_ = Label(frame1, text="Enquiries:", font=("Arial", "15"), bg="#7fa5e8")
    Enquiry_.place(x=15, y=523)

    Email_id = Label(frame1, text="Email: bookwarica7@gmail.com", font=("Arial", "15"), bg="#7fa5e8")
    Email_id.place(x=15, y=580)

    Contact = Label(frame1, text="Contact: +977 9742869215", font=("Arial", "15"), bg="#7fa5e8")
    Contact.place(x=15, y=610)

    admin_dashboard.state('zoomed')



def open_user_dashboard():
    # ==================================================Create the Toplevel user dashboard window=========================
    user_dashboard_window = Toplevel(root)
    user_dashboard_window.geometry("700x700")
    user_dashboard_window.title("Library Management System")
    user_dashboard_window.config(bg="#8AAAE5")
    user_dashboard_window.iconbitmap("l.ico")

    # ==================================================Add header labels
    colour1 = Label(user_dashboard_window, text="      Library Management System ", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    colour1.pack()

    colour2 = Label(user_dashboard_window, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)
    
    User_Dashboard = Label(user_dashboard_window, text="USER DASHBOARD", font=("Arial Black", 20), fg="black", bg='#8AAAE5', width=50)
    User_Dashboard.place(x=280, y=60)

    
    def borrowfunc():
        user_dashboard_window.destroy()
        import User_borrow_book  # Ensure User_borrow_book is available and correctly imported

    Borrow_Book_Button = Button(user_dashboard_window, text="    Borrow Book    ", bg="white", font="50", command=borrowfunc)
    Borrow_Book_Button.place(x=60, y=140)

    def payfinefunc():
        user_dashboard_window.destroy()
        import User_Payfine  # Ensure User_Payfine is available and correctly imported

    payment_Button = Button(user_dashboard_window, text="       Payment       ", bg="white", font="50", command=payfinefunc)
    payment_Button.place(x=60, y=200)

    def log_outf():
        user_dashboard_window.destroy()
        open_login_window()  # Ensure login is available and correctly imported

    exit_but = Button(user_dashboard_window, text="  Log out ", bg="white", fg="red", font="50", width=8, command=log_outf)
    exit_but.place(x=1050, y=450)

    # =============================================Add buttom frame for contact information
    frame1 = Frame(user_dashboard_window, bg="#7fa5e8", height=220, width=1600)
    frame1.place(x=0, y=520)

    Enquiry_ = Label(frame1, text="Enquiries:", font=("Arial", 15), bg="#7fa5e8")
    Enquiry_.place(x=15, y=523)

    Email_id = Label(frame1, text="Email: bookwarica7@gmail.com", font=("Arial", 15), bg="#7fa5e8")
    Email_id.place(x=15, y=580)
    
    Contact = Label(frame1, text="Contact: +977 9742869215", font=("Arial", 15), bg="#7fa5e8")
    Contact.place(x=15, y=610)

    user_dashboard_window.state('zoomed')
mainloop()
