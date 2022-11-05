from tkinter import *
from tkcalendar import Calendar

# create window
root=Tk()

#set geometry
root.geometry("400x400")

#add Calendar
cal = Calendar(root, selectmode = 'day',
                year = 2022, month = 5,
                day=22)

cal.pack(pady = 20)

def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())

#add button and label
Button(root, text = "Get Date",
        command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

root.mainloop()
