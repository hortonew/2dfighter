#!/usr/bin/python
from helpers import *
import pygame
from pygame.locals import *
from math import e, pi, cos, sin, sqrt
from random import uniform
from helpers import pygamehelper
from classes import player

global groundY
groundY = 300
WINDOW_SIZE = (800, 600)


class Game:
	def __init__(self):
		self.running = False
		self.clock = pygame.time.Clock() #to track FPS
		pygame.init()
		self.screen = pygame.display.set_mode(WINDOW_SIZE)
		self.screen.fill((255,255,255))
		pygame.display.flip()
		self.fps= 0
		self.w, self.h = WINDOW_SIZE[0], WINDOW_SIZE[1]
		helpers = pygamehelper.PygameHelper()

		#coordinates on sprite sheet for each image
		p1_coords = [(0, 0, 22, 27), (24, 0, 24, 27), (50, 0, 24, 27), (78, 0, 21, 27), (104, 0, 19, 27)]
		self.p1 = player.Player(helpers.get_spritesheet('../images/iceman_sprite.png', p1_coords))

	def update(self):
		#update player's position
		self.p1.update()
		pass
    
	def keyUp(self, key):
		#check if any key was released, but only set movement to false if no other movement key is pressed down

		#update speed how to
		#[speed], SpriteImage, 1 if x flip, 1 if y flip

		#normal speed 
		if key == K_LSHIFT:
			self.p1.x_speed = self.p1.starting_x_speed
		elif key == K_s:
			#stand up
			self.p1.speed = [0,0]
			self.p1.updateSpeed([0, 0], -1, 0, 0)
		elif key == K_r:
			#block
			self.p1.speed = [0,0]
			self.p1.updateSpeed([0, 0], -1, 0, 0)
	
	def keyDown(self, key):
		#update speed how to
		#[speed], SpriteImage, 1 if x flip, 1 if y flip
		if key == K_s:
			#move down
			self.p1.speed = [0,0]
			self.p1.updateSpeed([0, 0], 3, 0, 0)
		elif key == K_w:
			#move up
			pass
		elif key == K_a:
			#move left
			self.p1.updateSpeed([-self.p1.x_speed, 0], 0, 1, 0)
		elif key == K_d:
			#move right
			self.p1.updateSpeed([self.p1.x_speed, 0], 0, 0, 0)
		elif key == K_SPACE:
			#jump
			if self.p1.isJumping != True:
				self.p1.vSpeed = -self.p1.jumpForce
				self.p1.isJumping = True
		elif key == K_LSHIFT:
			#sprint
			self.p1.x_speed = 15
		elif key == K_r:
			#block
			self.p1.speed = [0,0]
			self.p1.updateSpeed([0, 0], 4, 0, 0)
            
	def mouseUp(self, button, pos):
		pass

	def mouseMotion(self, buttons, pos, rel):
		pass
        
	#create and display all font on screen
	def setText(self):
		font = pygame.font.Font(None, 36)
		font2 = pygame.font.Font(None, 20)
		self.text1 = font.render('Controls', True, (0,0,0), (255,255,255))
		self.text2 = font2.render('SPACE - Jump', True, (0,0,0), (255,255,255))
		self.text3 = font2.render('SHIFT - Sprint', True, (0,0,0), (255,255,255))
		self.text4 = font2.render('WASD - Move', True, (0,0,0), (255,255,255))

		self.text1Rect = self.text1.get_rect()
		self.text1Rect.centerx = self.w - 200
		self.text1Rect.centery = 50

		self.text2Rect = self.text2.get_rect()
		self.text2Rect.centerx = self.w - 200
		self.text2Rect.centery = 75

		self.text3Rect = self.text3.get_rect()
		self.text3Rect.centerx = self.w - 200
		self.text3Rect.centery = 95

		self.text4Rect = self.text4.get_rect()
		self.text4Rect.centerx = self.w - 200
		self.text4Rect.centery = 115

		self.screen.blit(self.text1, self.text1Rect)
		self.screen.blit(self.text2, self.text2Rect)
		self.screen.blit(self.text3, self.text3Rect)
		self.screen.blit(self.text4, self.text4Rect)

    
        
	def draw(self):
		#clear the screen
		self.screen.fill((255,255,255))


		#write text on screen
		self.setText()

		#draw player on screen
		self.screen.blit(self.p1.image, self.p1.rect)
		pygame.draw.line(self.screen, (0,0,0), (000, 328), (800, 328))

	def handleEvents(self):
		keys = pygame.key.get_pressed()  #checking pressed keys
		#if keys[K_w]:
		#self.keyDown(K_w)
		#if keys[K_s]:
		#self.keyDown(K_s)
		if keys[K_a]:
			self.keyDown(K_a)
		elif keys[K_d]:
			self.keyDown(K_d)
		elif keys[K_LSHIFT]:
			self.keyDown(K_LSHIFT)
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False
			elif event.type == KEYDOWN:
				self.keyDown(event.key)
			elif event.type == KEYUP:
				if event.key == K_ESCAPE:
					self.running = False
				self.keyUp(event.key)
			elif event.type == MOUSEBUTTONUP:
				self.mouseUp(event.button, event.pos)
			elif event.type == MOUSEMOTION:
				self.mouseMotion(event.buttons, event.pos, event.rel)

	def mainLoop(self, fps=0):
		self.running = True
		self.fps= fps

		while self.running:
			pygame.display.set_caption("FPS: %i" % self.clock.get_fps())
			self.handleEvents()
			self.update()
			self.draw()
			pygame.display.flip()
			self.clock.tick(self.fps)

g = Game()
g.mainLoop(30)
