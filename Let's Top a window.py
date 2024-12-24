from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top, text = "This is a toplevel window")
    l2.pack()
    btn2 = Button(top, text = "Hi I am Divyesh Nice to meet you")
    btn2.pack
    top.mainloop()


l = Label(root, text = "This is root window")
l.pack()
btn = Button(root, text = "Click here to open another window", comman = topwin)  
btn.pack()
root.mainloop()