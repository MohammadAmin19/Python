import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bg_color = "#6b6e6c"
        self.button_color = "#7dcad4"
        self.text_color = "#eeeeee"
        self.error_bg = "#ff3d00"
        self.finish_color = "#14cc45"
        self.clear_color = "#d50000"

        self.title("Calculator")
        self.geometry("400x600")
        self.config(bg = self.bg_color )
        self.resizable(False,False)

        # Entry for result
        self.result = tk.Entry(self, font=('Arial', 32) , bg = self.bg_color , fg = self.text_color , insertbackground='white')
      
        self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=40, ipady=20, sticky=tk.W + tk.E)
        self.result.config(justify=tk.LEFT )
        self.grid_columnconfigure(0, weight=1)

        # Label for error messages
        self.error_label = tk.Label(self, text="", fg="white", font=('Arial', 14) , bg=self.bg_color)
        self.error_label.grid(row=1, column=0, columnspan=4, padx=30, pady=(0, 10), sticky="w") 
        
        # Frame for buttons
        button_frame = tk.Frame(self , bg=self.bg_color)
        button_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        self.create_button('1', button_frame, 0, 0, lambda: self.add_number(1))
        self.create_button('2', button_frame, 0, 1, lambda: self.add_number(2))
        self.create_button('3', button_frame, 0, 2, lambda: self.add_number(3))
        self.create_button('4', button_frame, 1, 0, lambda: self.add_number(4))
        self.create_button('5', button_frame, 1, 1, lambda: self.add_number(5))
        self.create_button('6', button_frame, 1, 2, lambda: self.add_number(6))
        self.create_button('7', button_frame, 2, 0, lambda: self.add_number(7))
        self.create_button('8', button_frame, 2, 1, lambda: self.add_number(8))
        self.create_button('9', button_frame, 2, 2, lambda: self.add_number(9))
        self.create_button('0', button_frame, 3, 1, lambda: self.add_number(0))
        self.create_button('+', button_frame, 0, 3, lambda: self.add_operation('+'))
        self.create_button('-', button_frame, 1, 3, lambda: self.add_operation('-'))
        self.create_button('*', button_frame, 2, 3, lambda: self.add_operation('*'))
        self.create_button('/', button_frame, 3, 0, lambda: self.add_operation('/'))
        self.create_button('0', button_frame, 3, 1, lambda: self.add_number(0))
        self.create_button('=', button_frame, 3, 2, self.safe_calculate, self.finish_color)
        self.create_button('C', button_frame, 3, 3, self.clear, self.clear_color)

    def create_button(self, text, frame, row, column, command, bg=None):
        color = bg if bg else self.button_color
        button = tk.Button(frame, text=text, command=command, font=('Arial', 16), width=5, height=2, activebackground="#666",bg=color ,fg = self.text_color, relief = 'flat')
        button.grid(row=row, column=column, padx=8, pady=8)

    def add_number(self, number):
        current = self.result.get()
        current += str(number)
        self.result.delete(0, tk.END)
        self.result.insert(0, current)
        self.error_label.config(text="" , bg = self.bg_color)

    def add_operation(self, operator):
        current = self.result.get()
        current += operator
        self.result.delete(0, tk.END)
        self.result.insert(0, current)
        self.error_label.config(text="", bg = self.bg_color)

    def safe_calculate(self):
        try:
            current = self.result.get()
            result = eval(current)
            self.result.delete(0, tk.END)
            self.result.insert(0, result)
            self.error_label.config(text="", bg = self.bg_color)
        except Exception as e:
            self.error_label.config(text=f"An erro occured : {e}" , bg = self.error_bg )

    def clear(self):
        self.result.delete(0, tk.END)
        self.error_label.config(text="",bg = self.bg_color) 


if __name__ == '__main__':
    mycal = Calculator()
    mycal.mainloop()