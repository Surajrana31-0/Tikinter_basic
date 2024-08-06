from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox




lb =Tk()  
lb.title(" Library Management System ")
lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") 
lb.config(bg="#8AAAE5") 
lb.state("zoomed")
 
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

yet_name = Label(text="Dont have a account yet?",font=("Arial Bold","15"),fg="black",bg="#4285F4")
yet_name.place(x=450,y=258)

def open_signup_window1():
    lb.destroy()  
    import signup # Import and run the login script

sign_up_button = Button(text="Sign up",font=("Arial Bold","10"),fg="black",bg="#4285F4",command=open_signup_window1)
sign_up_button.place(x=1050,y=258)
introduction_label = Label(text="Introduction",font=("Arial Bold","20"),fg="#CC0000",bg="#8AAAE5")
introduction_label.place(x=700,y=320)


intRo_text =  Label(text="Libraries store the energy that fuels the imagination \n        They open up windows to the world and inspire us to explore and achieve,\n and contribute to improving our quality of life.",font=("Arial","15"),fg="black",bg="#8AAAE5")
intRo_text.place(x=440,y=360)

intRo_text2 =  Label(text="Nothing is pleasanter than exploring a library \n So for exploring more click Sign up/Sign in ",font=("Arial","15"),fg="black",bg="#8AAAE5")
intRo_text2.place(x=600,y=450)


def open_login_window():
    lb.destroy()  
    import login
    # Close the current window
    # Import and run the login script
   

btn_Sign_in = Button(text="Sign in",font=("Arial","15"),bg="#6D7ACF",command=open_login_window)
btn_Sign_in.place(x=1520,y=80,anchor="e")



Bottom_text = Label(text="BookWarica  LiBrarY",font=("Arial Bold","15"),fg="black",bg="#6D7ACF")
Bottom_text.place(x=680,y=750)

mainloop()


