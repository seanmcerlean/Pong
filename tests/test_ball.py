import random
import ball


def test_constructor():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    speed = random.randint(-100, 100)
    test_ball = ball.Ball(x, y, speed)

    assert test_ball.xcor() == x
    assert test_ball.ycor() == y
    assert test_ball.x_speed == speed or test_ball.x_speed == -speed
    assert test_ball.y_speed == speed or test_ball.y_speed == -speed
    assert test_ball.shape() == 'square'
    assert test_ball.color() == ('white', 'white')
    assert test_ball.out_of_bounds_left == 0
    assert test_ball.out_of_bounds_right == 0


def test_move():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    speed = random.randint(-100, 100)
    test_ball = ball.Ball(x, y, speed)

    test_ball.move()
    assert test_ball.xcor() == x + test_ball.x_speed
    assert test_ball.ycor() == y + test_ball.y_speed


def test_reset_speed_with_a_positive_speed():
    test_ball = ball.Ball(0, 0, 1)
    test_ball.x_speed = 2
    test_ball.y_speed = 3

    test_ball.reset_speed()
    assert test_ball.x_speed == -1
    assert test_ball.y_speed == -1


def test_reset_speed_with_a_negative_speed():
    test_ball = ball.Ball(0, 0, 1)
    test_ball.x_speed = -4
    test_ball.y_speed = -5

    test_ball.reset_speed()
    assert test_ball.x_speed == 1
    assert test_ball.y_speed == 1
