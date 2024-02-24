import tkinter as tk

WHITE = '#FFFFFF'
BLACK = '#000000'
Large_font = ('Arial', 40, 'bold')
Small_font = ('Arial', 16)
Digit_font = ('Aial', 24, 'bold')


class Calculator:
    def __init__ (self):
        self.window = tk.Tk()
        self.window.geometry('375x667')
        self.window.title("Calculator")
        self.window.resizable(0,0)
        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()
        self.current_expression_text = "0"
        self.result_expression_text = "0"
        self.current_label, self.result_label = self.create_labels()
        self.digits = {7:(1,1), 8:(1,2), 9:(1,3),
                       4:(2,1), 5:(2,2), 6:(2,3),
                       1:(3,1), 2:(3,2), 3:(3,3),
                                0:(4,2), ".":(4,3)} 
        self.create_digit_buttons()
        self.operations = {"/" : "\u00F7", "*" : "\u00D7" , "-" : "-", "+" : "+" , }
        self.create_operation_buttons()
        self.create_equal_button()
        self.create_clear_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_delete_button()
        self.button_frame.rowconfigure(0,weight = 1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x,weight = 1)
            self.button_frame.columnconfigure(x, weight = 1)
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221,bg=BLACK)
        frame.pack(expand=True, fill='both')
        return frame
    def create_button_frame(self):
        frame = tk.Frame(self.window, height=446,bg=BLACK)
        frame.pack(expand=True, fill='both')
        return frame
    def create_labels(self):
        current_label = tk.Label(self.display_frame,text = self.current_expression_text, bg = BLACK, foreground = WHITE, font = Small_font, anchor = tk.E , padx = 24)
        current_label.pack(expand= True, fill= 'both')
        result_label = tk.Label(self.display_frame,text = self.result_expression_text, bg = BLACK, foreground = WHITE, font = Large_font, anchor = tk.E , padx = 24)
        result_label.pack(expand = True, fill = 'both')
        return current_label, result_label
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text = str(digit), bg= BLACK, foreground= WHITE, font= Digit_font, command= lambda x = digit : self.add_to_expression(value = x) ) 
            button.grid(row=grid_value[0] , column=grid_value[1], sticky=tk.NSEW)
    def create_operation_buttons(self):
        row = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text = symbol, bg= BLACK, foreground= WHITE, font= Digit_font, command = lambda x = operator : self.add_operation(operator = x) )
            button.grid(row = row, column = 4, sticky=tk.NSEW)
            row += 1
    def create_equal_button(self):
        button = tk.Button(self.button_frame, text = "=", bg= BLACK, foreground= WHITE, font= Digit_font, command = self.equal)
        button.grid(row = 4, column = 4, sticky =tk.NSEW )
    def create_clear_button(self):
        button = tk.Button(self.button_frame, text = "C", bg = BLACK, foreground = WHITE, font= Digit_font, command = self.clear_calculator)
        button.grid(row = 0, column = 1, sticky = tk.NSEW ) 
    def clear_calculator(self):
         self.result_expression_text = "0"
         self.current_expression_text = "0"
         self.update_current_label()
         self.update_result_label()
    def create_square_button(self):
        button = tk.Button(self.button_frame, text = "x\u00b2", bg = BLACK, foreground = WHITE, font= Digit_font, command = self.square)
        button.grid(row = 0, column = 2, sticky = tk.NSEW ) 
    def square(self):
        self.result_expression_text = str(eval(f"{self.result_expression_text}** 2"))
        self.update_result_label()
    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text = "\u221ax", bg = BLACK, foreground = WHITE, font= Digit_font, command = self.sqrt)
        button.grid(row = 0, column = 3, sticky = tk.NSEW ) 
    def sqrt(self):
        self.result_expression_text = str(eval(f"{self.result_expression_text}** (1/2)"))
        self.update_result_label()
    def create_delete_button(self):
        button = tk.Button(self.button_frame, text = "<=", bg = BLACK, foreground = WHITE, font= Digit_font, command = self.delete)
        button.grid(row = 4, column = 1, sticky = tk.NSEW ) 
    def delete(self):
        self.result_expression_text = self.result_expression_text[:-1]
        self.update_result_label()
    def add_to_expression(self, value):
        if self.result_expression_text == "0":
            self.result_expression_text = str(value)
        else:
            self.result_expression_text += str(value) 
        self.update_result_label() 
    def add_operation(self, operator):
        if self.current_expression_text == "0":
            self.current_expression_text = self.result_expression_text + operator
        else:
            self.current_expression_text += self.result_expression_text + operator
        self.update_current_label()
        self.result_expression_text = "0"
    def equal(self):
        self.current_expression_text += self.result_expression_text
        self.result_expression_text = eval(self.current_expression_text)
        self.result_expression_text = str(self.result_expression_text) 
        self.update_result_label()
        self.update_current_label()
    def update_result_label(self):
        self.result_label.config(text = self.result_expression_text)
    def update_current_label(self):
        self.current_label.config(text = self.current_expression_text)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    cal = Calculator()
    cal.run()
       