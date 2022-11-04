import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

class QuoteFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        self.__create_widgets()

    def __create_widgets(self):
        ttk.Label(self, text="Customer").grid(column=1, row=1, sticky=tk.W)
        customer = ttk.Entry(self, width=20)
        customer.focus()
        customer.grid(column=2, row=1, sticky=tk.W)

        ttk.Label(self, text="Job Name").grid(column=3, row=1, sticky=tk.E)
        job = ttk.Entry(self, width=20)
        job.grid(column=4, row=1, sticky=tk.E)

        ttk.Label(self, text="Item Number").grid(column=1, row=2, sticky=tk.W)
        item = ttk.Entry(self, width=20)
        item.grid(column=2, row=2, sticky=tk.W)

        ttk.Label(self, text="Item Color").grid(column=3, row=2, sticky=tk.E)
        color = ttk.Entry(self, width=20)
        color.grid(column=4, row=2, sticky=tk.E)

        ttk.Label(self, text="Blank Cost").grid(column=1, row=3, sticky=tk.W)
        blank_cost = ttk.Entry(self, width=20)
        blank_cost.grid(column=2, row=3, sticky=tk.W)

        ttk.Label(self, text="Quantity").grid(column=3, row=3, sticky=tk.E)
        quantity = ttk.Entry(self, width=20)
        quantity.grid(column=4, row=3, sticky=tk.E)

        two_x_check = tk.StringVar()
        two_x_checkbox = ttk.Checkbutton(
            self,
            text='2XLs?',
            variable=two_x_check)
        two_x_checkbox.grid(column=1, row=4, sticky=tk.W)

        three_x_check = tk.StringVar()
        three_x_checkbox = ttk.Checkbutton(
            self,
            text='3XLs?',
            variable=three_x_check,
            command=findwindow())

        three_x_checkbox.grid(column=1, row=4, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)

class FindWindow(tk.Toplevel):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs )
        self.geometry('350x100')
        self.title('Find and Replace')

        self.__create_widgets()

    def __create_widgets(self):
        two_x_check = tk.StringVar()
        two_x_checkbox = ttk.Checkbutton(
            self,
            text='2XLs?',
            variable=two_x_check)
        two_x_checkbox.grid(column=1, row=4, sticky=tk.W)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Quote Calculator')
        self.geometry('400x150')
        self.resizable(0, 0)
        # windows only (remove the minimize/maximize button)
        self.attributes('-toolwindow', True)

        # layout on the root window

        self.__create_widgets()

    def __create_widgets(self):
        # create the input frame
        quote_frame = QuoteFrame(self)
        quote_frame.grid(column=0, row=0)
        quote_frame.focus()




if __name__ == "__main__":
    app = App()
    QuoteFrame(app)
    app.mainloop()
