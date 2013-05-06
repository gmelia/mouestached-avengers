import pygame
import sys
from preferences import *

# Game
#
# 	This class represents all basic mechanisms of a game such as
#	game loop, loading, etc...
#

class Game :

	# Singleton instance
	_instance = None
	# Pygame screen
	screen = None
	# Current preferences
	prefs = Preferences()
	# Current scene
	currentScene = None
	# Scenes set
	scenes = {}
	# Running loop condition
	RUNNING = False

	# Singleton constructor	
	def __new__(cls):
        	if not cls._instance:
        		# Initialise pygame
			pygame.init()
			# Load preferences
			self.prefs.deserialize("currentPrefs");
            		cls._instance = super(Game, cls).__new__(cls)
        	return cls._instance
		
	# Set current scene as given scene
	def setScene(self, name) :
		self.RUNNING = False
		self.currentScene = self.scenes[name]
		self.run()
		
	# Add scene to scenes set
	def addScene(self, name, scene) :
		self.scenes[name] = scene
		
	# Load current scene
	def load(self) :
		self.currentScene.load()
		
	# Update current scene
	def update(self) :
		self.currentScene.update()
		
	# Render current scene
	def render(self) :
		self.screen.fill((0,0,0))
		self.currentScene.render()
		pygame.display.flip()
	
	# Run game main loop
	def run(self) :
		# Create display
		self.screen = pygame.display.set_mode((self.prefs.value("width"),
							self.prefs.value("height")));
		# Change window title
		pygame.display.set_caption("Le jeu")
		# Load all needed assets		
		self.load()
		# Main loop
		self.RUNNING = True
		while self.RUNNING:
			# Iterate in events
			for event in pygame.event.get():
				# If quit event, exit
		 		if event.type == pygame.QUIT : sys.exit()
		 	
		 	# Get current time
		 	time = pygame.time.get_ticks()
		 	
		 	# Update entities state
		 	self.update()
		 	# Render entities
		 	self.render()
		
			# Get execution time
			execTime = pygame.time.get_ticks() - time
			# Get remaining time
			remTime = (1000.0/60.0) - execTime
			# If time remaining apply delay
			if remTime > 0 :
				pygame.time.delay(int(round(remTime)))
