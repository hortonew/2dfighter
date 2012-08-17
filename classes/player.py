import pygame
gravity = 0.5
groundY = 300
class Player(pygame.sprite.Sprite):
	def __init__(self, images):
		pygame.sprite.Sprite.__init__(self)
		self.images = images
		self.image = self.images[0]
		#self.rect = self.image.get_rect()
		self.rect = self.image.get_rect().move([200, 300])
		
		#last image to return to after odd movements like jumping
		self.last_image = self.image
		
		#controls how fast to the right and left the player can move.
		#starting_x_speed allows the x_speed to return to normal after sprinting
		self.starting_x_speed = 9
		self.x_speed = 9
		
		#self.starting_y_speed = 9
		#self.y_speed = 9
		
		#current speed of player
		self.speed = [0, 0]
		
		#self.jump_height = 30
		self.isJumping = False
		
		#acceleration of player in upward direction
		self.vSpeed = 0
		
		#max acceleration in upward direction
		self.maxVSpeed = 3
		
		#controls what the starting vSpeed gets set to when jump is pressed
		self.jumpForce = 8
		
		#starting y value of player (ground)
		self.y = 300
		
	def updateSpeed(self, spd, i, x, y):
		#return to previous state (usually after a jump, or possibly attack)
		if i == -1:
			self.image = self.last_image
		else:
			#store the current image as the last image to revert back to later
			self.last_image = self.image
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
		self.rect = self.rect.move(self.speed)
		
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
		if self.isJumping == True:
			self.jump()
			if self.speed[0] > 0:
				self.image = self.images[2]
			else:
				self.image = pygame.transform.flip(self.images[2], 1, 0)
		if self.rect[1] >= groundY and self.image != self.images[3]:
			if self.speed[0] > 0:
				self.image = self.images[0]
			else:
				self.image = pygame.transform.flip(self.images[0], 1, 0)
