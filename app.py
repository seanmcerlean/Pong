import game

print(dir(game))
game = game.Game()

while not game.score.has_won(game.winning_score):
    game.update()
