from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.button import Button, Label
from random import randint


class PongPaddle(Widget):
    score = NumericProperty(0)
    orientation = ObjectProperty([0, 0])
    color = ObjectProperty([0,0,0,1])

def bounce_ball(self, ball):
    if self.collide_widget(ball):
        vx, vy = ball.velocity
        ball.color = self.color
        ball.last_hit = int(self.custom_id)
        if self.orientation[0] == 25:                
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
        else:
            offset = (ball.center_x - self.center_x) / (self.width / 2)
            bounced = Vector(vx, -1 * vy)
            vel = bounced * 1.1
            ball.velocity = vel.x + offset, vel.y

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    last_hit = 0
    color = ObjectProperty([0,0,0,1])
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    player3 = ObjectProperty(None)
    player4 = ObjectProperty(None)
    l = Label()
    btn1 = Button(text='Restart')
    win_game = 1

    def start(self):
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def stop(self):
        # Stop updating
        Clock.unschedule(self.update)

    def init(self):
        ## Setup players
        self.player1.orientation = [25, 200]
        self.player1.color = [1,0,0,1]
        self.player1.score = 0
        # Player 2
        self.player2.orientation = [25, 200]
        self.player2.color = [0,1,0,1]
        self.player2.score = 0
        # Player 3
        self.player3.orientation = [200, 25]
        self.player3.color = [0,0,1,1]
        self.player3.score = 0
        # Player 4
        self.player4.orientation = [200, 25]
        self.player4.color = [1,1,0,1]
        self.player4.score = 0

    def serve_ball(self):
        # Ball velocity - Add 2 to avoid 0
        vel = (randint(-8,6)+2, randint(-8,6)+2)

        # Setup ball
        self.ball.center = self.center
        self.ball.velocity = vel
        self.ball.last_hit = 0
        self.ball.color = [1,1,1,1]

    def update(self, dt):
        self.ball.move()

        #Bounce out the of paddles - Why do all check? Only can bounce on one any given time
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        self.player3.bounce_ball(self.ball)
        self.player4.bounce_ball(self.ball)

        #bounce ball off bottom or top - This is for 2 players game
        # if (self.ball.y < self.y) or (self.ball.top > self.top):
        #     self.ball.velocity_y *= -1

        # Went of any side? - Last hitter gets a goal
        if self.ball.x < self.x or self.ball.x > self.width or self.ball.y < self.y or self.ball.y > self.height:
            if self.ball.last_hit == 1:
                self.player1.score += 1
            elif self.ball.last_hit == 2:
                self.player2.score += 1
            elif self.ball.last_hit == 3:
                self.player3.score += 1
            elif self.ball.last_hit == 4:
                self.player4.score += 1
            self.serve_ball()

        if self.player1.score >= self.win_game:
            self.player_win(1)
        elif self.player2.score >= self.win_game:
            self.player_win(2)
        elif self.player3.score >= self.win_game:
            self.player_win(3)
        elif self.player4.score >= self.win_game:
            self.player_win(4)

    def player_win(self, player_int):
        # Remove Ball and players
        self.clear_widgets()
        # Configure Label and Btn
        self.l.text ='Player ' + str(player_int) + ' Wins!!'
        self.l.top = self.top-50
        self.l.font_size = 50
        self.l.center_x = self.width/2
        self.btn1.bind(on_press=self.restart)
        self.btn1.center_x = self.width/2
        self.btn1.top = self.top/2
        self.add_widget(self.l)
        self.add_widget(self.btn1)
        self.stop()


    def on_touch_move(self, touch):
        if touch.x < self.width / 3 and touch.y > self.height / 6 \
            and touch.y < 5 * self.height/6:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3 and touch.y > self.height / 6 \
            and touch.y < 5 * self.height / 6:
            self.player2.center_y = touch.y
        if touch.y < self.height / 3 and touch.x > self.width / 6 \
            and touch.x < 5 * self.width / 6:
            self.player4.center_x = touch.x
        if touch.y > 2* self.height / 3 and touch.x > self.width / 6 \
            and touch.x < 5 * self.width / 6:
            self.player3.center_x = touch.x

    # Method update  layout
    def update_rect(instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def restart(self, instance):
        # Remove btn and labels
        self.clear_widgets()

        # Add what I want
        self.add_widget(self.ball)
        self.add_widget(self.player1)
        self.add_widget(self.player2)
        self.add_widget(self.player3)
        self.add_widget(self.player4)
        self.init()
        self.serve_ball()
        self.start()

class PongApp(App):
    def build(self):
        game = PongGame()
        game.init()
        game.serve_ball()
        game.start()
        return game


if __name__ == '__main__':
    PongApp().run()