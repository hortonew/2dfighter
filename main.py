#!/usr/bin/python
from helpers import *
import pygame
from pygame.locals import *
from math import e, pi, cos, sin, sqrt
from random import uniform
from helpers import pygamehelper
from classes import player, background, gametext

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
		self.background = background.Background()
		self.gametext = gametext.GameText()
		
		#select which character for player one.  start at 1
		self.p1 = self.select_character(1)
		
	def select_character(self, i):
		#list of characters (lists of coordinates and image paths)
		characters = [
			[
				#character 1
				[(0, 0, 22, 27), (24, 0, 24, 27), (50, 0, 24, 27), (78, 0, 21, 27), (104, 0, 19, 27), (125, 0, 22, 27)],
				'sprites/characters/iceman_sprite.png'
			],
			[
				#character 2
				[(0, 0, 22, 27), (24, 0, 24, 27), (50, 0, 24, 27), (78, 0, 21, 27), (104, 0, 19, 27), (125, 0, 22, 27)],
				'sprites/characters/iceman_sprite_red.png'
			]
		]
		coords = characters[i-1][0] # list of coords
		i_path = characters[i-1][1] # image path
		character = player.Player(self.helpers.get_spritesheet(i_path, coords))
		return character

	def update(self):
		#update player's position
		self.p1.update()
    
	def keyUp(self, key):
		self.p1.currentAnim = 0
	
	def keyDown(self, key):
		#reset animation loop
		if self.p1.currentAnim > 1:
			self.p1.currentAnim = 0
		
		#if you press numpad 1 or 2, swap iceman sprites
		if key == K_KP1:
			self.p1 = self.select_character(1)
		elif key == K_KP2:
			self.p1 = self.select_character(2)

		if not self.p1.isDucking:
			if not self.p1.isBlocking:
				if key == K_a:
					#move left
					self.p1.currentAnim += 1
					self.p1.updateSpeed([-self.p1.x_speed, 0], self.p1.currentAnim, 1, 0)
				elif key == K_d:
					#move right
					self.p1.currentAnim += 1
					self.p1.updateSpeed([self.p1.x_speed, 0], self.p1.currentAnim, 0, 0)
				elif key == K_LCTRL or key == K_RCTRL:
					self.p1.shoot()
				elif key == K_LSHIFT:
					#sprint
					self.p1.x_speed = 15
				elif key == K_j:
					self.p1.punch()
					
			if key == K_r:
				#block
				self.p1.block()

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
        
	#Display all text on screen
	def setText(self):
		p1_health = self.gametext.get_text(str(self.p1.health), (255,0,0), (255,255,255), 200, 75, 20)
		self.screen.blit(p1_health[0], p1_health[1])
		for text in self.gametext.textobjects:
			self.screen.blit(text[0], text[1])
	
	#Display all background images
	def setBackground(self):
		self.screen.blit(self.background.top, self.background.top_rect)
		self.screen.blit(self.background.middle, self.background.middle_rect)
        
	def draw(self):
		global groundY
		ground = groundY + 27 # groundY plus height of player sprite
		self.screen.fill((255,255,255)) #clear the screen
		
		self.setBackground() # blit the background images
		self.setText() #write text on screen
		self.screen.blit(self.p1.image, self.p1.rect) #draw player on screen
		#draw the players projectiles:
		for p in self.p1.projectiles:
			pygame.draw.rect(self.screen, p.color, pygame.rect.Rect(p.rect))

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
