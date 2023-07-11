from tkinter import *
import tkinter.messagebox as msgbox
form=Tk()
form.geometry("500x500")

lbltitle=Label(form,text="USER NAME :",font=("Arial",20,"bold"))
lbltitle.grid(row=1,column=1)
etun=Entry(form,width=50)
etun.grid(row=1,column=2)

lbltitle=Label(form,text="PASSWORD :",font=("Arial",20,"bold"))
lbltitle.grid(row=2,column=1)
etp=Entry(form,width=50,show="*")
etp.grid(row=2,column=2)

def exist():
    un=etun.get()
    p=etp.get()
    if(un=="admin" and p=="1234"):
        msgbox.showinfo("success","Login successful")
    else:
        msgbox.showinfo("invalid","Incorrect User Name or Password")


btnexist=Button(form,text="login",command=exist,font=("Arial",14,"bold"))
btnexist.grid(row=3,column=2)
form.mainloop()