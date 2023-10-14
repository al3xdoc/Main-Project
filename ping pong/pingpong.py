from tkinter import*
import time, random
class Ball :
    'This is a ball(?)'
    def __init__(self, canvas, color, paddle ): 
          self.canvas = canvas
          self.id = canvas.create_oval((0, 0, 30, 30), fill = color )
          self.canvas.move(self.id, 250, 250)
          speed = [-2, -1, 1, 2]
          self.x = random.choice(speed)
          self.y = random.choice(speed)
          self.paddle = paddle
          self.score = 0
    def draw(self):
          self.canvas.move(self.id, self.x , self.y)
          pos = self.canvas.coords(self.id)
          print(pos)
          if pos[0] <= 0:
              self.x*= -1
          elif pos[2] >= 600:
              self.x*= -1
          elif pos[1] <= 0:
              self.y*= -1
          elif pos[3] >= 500:
              self.y*= -1
    def bounce(self,pos):
         paddle_pos = self.canvas.coords(self.paddle.id)
         print(pos , paddle_pos)
         if (pos[3] >= paddle_pos[1]) and (pos[0] >= paddle_pos[0]) and (pos[2] <= paddle_pos[2]) and (pos[1] <= paddle_pos[3]): 
              self.y*= -1
              self.score += 1

class Paddle :  
     '!!'
     def __init__(self, canvas, color ):
          self.canvas = canvas
          self.id = canvas.create_rectangle((0,0,100,25), fill=color)
          self.canvas.move(self.id, 250, 400)
          self.x = 0
          self.canvas.bind_all('<Right>', self.right)
          self.canvas.bind_all('<Left>', self.left)
     def move(self):
          self.canvas.move(self.id , self.x , 0)
          puddle_pos = self.canvas.coords(self.id)
          if puddle_pos[0] <= 0:
               self.x*= -1
          elif puddle_pos[2] >= 600:
               self.x*= -1
     def right(self , event):
          self.x = 2
     def left(self, event):
          self.x = -2


root = Tk()
root.title('ping pong')
root.resizable(0,0)
root.wm_attributes("-topmost", 1)

label_name = Label( foreground = 'red', text = "Pingpong", font = ("Arial", 25))
label_name.pack()

paper = Canvas(bg = 'white', height = 500, width = 600)
paper.pack()

rocket = Paddle(paper, color = 'black')

ball = Ball(paper, color = 'red', paddle = rocket)

label_score = Label(bg = 'white', foreground = 'red', text = ball.score, font = ("Arial", 35,))
label_score.pack()

# list of speed (-2 <-> 2)

while True:
     ball.draw()
     rocket.move()
     ball.bounce(pos = ball.canvas.coords(ball.id))
     label_score.configure(text = ball.score)
     root.update_idletasks()
     root.update()
     time.sleep(0.01)
    

