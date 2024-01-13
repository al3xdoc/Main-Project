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
            button = tk.Button(self.button_frame, text = str(digit), bg= BLACK, foreground= WHITE, font= Digit_font) 
            button.grid(row=grid_value[0] , column=grid_value[1], sticky=tk.NSEW)
    def create_operation_buttons(self):
        row = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text = symbol, bg= BLACK, foreground= WHITE, font= Digit_font)
            button.grid(row = row, column = 4, sticky=tk.NSEW)
            row += 1
    def create_equal_button(self):
        button = tk.Button(self.button_frame, text = "=", bg= BLACK, foreground= WHITE, font= Digit_font)
        button.grid(row = 4, column = 4, sticky =tk.NSEW )
    def add_to_expression(self, value):
        self.result_expression_text += str(value) 
        self.update_result_label() #create a method that update current label  
    def update_result_label(self):
        self.result_label.config(text = self.result_expression_text)


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    cal = Calculator()
    cal.run()

 