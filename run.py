from Env.Env import connect4Env


game = connect4Env()
obs = game.reset()

game.step(0)
game.step(0)
print(game.render())
game.step(1)
game.step(2)
game.step(6)
game.step(6)
game.step(6)
print(game.render())