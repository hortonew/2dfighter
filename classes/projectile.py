import pygame
LEFT = -1
GRAVITY = 1.3
groundY = 300
class Projectile(object):
	def __init__(self, affected_by_gravity=False, rect=pygame.Rect((200,200,200,200)), color=(255,0,0), speed=10, x=100, y=100, direction=LEFT):
		self.rect = rect
		self.color = color
		self.speed = speed
		self.direction = direction
		self.affected_by_gravity = affected_by_gravity
		self.rect.x = x
		self.rect.y = y
	def update(self):
		if self.direction == LEFT:
			self.rect.x -= self.speed
		else:
			self.rect.x += self.speed
		if self.affected_by_gravity:
			self.rect.y += GRAVITY 
		#need condition to check if bullet is beyond ground
