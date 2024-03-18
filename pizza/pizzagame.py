import tkinter as tk

WHITE = '#FFFFFF' #make new colours (red and golden)
BLACK = '#000000'
GOLD = '#ffd966'
RED = '#841818'
Large_font = ('Arial', 40, 'bold')
Small_font = ('Arial', 16)
Digit_font = ('Arial', 20, 'bold')


class Pizza:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('800x600')
        self.window.title("Mini-Pizzaria")
        self.window.iconbitmap("C:\\Users\\malak\\OneDrive\\Рабочий стол\\Project\\pizza\\pizza.ico")
        self.order_text = "Current order"
        self.current_order_label = self.create_order_label()
        self.canvas = self.create_canvas()
        self.button_text = {"Add Sauce":(1,0) , "Add Pepperoni":(2,0), "Add Mushrooms" : (3,0), "Add Cheese" : (4,0),
                            "Add Chiken" : (1,3), "Add Sausage" : (2,3)}
        self.create_buttons()
        self.create_bake_button()
    def create_order_label(self):
        current_order = tk.Label(self.window, text = self.order_text, bg = GOLD, foreground = RED, font = Large_font )
        current_order.grid(row = 0 , column = 0, sticky=tk.NSEW, columnspan = 4)
        return current_order
    def create_canvas(self):
        canvas = tk.Canvas (self.window, bg = WHITE)
        canvas.grid(row = 1, column = 1, sticky=tk.NSEW, columnspan = 2, rowspan = 4)
        return canvas
    def create_buttons(self):
        for text, grid_value in self.button_text.items():
            button = tk.Button(self.window, text = text, font =  Small_font)
            button.grid(row=grid_value[0] , column=grid_value[1], sticky=tk.NSEW)
    def create_bake_button(self):
        button = tk.Button(self.window, text = "Bake!", font = Digit_font )
        button.grid(row = 3, column = 3, sticky = tk.NSEW, rowspan = 2)
#  *bg
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    pizza = Pizza()
    pizza.run()
    
    #make labels and buttons take upp all the sapce (and canvas too)