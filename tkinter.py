from tkinter import *

window = Tk()
window.title('Tkinter Sample Window')
window.geometry("400 x 400")

greeting=Label(text="Hello User ", bg="white", fg="black")
button=Button(text="click me ",bg="black" ,fg="white")

entry=Entry(bg="red", fg="blue")
greeting.pack()
button.pack()
entry.pack()

frame=Frame(master=window,relief=RAISED, borderwidth=6)
frame.pack()

label2=Label( master=frame, text="Hello User once again  ", bg="white", fg="black")
label2.pack()

window.mainloop()
