import pygame

class GameText:
	def __init__(self):
		t1, t1_rect = self.get_text('Controls', (0,0,0), (255,255,255), 600, 50, 36)
		t2, t2_rect = self.get_text('SPACE - Jump', (0,0,0), (255,255,255), 600, 75, 20)
		t3, t3_rect = self.get_text('SHIFT - Sprint', (0,0,0), (255,255,255), 600, 95, 20)
		t4, t4_rect = self.get_text('WASD - Move', (0,0,0), (255,255,255), 600, 115, 20)
		t5, t5_rect = self.get_text('R - Block', (0,0,0), (255,255,255), 600, 130, 20)
		t6, t6_rect = self.get_text('CTRL - Shoot', (0,0,0), (255,255,255), 600, 145, 20)
		
		self.textobjects = [
			[t1, t1_rect],
			[t2, t2_rect],
			[t3, t3_rect],
			[t4, t4_rect],
			[t5, t5_rect],
			[t6, t6_rect]
		]
		
	def get_text(self, text, color, bgcolor, cx, cy, size):
		font = pygame.font.Font(None, size)
		t = font.render(text, True, color, bgcolor)
		t_rect = t.get_rect()
		t_rect.centerx = cx
		t_rect.centery = cy
		
		return t, t_rect