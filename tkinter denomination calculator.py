from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root=Tk()
root.title('Denominator Counter')
root.configure(bg='light blue')
root.geometry('650x400')
upload=Image.open("paisa hi paisa.jpeg")
upload=upload.resize((300,300))
image-ImageTk.PhotoImage(upload)
label=Label(root,image=image,bg='light blue')
label.place(x=180,y=20)
label1=Label(root,
             text="Hey User! Welcome to denomiantion counter applcation.",
             bg='light blue')
label1.place(relx=0.5,y=340, anchor=CENTER)
def msg():
    MsgBox=messagebox.showinfo(
        "Alert","Do you want to calculate the denomination count?")
    if MsgBox =='ok':
        topwin()
button1=Button(root,
               text="Let's get started!",
               command=msg,
               bg='brown'
               fg='white')
button1.place(x=260,y=360)
