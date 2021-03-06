import pygame
import projectile
gravity = 1.3
groundY = 300
WINDOW_SIZE = (800, 600)
PUNCHING_IMAGE = 5
class Player(pygame.sprite.Sprite):
	def __init__(self, images):
		pygame.sprite.Sprite.__init__(self)
		
		#running animation sprite
		self.currentAnim = 0
		
		self.images = images
		self.image = self.images[self.currentAnim]
		self.rect = self.image.get_rect().move([200, 300])

		#an array to be filled with player's projectiles
		self.projectiles = []
		
		#controls how fast to the right and left the player can move.
		#starting_x_speed allows the x_speed to return to normal after sprinting
		self.starting_x_speed = 9
		self.x_speed = 9
		
		#controls which way the player is looking
		self.direction = 1
		
		#current speed of player
		self.speed = [0, 0]
		
		self.isJumping = False
		self.isDucking = False
		self.isBlocking = False
		
		#stats
		self.health = 100
		
		#acceleration of player in upward direction
		self.vSpeed = 0
		
		#max acceleration in upward direction
		self.maxVSpeed = 3
		
		#controls what the starting vSpeed gets set to when jump is pressed
		self.jumpForce = 11
		
		#starting y value of player (ground)
		self.y = 300
		
	def updateSpeed(self, spd, i, x, y):
		#return to previous state (usually after a jump, or possibly attack)
		if self.speed[0] < 0:
			self.direction = -1
		else:
			self.direction = 1
		#return to normal
		if i == -1:
			if self.direction == 1:
				self.image = self.images[1]
			else:
				self.image = pygame.transform.flip(self.images[1], 1, 0)
		else:
			if x == 0:
				#set sprite image to image in spritesheet
				self.image = self.images[i]
			else:
				#set sprite image to image in spritesheet
				#flip image on x axis
				self.image = pygame.transform.flip(self.images[i], 1, 0)
				
		if spd[0] != 0:
			self.speed[0] = spd[0]
		if spd[1] != 0:
			self.speed[1] = spd[1]
		
		#move the player
		if spd != [0,0]:
			self.rect = self.rect.move(self.speed)

	def do_animation(self, index):
		self.currentAnim = index
		self.image = self.images[self.currentAnim]
		if self.direction == -1:
			self.image = pygame.transform.flip(self.images[self.currentAnim], 1, 0)

	def punch(self):
		self.do_animation(5)
		#put any life/damage/etc code here

	def shoot(self):
		self.projectiles.append(
		projectile.Projectile(
			affected_by_gravity=False,
			x=self.rect.x,
			y=self.rect.y,
			direction=self.direction,
			rect=pygame.rect.Rect(
				self.rect.x,
				self.rect.y,10,10
			)
		))

	def block(self):
		self.do_animation(4)
		#put any life/damage/etc code here

	def duck(self):
		self.do_animation(3)
		
	def jump(self):
		global gravity
		global groundY
		self.vSpeed += gravity
		
		#don't let the vertical speed surpass the maxVerticalSpeed
		if self.vSpeed > self.maxVSpeed:
			self.vSpeed = self.maxVSpeed
		self.y += self.vSpeed #increase the players height by the current vertical speed
		
		#don't let the player move below the ground
		if self.y >= groundY:
			self.vSpeed = 0
			self.y = self.rect[1] = groundY
			self.isJumping = False

		#move player up or down depending on the point of the <jum></jum>p
		self.rect = self.rect.move(0, self.vSpeed)

	def update(self):
		#update the projectiles of this player:
		purge = []
		for i, p in enumerate(self.projectiles):
			p.update()	
			#delete the projectile if it's off the screen
			if p.rect.x > WINDOW_SIZE[0]:
				purge.append(i)
		for i in reversed(purge):
			del(self.projectiles[i])

		#return to normal state
		if self.direction == 1:
			self.image = self.images[self.currentAnim]
		else:
			self.image = pygame.transform.flip(self.images[self.currentAnim], 1, 0)

		#jump code
		if self.isJumping == True:
			self.jump()
			if self.direction ==1:
				self.image = self.images[2]
			else:
				self.image = pygame.transform.flip(self.images[2], 1, 0)
