import game.game as game

print(dir(game))
game = game.Game()

while True:
    game.update()