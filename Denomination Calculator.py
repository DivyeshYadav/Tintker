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
    top.config(bg="light grey")


    label = Label(top, text="Enter total amount", bg="light grey")
    entry = Entry(top)
    lbl = Label(top, text = "Here are number of notes for each denomination")

    l1 = Label(top, text = "1000", bg = "light grey")
    l2 = Label(top, text = "500", bg = "light grey")
    l3 = Label(top, text = "100", bg = "light grey")
    
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note1000 = amount // 2000 
            amount %= 1000
            note500 = amount // 2000 
            amount %= 1000
            note100 = amount // 2000
            amount %= 1000

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)


            t1.insert(END, str(note1000))
            t1.insert(END, str(note500))    
            t1.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error","Please Enter a valid number")
    btn = Button(top, text="Calculate", command = calculator, bg = "brown", fg ="white" )
label.place(x=230, y=50  )    
entry.place(x=200, y=80  )
btn.place(x=240, y = 120)
lbl.place(x = 140 ,y = 170)

l1.place(x=180,y=200)
l2.place(x=180,y=230)
l3.place(x=180,y=260)

t1.place(x= 270, y=200)
t2.place(x= 270, y=200)
t3.place(x= 270, y=200)
root.mainloop()