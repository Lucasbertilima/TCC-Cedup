from tkinter import *

window = Tk()
window.title("TurtleOrg")
window.geometry("400x400")
window.configure(background = "green");

nome = Label(window, text='Nome', width=10).grid(row=0, column=0)
telefone = Label(window, text='Telefone', width=10).grid(row=1, column=0)
email = Label(window, text='Email', width=10).grid(row=2, column=0)
n1 = Entry(window, width=20).grid(row=0, column=1)
d1 = Entry(window, width=20).grid(row=1, column=1)
p1 = Entry(window, width=20).grid(row=2, column=1)
btn = Button(window, text="Cadastrar", width=20).grid(row=3, column=1)
window.mainloop()