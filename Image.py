from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox

root = Tk()
rootgeometry =  root.geometry("500x500")
roottitle = root.title("Image")

img = Image.open("images.jpeg")
img1 = ImageTk.PhotoImage(img)
lable = Label(root, image=img1, height= 300 , width=300)
lable.place(x=50, y=20)
lable1 = Label(text = "This is  a dog", fg = "black", bg = "white", height=20, width=50)
lable1.place(x = 40, y = 300)

messeage = messagebox.showwarning("Alert","don't use this file it has corona virus")
messeage.place()
root.mainloop()