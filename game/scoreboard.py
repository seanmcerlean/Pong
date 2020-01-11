import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self, xcor, ycor):
        super(ScoreBoard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(xcor, ycor)

        self._player1_score = 0
        self._player2_score = 0
        self.write_score_text()

    def add_player1_score(self):
        self._player1_score = self._player1_score + 1

    def add_player2_score(self):
        self._player2_score = self._player2_score + 1

    def write_score_text(self):
        self.clear()
        self.write(f'{self._player1_score} : {self._player2_score}', align='center', font='Courier')

    def has_won(self, winning_score):
        return self._player1_score == winning_score or self._player2_score == winning_score