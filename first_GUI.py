from tkinter import *

window = Tk()
window.geometry("520x520")
window.title("My first GUI program")

icon = PhotoImage(file='d20.png')
window.iconphoto(True,icon)
window.config(background="black")

window.mainloop()