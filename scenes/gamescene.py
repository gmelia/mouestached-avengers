import pygame

class GameScene :

	def load(self) :
		print "LOADING GAME SCENE"
	
	def update(self) :
		print ""
	
	def render(self) :
		print "RENDER GAME SCENE"
		pygame.display.get_surface().fill((150,100,100));
