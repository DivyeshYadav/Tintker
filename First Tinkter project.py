import tkinter as tk
win = tk.Tk()
win.title("First Project")
win.geometry("300x300")

button = tk.Button(text = "click me",fg= "white", bg = "black", height =  3, width = 20)
button.pack()
greet = tk.Label(text="Hi", fg = "red", bg = "yellow", height = 5, width = 50)
greet.pack()
input = tk.Entry(fg = "white", bg = "black",width = 50)
input.pack()
textline = tk.Text(fg = "white", bg =  "black", height=30, width=50)
textline.pack()
win.mainloop()
