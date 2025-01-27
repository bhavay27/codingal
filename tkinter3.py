from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("DDLJ")
root.geometry("400X400")
upload=Image.open("admin.png")
image=ImageTk.PhotoImage(upload)
label=Label(image=image , height=350, width=300)
label.place(x=50,y=0)
root.mainloop()
