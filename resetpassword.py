from tkinter import *
from tkinter import messagebox
import sqlite3

# ============================================================Initialize Tkinter window
lb = Tk()
lb.state("zoomed")
lb.title('Library Management System')
lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100")
lb.config(bg="#8AAAE5")

colour1 = Label(text="      Library Management System                                                                                                                                                                                   Reset Password", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF", width=240, height=3)
colour2.pack(side=BOTTOM)

Label_reset_password = Label(lb, text="Reset Your Password?", font=("Arial Black", "25"), fg="blue", bg='#8AAAE5', width=50)
Label_reset_password.pack(padx=20, pady=30)

label_username = Label(lb, text="Username", font=("Arial", "20"), bg='#8AAAE5')
label_username.place(x=150, y=170)
username_Entry = Entry(lb, font=("Arial", "20"), fg="black", width=17)
username_Entry.place(x=400, y=170)

old_password = Label(lb, text="      Old Password", font=("Arial", "20"), bg='#8AAAE5')
old_password.place(x=80, y=230)
old_password_Entry = Entry(lb, font=("Arial", "20"), fg="black", width=17, show='*')
old_password_Entry.place(x=400, y=230)

type_new_password = Label(lb, text="Type New Password", font=("Arial", "20"), bg='#8AAAE5')
type_new_password.place(x=80, y=290)
type_new_password_Entry = Entry(lb, font=("Arial", "20"), fg="black", width=17, show='*')
type_new_password_Entry.place(x=400, y=290)

retype_password = Label(lb, text="  Retype password", bg='#8AAAE5', font=("Arial", "20"))
retype_password.place(x=80, y=350)
retype_Entry = Entry(lb, font=("Arial", "20"), width=17, show='*')
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
                lb.destroy()  
                import login  # Redirect to the login window
            else:
                messagebox.showerror("Error", "Invalid username or old password")
            conn.close()
        else:
            messagebox.showerror("Error", "New password and retyped password do not match")
    else:
        messagebox.showerror("Error", "Please fill out all fields")

confirm_button = Button(lb, text="Confirm", fg="green", bg="white", font=("Arial", "15"), width=8, command=confirm_fun)
confirm_button.place(x=950, y=600)

def exit_but():
    messagebox.showinfo("Library Management System", "Exited")
    lb.destroy()  
    import login  # Redirect to the login window

Exit_button = Button(lb, text="Exit", fg="red", bg="white", font=("Arial", "15"), width=8, command=exit_but)
Exit_button.place(x=500, y=600)

mainloop()
