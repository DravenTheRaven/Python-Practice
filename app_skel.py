import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror



class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)


        self.title('Toplevel Window')
        self.__create_widgets()


    def __create_widgets(self):
        self.three_x_label = ttk.Label(self, text="2XL Cost")
        self.three_x_label.grid(column=0, row=0)

class WindowFrame(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)


        self.title('Toplevel Window')
        self.__create_widgets()


    def __create_widgets(self):
        self.three_x_label = ttk.Label(self, text="3XL Cost")
        self.three_x_label.grid(column=0, row=0)

class QuoteFrame(ttk.Frame):
    def __init__(self):
        super().__init__()
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)

        self.pack()
        self.__create_widgets()

    def __create_widgets(self):
        self.customer_label = ttk.Label(self, text="Customer")
        self.customer_label.grid(column=1, row=1, sticky=tk.W)
        self.customer_entry = ttk.Entry(self, width=20)
        self.customer_entry.grid(column=2, row=1, sticky=tk.W)
        self.customer_entry.focus()




        self.two_x_button = ttk.Button(self, text='2XL Cost')
        self.two_x_button['command']= self.open_two_x
        self.two_x_button.grid(column=0, row=0)

        self.three_x_button = ttk.Button(self, text='3XL Cost')
        self.three_x_button['command']= self.open_three_x
        self.three_x_button.grid(column=0, row=2)

        self.change_button = ttk.Button(self, text='Change')
        self.change_button['command']=self.__change_frames(ResultFrame)
        self.change_button.grid(column=0, row=3)

    def open_two_x(self):
        window_two = Window(self)
        window_two.grab_set()

    def open_three_x(self):
        window_three = WindowFrame(self)
        window_three.grab_set()

    def __change_frames(self, ResultFrame):

        ResultFrame.__create_widgets()
        ResultFrame.grid(self)
        self.grid_remove()


class ResultFrame(ttk.Frame):
    def __init__(self, QuoteFrame):
        super().__init__(QuoteFrame)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)

        self.__create_widgets()


    def __create_widgets(self):
        self.customer_label = ttk.Label(self, text="Customer")
        self.customer_label.grid(column=1, row=1, sticky=tk.W)
        self.customer_entry = ttk.Entry(self, width=20)
        self.customer_entry.grid(column=2, row=1, sticky=tk.W)
        self.customer_entry.focus()

        self.change_button = ttk.Button(self, text='Change')
        self.change_button['command']=self.__change_frames
        self.change_button.grid(column=0, row=3)

    def __change_frames(QuoteFrame):
        QuoteFrame.pack()



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Quote Calculator')
        self.geometry('400x150')
        self.resizable(0, 0)
        # windows only (remove the minimize/maximize button)
        self.attributes('-toolwindow', True)

        # layout on the root window


    def open_window(self):
        window = ResultFrame(self)
        window.pack(self)



if __name__ == "__main__":
    app = App()

    quote_frame = QuoteFrame(app)

    app.mainloop()
