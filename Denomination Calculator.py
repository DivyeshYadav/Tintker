from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox

root = Tk()
rootgeometry =  root.geometry("650x400")
roottitle = root.title("Denomination Calculator")
upload = Image.open("app_img.jpg")
image = upload.resize((300,300))
image1 = ImageTk.PhotoImage(image)
label1 = Label(root, image = image1, bg = "light blue")
label1.place(x = 180, y = 20)
label = Label(root, text="Hey user! welcome to Denomination Calculator", bg="light blue")
label.place(relx = 0.5, y = 340, anchor=CENTER)

def msg():
    Msgbox = messagebox.showinfo("Alert","Do you want to use Cash Denomination Calculator?")
    if Msgbox == 'ok':
        topwin()

button = Button(root, text = "Let's Get started", bg = "orange", fg = "black" ,command=msg())
button.place(x = 260, y = 360)

    
def topwin():
    top = Toplevel()
    top.geometry("600x350+50+50")
    top.title("toplevel")
    top.config()
root.mainloop()