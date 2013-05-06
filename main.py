from game import *
from scenes.mainmenu import *
from scenes.gamescene import *

game = Game()
menu = MainMenu()
gamescene = GameScene()

game.addScene("menu",menu)
game.addScene("gamescene",gamescene)

game.setScene("menu")

game.run()
