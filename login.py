from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3   

lb = Tk()  
lb.title("Library Management System") 
lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") 
lb.config(bg="#8AAAE5")  

admin = Label(lb, text="Library Login", font=("Bold Arial", "30"), bg="#8AAAE5", fg="#000000")
admin.place(x=900, y=150)

library_photo = Image.open("zbc.png")
c = library_photo.resize((850, 690))
r = ImageTk.PhotoImage(c)                
image1 = Label(image=r).place(x=0, y=50)
563


colour1 = Label(text="    Library Management System", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
colour1.pack()

colour2 = Label(bg="#6D7ACF", width=240, height=3)
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
            lb.destroy()
            import Admin_Dashboard  # Redirect to the admin dashboard
        else:
            messagebox.showinfo("Library Management System", "Welcome User!")
            lb.destroy()
            import User_Dashboard  # Redirect to the user dashboard
    else:
        messagebox.showerror("Error", "Invalid credentials")

    conn.close()

username = Label(lb, text="Username", font="34", bg="#8AAAE5")
username.place(x=900, y=270)

password = Label(lb, text="Password", font="34", bg="#8AAAE5", fg="black")
password.place(x=900, y=360)

log_inButton = Button(lb, text="Login", font=("4"), fg="black", bg="white", command=login)
log_inButton.place(x=900, y=550, height=35)       

def onclick(event, text):
    if event.widget.get() == text:
        event.widget.delete(0, END)
        event.widget.insert(0, '')

def offclick(event, text):
    if event.widget.get() == '':
        event.widget.insert(0, text)


def resetf():
    lb.destroy() 
    import resetpassword  

reset_Button = Button(lb, text="Reset Password?", font=("4"), fg="black", bg="white", command=resetf)
reset_Button.place(x=1060, y=550, height=35)

placeholder = 'Enter Username or Email'
User_Entry = Entry(lb, font="20", bg='white', fg="black")
User_Entry.place(x=900, y=310, height=35, width=235)
User_Entry.insert(0, placeholder)
User_Entry.bind('<FocusIn>', lambda event, text=placeholder: onclick(event, text))
User_Entry.bind('<FocusOut>', lambda event, text=placeholder: offclick(event, text))

placeholder1 = 'Enter Password'
password_Entry = Entry(lb, font="20", show="*")
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
Show_Password_Button1 = Checkbutton(text="Show Password", variable=a, command=add, font="20")
Show_Password_Button1.place(x=900, y=460)

lb.state('zoomed')
mainloop()


lb.mainloop()
