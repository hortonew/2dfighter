#!/usr/bin/python
from helpers import *
import pygame
from pygame.locals import *
from math import e, pi, cos, sin, sqrt
from random import uniform
from helpers import pygamehelper
from classes import player

WINDOW_SIZE = (800, 600)
groundY = 300

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
		self.helpers = pygamehelper.PygameHelper()
		
		#select which character for player one.  start at 1
		self.p1 = self.select_character(1)
		
	def select_character(self, i):
		#list of characters (lists of coordinates and image paths)
		characters = [
			[
				#character 1
				[(0, 0, 22, 27), (24, 0, 24, 27), (50, 0, 24, 27), (78, 0, 21, 27), (104, 0, 19, 27)],
				'sprites/characters/iceman_sprite.png'
			]
		]
		coords = characters[i-1][0] # list of coords
		i_path = characters[i-1][1] # image path
		character = player.Player(self.helpers.get_spritesheet(i_path, coords))
		return character

	def update(self):
		#update player's position
		self.p1.update()
		pass
    
	def keyUp(self, key):
		#check if any key was released, but only set movement to false if no other movement key is pressed down

		#update speed how to
		#[speed], SpriteImage, 1 if x flip, 1 if y flip
		if not self.p1.isBlocking:
			if key == K_s:
				#stand up
				self.p1.isDucking = False
				self.p1.updateSpeed([0, 0], -1, 0, 0)
		if not self.p1.isDucking:
			if key == K_LSHIFT:
				#normal speed 
				self.p1.x_speed = self.p1.starting_x_speed
			elif key == K_r:
				#block
				self.p1.isBlocking = False
				self.p1.updateSpeed([0, 0], -1, 0, 0)
	
	def keyDown(self, key):
		#update speed how to
		#[speed], SpriteImage, 1 if x flip, 1 if y flip
		if not self.p1.isDucking:
			if not self.p1.isBlocking:
				if key == K_a:
					#move left
					self.p1.updateSpeed([-self.p1.x_speed, 0], 0, 1, 0)
				elif key == K_d:
					#move right
					self.p1.updateSpeed([self.p1.x_speed, 0], 0, 0, 0)
				elif key == K_LSHIFT:
					#sprint
					self.p1.x_speed = 15
			if key == K_r:
				#block
				self.p1.isBlocking = True
				self.p1.updateSpeed([0, 0], 4, 0, 0)
		if not self.p1.isBlocking:
			if key == K_s:
				#duck
				self.p1.isDucking = True
				self.p1.updateSpeed([0, 0], 3, 0, 0)
			elif key == K_SPACE:
				#jump
				if self.p1.isJumping != True:
					self.p1.vSpeed = -self.p1.jumpForce
					self.p1.isJumping = True
            
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
		global groundY
		ground = groundY + 27 # groundY plus height of player sprite
		self.screen.fill((255,255,255)) #clear the screen
		self.setText() #write text on screen
		self.screen.blit(self.p1.image, self.p1.rect) #draw player on screen
		pygame.draw.line(self.screen, (0,0,0), (000, ground), (800, ground)) #draw line for ground

	def handleEvents(self):
		keys = pygame.key.get_pressed()  #checking pressed keys
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