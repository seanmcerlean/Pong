import time

import ball
import paddle
import game


def test_sixty_fps_decorator():
    def test_func():
        pass

    start_time = time.time_ns()
    game.sixty_fps(test_func)()
    end_time = time.time_ns()
    one_sixtyth_second_in_ns = 16666666
    assert start_time + one_sixtyth_second_in_ns < end_time


def test_constructor():
    new_game = game.Game((800, 600))

    assert new_game.left_edge == -400
    assert new_game.right_edge == 400
    assert new_game.top_edge == 300
    assert new_game.bottom_edge == -300.0

    assert new_game.paddle_1.xcor() == -350
    assert new_game.paddle_1.ycor() == 0
    assert new_game.paddle_1.movement_speed == 20
    assert str(type(new_game.paddle_1)) == "<class 'paddle.Paddle'>"
    assert new_game.paddle_2.xcor() == 350
    assert new_game.paddle_2.ycor() == 0
    assert new_game.paddle_2.movement_speed == 20
    assert str(type(new_game.paddle_2)) == "<class 'paddle.AutoPaddle'>"

    assert new_game.ball.xcor() == 0
    assert new_game.ball.ycor() == 0
    assert new_game.ball.x_speed == 5 or new_game.ball.x_speed == -5
    assert new_game.ball.y_speed == 5 or new_game.ball.y_speed == -5

    assert new_game.score.xcor() == 0
    assert new_game.score.ycor() == 250


def test_ball_hit_top():
    new_game = game.Game((800, 600))
    test_ball = ball.Ball(50, 325, 1)

    new_game.ball = test_ball
    old_speed = test_ball.y_speed
    new_game.check_collisions()
    assert new_game.ball.ycor() == 300
    assert new_game.ball.y_speed == old_speed * -1


def test_ball_hit_bottom():
    new_game = game.Game((800, 600))
    test_ball = ball.Ball(50, -325, -1)
    old_speed = test_ball.y_speed

    new_game.ball = test_ball
    new_game.check_collisions()
    assert new_game.ball.ycor() == -300
    assert new_game.ball.y_speed == old_speed * -1


def test_paddle_1_move():
    new_game = game.Game((800, 600))
    test_paddle = paddle.Paddle(100, 201, 10, 10, 1)

    new_game.paddle_1 = test_paddle
    new_game.check_collisions()
    assert new_game.ball.xcor() == 202


def test_paddle_1_hit_top():
    new_game = game.Game((800, 600))
    test_paddle = paddle.Paddle(100, 301, 10, 10, 1)

    new_game.paddle_1 = test_paddle
    new_game.check_collisions()
    assert new_game.ball.xcor() == 300


def test_paddle_1_hit_bottom():
    new_game = game.Game((800, 600))
    test_paddle = paddle.Paddle(100, -301, 10, 10, 1)

    new_game.paddle_1 = test_paddle
    new_game.check_collisions()
    assert new_game.ball.xcor() == -300


def test_paddle_2_move():
    new_game = game.Game((800, 600))
    test_paddle = paddle.Paddle(-100, 201, 10, 10, 1)

    new_game.paddle_2 = test_paddle
    new_game.check_collisions()
    assert new_game.ball.xcor() == 202


def test_paddle_2_hit_top():
    new_game = game.Game((800, 600))
    test_paddle = paddle.Paddle(100, 301, 10, 10, 1)

    new_game.paddle_2 = test_paddle
    new_game.check_collisions()
    assert new_game.ball.xcor() == 300


def test_paddle_2_hit_bottom():
    new_game = game.Game((800, 600))
    test_paddle = paddle.Paddle(100, -301, 10, 10, 1)

    new_game.paddle_2 = test_paddle
    new_game.check_collisions()
    assert new_game.ball.xcor() == -300


def test_paddle_1_hit_ball():
    new_game = game.Game((800, 600))
    test_paddle = paddle.Paddle(100, 100, 10, 10, 1)
    test_ball = ball.Ball(101, 101, 1)

    new_game.paddle_1 = test_paddle
    new_game.ball = test_ball

    new_game.check_collisions()

    assert new_game.ball.x_speed == 1.05


def test_paddle_2_hit_ball():
    new_game = game.Game((800, 600))
    test_paddle = paddle.Paddle(-100, -100, 10, 10, 1)
    test_ball = ball.Ball(-99, -99, 1)

    new_game.paddle_2 = test_paddle
    new_game.ball = test_ball

    new_game.check_collisions()

    assert new_game.ball.x_speed == 1.05


def test_player1_score():
    new_game = game.Game((800, 600))
    test_ball = ball.Ball(499, -99, 1)

    new_game.ball = test_ball
    new_game.check_collisions()
    assert new_game.ball.xcor() == 0
    assert new_game.ball.ycor() == 0
    # can't be bothered creating a function to avoid private variables
    assert new_game.score._player1_score == 1
    assert new_game.score._player2_score == 0


def test_player2_score():
    new_game = game.Game((800, 600))
    test_ball = ball.Ball(-499, -99, 1)

    new_game.ball = test_ball
    new_game.check_collisions()
    assert new_game.ball.xcor() == 0
    assert new_game.ball.ycor() == 0
    # can't be bothered creating a function to avoid private variables
    assert new_game.score._player1_score == 0
    assert new_game.score._player2_score == 1
