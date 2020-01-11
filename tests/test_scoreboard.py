import random
import scoreboard


def test_constructor():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    test_scoreboard = scoreboard.ScoreBoard(x, y)

    assert test_scoreboard.xcor() == x
    assert test_scoreboard.ycor() == y
    assert test_scoreboard.color() == ('white', 'white')
    assert test_scoreboard._player1_score == 0
    assert test_scoreboard._player2_score == 0


def test_add_player_1_score():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    test_scoreboard = scoreboard.ScoreBoard(x, y)

    test_scoreboard.add_player1_score()
    assert test_scoreboard._player1_score == 1


def test_add_player_2_score():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    test_scoreboard = scoreboard.ScoreBoard(x, y)

    test_scoreboard.add_player2_score()
    assert test_scoreboard._player2_score == 1
