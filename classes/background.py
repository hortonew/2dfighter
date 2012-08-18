import pygame
import os

class Background:
	def __init__(self):
		#background images
		self.top = self.createImage('../images/backgrounds/starfield.png')
		self.top_rect = self.top.get_rect().move([0, 0])
		self.middle = self.createImage('../images/backgrounds/city.png')
		self.middle_rect = self.middle.get_rect().move([0, 200])
		
	def createImage(self, ipath):
		mypath = os.path.dirname( os.path.realpath( __file__) )
		return pygame.image.load( os.path.join(mypath, ipath) ).convert_alpha()
		
	def changeBackground(self, i):
		if i == 1:
			top = '../images/backgrounds/starfield.png'
			top_rect = [0, 0]
			middle = '../images/backgrounds/city.png'
			middle_rect = [0, 200]
			
		self.top = createImage(top)
		self.top_rect = self.top.get_rect().move([0, 0])
		self.middle = createImage(middle)
		self.middle_rect = self.middle.get_rect().move([0, 200])