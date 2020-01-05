import random
import turtle

class Ball(turtle.Turtle):
    def __init__(self, initial_x, initial_y, speed):
        super(Ball, self).__init__()

        self.setx(initial_x)
        self.sety(initial_y)
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(self.xcor(), self.ycor())

        self.out_of_bounds_left = 0
        self.out_of_bounds_right = 0

        self.base_speed = speed
        self.x_speed = random.choice((speed, -speed))
        self.y_speed = random.choice((speed, -speed))

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def reset_speed(self):
        reverse_sign = lambda x: (1, -1)[x > 0]

        self.x_speed = self.base_speed * reverse_sign(self.x_speed)
        self.y_speed = self.base_speed * reverse_sign(self.y_speed)