import pygame

class GameText:
	def __init__(self):		
		self.textobjects = []
		
		#Game Controls
		self.textobjects.append(self.get_text('Controls', (0,0,0), (255,255,255), 600, 50, 36))
		self.textobjects.append(self.get_text('SPACE - Jump', (0,0,0), (255,255,255), 600, 75, 20))
		self.textobjects.append(self.get_text('SHIFT - Sprint', (0,0,0), (255,255,255), 600, 95, 20))
		self.textobjects.append(self.get_text('WASD - Move', (0,0,0), (255,255,255), 600, 115, 20))
		self.textobjects.append(self.get_text('R - Block', (0,0,0), (255,255,255), 600, 130, 20))
		self.textobjects.append(self.get_text('CTRL - Shoot', (0,0,0), (255,255,255), 600, 145, 20))
		
		#Player 1 health
		self.textobjects.append(self.get_text('Player 1 Health', (0,0,0), (255,255,255), 200, 50, 20))
		
	def get_text(self, text, color, bgcolor, cx, cy, size):
		font = pygame.font.Font(None, size)
		t = font.render(text, True, color, bgcolor)
		t_rect = t.get_rect()
		t_rect.centerx = cx
		t_rect.centery = cy
		
		return t, t_rect