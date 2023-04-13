from tkinter import *
window = Tk()
window.geometry("500x300")
window.title("Midterm Exam Problem 2")

class GUI:
    def __init__(self, win):
        self.Title = Label(text = "My Full Name")
        self.Title.place(x=200, y=30)

        self.gn = Label(text = "Enter Given Name:")
        self.gn.place(x=100,y=55)
        self.gne = Entry()
        self.gne.place(x=300, y=55)

        self.mn = Label(text = "Enter Middle Name:")
        self.mn.place(x=100, y=80)
        self.mne = Entry()
        self.mne.place(x=300, y=80)

        self.ln = Label(text = "Enter Last Name:")
        self.ln.place(x=100, y=110)
        self.lne = Entry()
        self.lne.place(x=300, y=110)

        self.fn = Label(text = "My Full Name is")
        self.fn.place(x=100, y=140)
        self.fne = Entry(width=30)
        self.fne.place(x=300, y=140)

        self.button = Button(text = "Show Full Name")
        self.button.place(x=200, y=170)
        self.button.bind("<Button-1>", self.display)

        self.button = Button(text = "Clear All")
        self.button.place(x=200, y=200)
        self.button.bind("<Button-1>", self.display)


    def display(self, display):
        self.fne.delete(0,'end')
        full_name = (str(self.gne.get())+" "+ str(self.mne.get())+" "+ str(self.lne.get()))
        self.fne.insert(END, str(full_name))
    def display(self,display):
        self.gne.delete(0,'end')
        self.gne.insert(END, str(given_name))
        self.mne.delete(0, 'end')
        self.mne.insert(END, str(given_name))
        self.lne.delete(0, 'end')
        self.lne.insert(END, str(given_name))
        self.fne.delete(0, 'end')
        self.fne.insert(END, str(given_name))



mywin = GUI(window)
window.mainloop()