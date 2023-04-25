from tkinter import *

window = Tk()

window.title("Grid Manager")
window.geometry("400x300+10+10")
#button = Button(window,width=10)
#button.grid(row=0,column=0)
txt = Entry(window, bd=2, justify="center")
txt.grid(row=0, column=0)
txt.insert(0,"row 0 column 0")

txt1 = Entry(window, bd=2, justify="center")
txt1.grid(row=0, column=1)
txt1.insert(0, "row 0 column 1")

txt2 = Entry(window, bd=2, justify="center")
txt2.grid(row=0, column=2)
txt2.insert(0, "row 0 column 2")

txt3 = Entry(window, bd=2, justify="center")
txt3.grid(row=1, column=0)
txt3.insert(0, "row 1 column 0")

txt4 = Entry(window, bd=2, justify="center")
txt4.grid(row=1, column=1)
txt4.insert(0, "row 1 column 1")

txt5 = Entry(window, bd=2, justify="center")
txt5.grid(row=1, column=2)
txt5.insert(0, "row 1 column 2")

txt6 = Entry(window, bd=2, justify="center")
txt6.grid(row=2, column=0)
txt6.insert(0, "row 2 column 0")

txt7 = Entry(window, bd=2, justify="center")
txt7.grid(row=2, column=1)
txt7.insert(0, "row 2 column 1")

txt8 = Entry(window, bd=2, justify="center")
txt8.grid(row=2, column=2)
txt8.insert(0, "row 2 column 2")

txt8 = Entry(window, bd=2, justify="center")
txt8.grid(row=3, column=0)
txt8.insert(0, "row 3 column 0")

txt8 = Entry(window, bd=2, justify="center")
txt8.grid(row=3, column=1)
txt8.insert(0, "row 3 column 1")

txt8 = Entry(window, bd=2, justify="center")
txt8.grid(row=3, column=2)
txt8.insert(0, "row 3 column 2")


window.mainloop()