from .ball import Ball
from .paddle import AutoPaddle, Paddle
from .scoreboard import ScoreBoard

import pathlib
import playsound
import turtle
import time


def sixty_fps(func):
    """Wrapper to ensure function cannot be called more than 60 times per second"""
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        time.sleep(1/60)
    return wrapper

class Game(turtle.Turtle):
    def __init__(self, resolution=(800, 600)):
        self._window = turtle.Screen()
        self._window.title('Pong')
        self._window.bgcolor('black')
        self._window.setup(width=resolution[0], height=resolution[1])
        self._window.tracer(0)

        self.left_edge = -resolution[0] / 2
        self.right_edge = resolution[0] / 2
        self.top_edge = resolution[1] / 2
        self.bottom_edge = -resolution[1] / 2

        self.paddle_1 = Paddle(self.left_edge+50, 0, 1, 6, 20)
        self.paddle_2 = AutoPaddle(self.right_edge-50, 0, 1, 6, 20)

        self.ball = Ball(0, 0, 5)

        self.score = ScoreBoard(0, self.top_edge - 50)

        self._window.listen()
        self._window.onkeypress(self.paddle_1.move_up, 'Up')
        self._window.onkeypress(self.paddle_1.move_down, 'Down')

    def _check_y_edge(self, game_object):
        if game_object.ycor() >= self.top_edge:
            game_object.sety(self.top_edge)
            try:
                game_object.y_speed = game_object.y_speed * - 1
            except AttributeError:
                pass
        elif game_object.ycor() <= self.bottom_edge:
            game_object.sety(self.bottom_edge)
            try:
                game_object.y_speed = game_object.y_speed * - 1
            except AttributeError:
                pass

    def _check_score(self):
        if (self.ball.xcor() <= self.left_edge):
            self.score.add_player2_score()
            self.ball.home()
            self.ball.reset_speed()
        elif (self.ball.xcor() >= self.right_edge):
            self.score.add_player1_score()
            self.ball.home()
            self.ball.reset_speed()

    def _check_paddle_hit(self, paddle, ball):
        if (paddle.contains(ball)):
            ball.x_speed = ball.x_speed * -1.05
            playsound.playsound(str(pathlib.Path(__file__).parent / 'pong.mp3'))

    def check_collisons(self):
        self._check_y_edge(self.paddle_1)
        self._check_y_edge(self.paddle_2)
        self._check_y_edge(self.ball)

        self._check_paddle_hit(self.paddle_1, self.ball)
        self._check_paddle_hit(self.paddle_2, self.ball)

        self._check_score()

    @sixty_fps
    def update(self):
        now = time.time_ns()
        self.ball.move()
        self.paddle_2.move(self.ball.ycor())
        self.check_collisons()
        self.score.write_score_text()
        self._window.update()

