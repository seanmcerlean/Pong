import random
import paddle
import ball


def test_constructor():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    height = random.randint(10, 20)
    width = random.randint(50, 75)
    speed = random.randint(-100, 100)
    test_paddle = paddle.Paddle(x, y, height, width, speed)
    assert test_paddle.xcor() == x
    assert test_paddle.ycor() == y
    assert test_paddle.movement_speed == speed
    assert test_paddle.shapesize() == (width, height, 1)
    assert test_paddle.shape() == 'square'
    assert test_paddle.color() == ('white', 'white')


def test_move_up():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    height = random.randint(10, 20)
    width = random.randint(50, 75)
    speed = random.randint(-100, 100)
    test_paddle = paddle.Paddle(x, y, height, width, speed)

    test_paddle.move_up()
    assert test_paddle.xcor() == x
    assert test_paddle.ycor() == y + test_paddle.movement_speed


def test_move_down():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    height = random.randint(10, 20)
    width = random.randint(50, 75)
    speed = random.randint(-100, 100)
    test_paddle = paddle.Paddle(x, y, height, width, speed)

    test_paddle.move_down()
    assert test_paddle.xcor() == x
    assert test_paddle.ycor() == y - test_paddle.movement_speed


def test_paddle_contains_ball():
    test_paddle = paddle.Paddle(100, 100, 10, 10, 1)
    test_ball = ball.Ball(101, 101, 1)
    assert test_paddle.contains(test_ball)


def test_paddle_does_not_contain_ball():
    test_paddle = paddle.Paddle(100, 100, 10, 10, 1)
    test_ball = ball.Ball(51, 51, 1)
    assert test_paddle.contains(test_ball)


def test_autopaddle_moves_down_with_no_error():
    test_autopaddle = paddle.AutoPaddle(10, 10, 10, 10, 1)
    for i in range(10):
        test_autopaddle.move(0, 10)
    assert test_autopaddle.ycor() == 0


def test_autopaddle_move_up_but_has_errors():
    test_autopaddle = paddle.AutoPaddle(10, 10, 10, 10, 1)
    # Random function so autopaddle sometimes makes mistakes - so shouldn't make it all the way to the expected position
    for i in range(10):
        test_autopaddle.move(20, 10)
    assert 10 < test_autopaddle.ycor() < 20
