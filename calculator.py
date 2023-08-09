import tkinter as tk

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")

        self.textbox = tk.Text(self.root, height=3, font=('Arial', 18))
        self.textbox.pack(padx=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)

        self.button_params = {'font': ('Arial', 18), 'height': 2, 'width': 8}

        self.btn1 = tk.Button(self.button_frame, text='1',command=self.one, **self.button_params)
        self.btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.btn2 = tk.Button(self.button_frame, text='2',command=self.two,**self.button_params)
        self.btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.btn3 = tk.Button(self.button_frame, text='3',command=self.three,**self.button_params)
        self.btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.btn4 = tk.Button(self.button_frame, text='4',command=self.four,**self.button_params)
        self.btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

        self.btn5 = tk.Button(self.button_frame, text='5',command=self.five,**self.button_params)
        self.btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.btn6 = tk.Button(self.button_frame, text='6',command=self.six,**self.button_params)
        self.btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

        self.btn7 = tk.Button(self.button_frame, text='7',command=self.seven,**self.button_params)
        self.btn7.grid(row=2, column=0, sticky=tk.W + tk.E)

        self.btn8 = tk.Button(self.button_frame, text='8',command=self.eight,**self.button_params)
        self.btn8.grid(row=2, column=1, sticky=tk.W + tk.E)

        self.btn9 = tk.Button(self.button_frame, text='9',command=self.nine,**self.button_params)
        self.btn9.grid(row=2, column=2, sticky=tk.W + tk.E)

        self.btn_add = tk.Button(self.button_frame, text='+',command=self.plus,**self.button_params)
        self.btn_add.grid(row=3, column=0, sticky=tk.W + tk.E)

        self.btn_minus = tk.Button(self.button_frame, text='-',command=self.subtract,**self.button_params)
        self.btn_minus.grid(row=3, column=1, sticky=tk.W + tk.E)

        self.btn_clear = tk.Button(self.button_frame, text='Clear',command=self.clear,**self.button_params)
        self.btn_clear.grid(row=3, column=2, sticky=tk.W + tk.E)

        self.btn_enter = tk.Button(self.button_frame, text='Enter',command=self.enter,**self.button_params)
        self.btn_enter.grid(row=4, sticky=tk.W + tk.E)

        self.button_frame.pack(fill='x')

        self.root.mainloop()

    def one(self):
        self.textbox.insert(tk.END, 1)
    def two(self):
        self.textbox.insert(tk.END, 2)
    def three(self):
        self.textbox.insert(tk.END, 3)
    def four(self):
        self.textbox.insert(tk.END, 4)
    def five(self):
        self.textbox.insert(tk.END, 5)
    def six(self):
        self.textbox.insert(tk.END, 6)
    def seven(self):
        self.textbox.insert(tk.END, 7)
    def eight(self):
        self.textbox.insert(tk.END, 8)
    def nine(self):
        self.textbox.insert(tk.END, 9)
    def subtract(self):
        self.textbox.insert(tk.END, '-')
    def plus(self):
        self.textbox.insert(tk.END, '+')

    def enter(self):
        expression = self.textbox.get("1.0", tk.END).strip()
        try:
            result = eval(expression)
            self.textbox.delete(1.0, tk.END)
            self.textbox.insert(tk.END, result)
        except:
            self.textbox.delete(1.0, tk.END)
            self.textbox.insert(tk.END, "Error")
    def clear(self):
        self.textbox.delete(1.0, tk.END)



Main()
