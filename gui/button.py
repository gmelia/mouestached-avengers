# two images have same rect TODO
import pygame

class Button :
	
	# Images
	image = None
	imageHover = None
	# Position
	width = 0
	height = 0
	x = 0
	y = 0
	
	def __init__(self,pathImage,pathImageHover) :
		self.image = pygame.image.load(pathImage)
		self.imageHover = pygame.image.load(pathImageHover)
		self.width = self.image.get_width()
		self.height = self.image.get_height()
	
	def clicked(self) :
		click = pygame.mouse.get_pressed()[0]
		if self.hover() and click :
			return True
			
	def hover(self) :
		mpos = pygame.mouse.get_pos()
		if  mpos[0] > self.x - self.width/2 and mpos[0] < self.x + self.width/2	and mpos[1] > self.y - self.height/2 and mpos[1] < self.y + self.height/2 :
			return True
		
	def draw(self) :
		screen = pygame.display.get_surface()
		surface = self.image
		if self.hover() : surface = self.imageHover
		screen.blit(surface,(self.x-self.width/2,self.y-self.height/2))
	
	def setX(self,x) :
		self.x = x
	
	def setY(self,y) :
		self.y = y
		
	def setPosition(x,y) :
		self.x = x
		self.y = y
	
	
	
