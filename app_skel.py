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

class ControlFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.title('ControlFrame')
        self.geometry('400x150')
        self.pack()

        self.__create_widgets()

    def __create_widgets(self):
        QuoteFrame.pack()
        ResultFrame.pack()
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)



class QuoteFrame(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Quote Frame")
        label.pack(padx=10, pady=10)


        # setup the grid layout manager


        self.pack()
        self.__create_widgets(controller)

    def __create_widgets(self, controller):
        self.customer_label = ttk.Label(self, text="Customer")
        self.customer_label.pack()
        self.customer_entry = ttk.Entry(self, width=20)
        self.customer_entry.pack()
        self.customer_entry.focus()




        self.two_x_button = ttk.Button(self, text='2XL Cost')
        self.two_x_button['command']= self.open_two_x
        self.two_x_button.pack()

        self.three_x_button = ttk.Button(self, text='3XL Cost')
        self.three_x_button['command']= self.open_three_x
        self.three_x_button.pack()

        switch_window_button = tk.Button(
            self,
            text="Generate Quote",
            command=lambda: controller.show_frame(ResultFrame),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

    def open_two_x(self):
        window_two = Window(self)
        window_two.grab_set()

    def open_three_x(self):
        window_three = WindowFrame(self)
        window_three.grab_set()




class ResultFrame(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)
        # setup the grid layout manager

        self.switch_window_button = tk.Button(self, text='Change', command=lambda: controller.show_frame(CompletionScreen))
        self.switch_window_button.pack(side="bottom", fill=tk.X)
        self.__create_widgets()


    def __create_widgets(self):
        self.customer_label = ttk.Label(self, text="Customer")
        self.customer_label.pack(side="left")
        self.customer_entry = ttk.Entry(self, width=20)
        self.customer_entry.pack(side="left")
        self.customer_entry.focus()




class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Complete")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(QuoteFrame)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Quote Calculator')
        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (QuoteFrame, ResultFrame, CompletionScreen):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(QuoteFrame)

    def show_frame(self, cont):
        frame=self.frames[cont]

        frame.tkraise()


        # layout on the root window



if __name__ == "__main__":
    app = App()
    app.mainloop()
