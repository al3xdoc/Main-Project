import tkinter as tk

WHITE = '#FFFFFF'
BLACK = '#000000'

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
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221,bg='red')
        frame.pack(expand=True, fill='both')
        return frame
    def create_button_frame(self):
        frame = tk.Frame(self.window, height=446,bg='blue')
        frame.pack(expand=True, fill='both')
        return frame

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    cal = Calculator()
    cal.run()
