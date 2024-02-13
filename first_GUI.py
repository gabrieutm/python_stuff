from tkinter import *

window = Tk()
#window.geometry("520x520")
window.title("My first GUI program")

icon = PhotoImage(file='d20.png')
window.iconphoto(True,icon)
#window.config(background='black')

photo = PhotoImage(file='dndwallpaper.png')

label = Label(window,text="Hello player",
              font=('Arial',30,'italic'),
              fg='black',
              bg='white',
              relief=RAISED,
              bd=5,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')

label.pack()

window.mainloop()