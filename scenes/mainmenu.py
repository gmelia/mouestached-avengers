import pygame
import sys
from preferences import *
from gui.button import *
from game import *

import os

class MainMenu :

	screen = None
	buttonPlay = None
	buttonSettings = None
	buttonQuit = None

	def load(self) :
		self.screen = pygame.display.get_surface()
		self.buttonPlay = Button("assets/button.png", "assets/buttonHover.png")
		self.buttonSettings = Button("assets/button.png", "assets/buttonHover.png")
		self.buttonQuit = Button("assets/button.png", "assets/buttonHover.png")
		
	def update(self) :
		if self.buttonPlay.clicked() :
			game = Game()
			game.setScene("gamescene")
		elif self.buttonSettings.clicked() :
			print "CLICK SETTINGS"
		elif self.buttonQuit.clicked() :
			sys.exit()
	
	def render(self) :
		print "RENDER MAIN MENU"
		# Fill screen in black
		self.screen.fill((100,150,100))
		# Move button play
		self.buttonPlay.setX(self.screen.get_width()/2)
		self.buttonPlay.setY(self.screen.get_height()/4)
		# Move button settings
		self.buttonSettings.setX(self.screen.get_width()/2)
		self.buttonSettings.setY(self.screen.get_height()/2)
		# Move button settings
		self.buttonQuit.setX(self.screen.get_width()/2)
		self.buttonQuit.setY(self.screen.get_height()-self.screen.get_height()/4)
		# Draw buttons
		self.buttonPlay.draw()
		self.buttonSettings.draw()
		self.buttonQuit.draw()
