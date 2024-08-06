from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

lb = Tk()  
lb.title("Library Management System") 
lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") # Adjust window position
lb.config(bg="#8AAAE5")  # Set background color
lb.state("zoomed")

# UI components
colour1 = Label(text="      Library Management System                                                                                                                                                                                       Signup now", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF", width=240, height=3)   # Color the top and bottom sides
colour2.pack(side=BOTTOM)

Sign_Up_page = Label(text="Signup Page", bg="#8AAAE5", font=("Bold Arial", "17"), width=13, height=1)   # Signup page label
Sign_Up_page.place(x=710, y=70)

Label_Username = Label(text="Username", bg="#8AAAE5", font=("Bold Arial", "20"))
Label_Username.place(x=200, y=170)
EntryUsername = Entry(lb, width=15, font=('Arial 20'))
EntryUsername.place(x=350, y=170)

date_of_birth_name = Label(text="Date of Birth", bg="#8AAAE5", font=("Bold Arial", "20"))
date_of_birth_name.place(x=180, y=225)
Entry_date_of_birth = Entry(lb, width=15, font=('Arial 20'))
Entry_date_of_birth.place(x=350, y=225)

Contact_name = Label(text="Contact", bg="#8AAAE5", font=("Bold Arial", "20"))
Contact_name.place(x=230, y=280)
Entry_contact = Entry(lb, width=15, font=('Arial 20'))
Entry_contact.place(x=350, y=280)

Addres_name = Label(text="Address", bg="#8AAAE5", font=("Bold Arial", "20"))
Addres_name.place(x=230, y=335)
Addres_Entry = Entry(lb, width=15, font=('Arial 20'))
Addres_Entry.place(x=350, y=335)

Password_label = Label(text="Password", bg="#8AAAE5", font=("Bold Arial", "20"))
Password_label.place(x=230, y=390)
Password_entry = Entry(lb, show="*", width=15, font=('Arial 20'))
Password_entry.place(x=350, y=390)

# Role selection
Role_label = Label(text="Role", bg="#8AAAE5", font=("Bold Arial", "20"))
Role_label.place(x=230, y=445)
role_var = StringVar(value="user")
Role_admin = Radiobutton(lb, text="Admin", variable=role_var, value="admin", bg="#8AAAE5", font=("Bold Arial", "20"))
Role_admin.place(x=350, y=440)
Role_user = Radiobutton(lb, text="User", variable=role_var, value="user", bg="#8AAAE5", font=("Bold Arial", "20"))
Role_user.place(x=450, y=440)

# Database connection and creation
conn = sqlite3.connect('Library_management_system.db')
c = conn.cursor()

# Create table if not exists
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

# Signup function
def signup():
    username = EntryUsername.get()
    dob = Entry_date_of_birth.get()
    contact = Entry_contact.get()
    address = Addres_Entry.get()
    password = Password_entry.get()
    role = role_var.get()
    
    if username and dob and contact and address and password:
        try:
            # Check if an admin already exists
            c.execute("SELECT COUNT(*) FROM users WHERE role='admin'")
            if role == "admin" and c.fetchone()[0] > 0:
                messagebox.showerror("Error", "Admin account already exists")
                return

            c.execute("INSERT INTO users (username, dob, contact, address, password, role) VALUES (?, ?, ?, ?, ?, ?)", 
                      (username, dob, contact, address, password, role))
            conn.commit()
            messagebox.showinfo("Library Management System", "Sign up successfully")
            lb.destroy()
            import login  # Redirect to the login
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
    else:
        messagebox.showerror("Error", "Please fill out all fields")

Sign_up_page_button = Button(text="Signup", font=('Arial'), command=signup)
Sign_up_page_button.place(x=350, y=500)


def exit_app():
    lb.destroy()
    import Homepage

Button_Exit = Button(text="   Exit   ", font=('Arial'), command=exit_app)
Button_Exit.place(x=1100, y=500)

lb.mainloop()

# ===========================================================Close the database connection when the application exits
conn.close()
