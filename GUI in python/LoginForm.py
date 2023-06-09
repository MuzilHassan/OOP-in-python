
from tkinter import *
from PIL import ImageTk, Image
from  tkinter import  messagebox

def handle_login():
    email= email_input.get()
    password=password_input.get()

    if email=="muzilhassan9@gmail.com" and password=="12345" :
        return messagebox.showinfo("succeess","Login Successfull")
    messagebox.showerror("Error","Login Failed")

root= Tk()

root.title("Login form")



root.geometry('400x500')

root.configure(background="#0096DC")
img=Image.open("Daraz-Logo.png")
comp_img=img.resize((70,70))
img=ImageTk.PhotoImage(comp_img)

img_label=Label(root,image=img)

img_label.pack(pady=(10,10))

text_label=Label(root, text="Daraz",fg="white", bg="#0096DC")
text_label.pack()
text_label.config(font=("verdana",24))

email_label=Label(root, text="Enter Your Email",fg="white", bg="#0096DC")
email_label.pack(pady=(20,5))
email_input=Entry(root,width=50)
email_input.pack(pady=(1,10),ipady=6)
password_label=Label(root, text="Enter Your Password",fg="white", bg="#0096DC")
password_label.pack(pady=(20,5))
password_input=Entry(root,width=50)
password_input.pack(pady=(1,20),ipady=6)

login_btn=Button(root,text="Login here",bg="white", fg="black", width=30,command=handle_login )
login_btn.pack()
root.mainloop()