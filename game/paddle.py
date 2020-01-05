import random
import turtle

class Paddle(turtle.Turtle):
    def __init__(self, initial_x, initial_y, height, width, speed):
        super(Paddle, self).__init__()
        self.setx(initial_x)
        self.sety(initial_y)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=height, stretch_wid=width)
        self.speed(0) # animation speed

        self.movement_speed = speed

        self.penup()
        self.goto(self.xcor(), self.ycor())

    def move_up(self):
        self.sety(self.ycor() + self.movement_speed)
        self.goto(self.xcor(), self.ycor())

    def move_down(self):
        self.sety(self.ycor() - self.movement_speed)
        self.goto(self.xcor(), self.ycor())

    def contains(self, other_object):
        edge_points = self.get_shapepoly()
        height = abs(edge_points[0][0])
        width = abs(edge_points[0][1])

        if (self.xcor() - width <= other_object.xcor() <= self.xcor() + width) and \
           (self.ycor() - height <= other_object.ycor() <= self.ycor() + height):
            return True
        else:
            return False

class AutoPaddle(Paddle):
    def move(self, ball_y, error_rate=10):
        error_score = random.randint(0, error_rate*3)

        if self.ycor() < ball_y and error_score > error_rate:
            self.move_up()
        elif self.ycor() < ball_y and error_score <= error_rate:
            self.move_down()
        elif self.ycor() > ball_y:
            self.move_down()
        else:
            pass