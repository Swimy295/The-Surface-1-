import pygame
import settings as se

class UI:
	def __init__(self):
		
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(se.UI_FONT,se.UI_FONT_SIZE)

		# bar setup 
		self.health_bar_rect = pygame.Rect(10,10,se.HEALTH_BAR_WIDTH,se.BAR_HEIGHT)
		self.energy_bar_rect = pygame.Rect(10,34,se.ENERGY_BAR_WIDTH,se.BAR_HEIGHT)

		# convert weapon dictionary
		self.weapon_graphics = []
		for weapon in se.weapon_data.values():
			path = weapon['graphic']
			weapon = pygame.image.load(path).convert_alpha()
			self.weapon_graphics.append(weapon)


	def show_bar(self,current,max_amount,bg_rect,color):
		# draw bg 
		pygame.draw.rect(self.display_surface,se.UI_BG_COLOR,bg_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width

		# drawing the bar
		pygame.draw.rect(self.display_surface,color,current_rect)
		pygame.draw.rect(self.display_surface,se.UI_BORDER_COLOR,bg_rect,3)

	def show_exp(self,exp):
		text_surf = self.font.render(str(int(exp)),False,se.TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 20
		y = self.display_surface.get_size()[1] - 20
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,se.UI_BG_COLOR,text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,se.UI_BORDER_COLOR,text_rect.inflate(20,20),3)

	def selection_box(self,left,top, has_switched):
		bg_rect = pygame.Rect(left,top,se.ITEM_BOX_SIZE,se.ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surface,se.UI_BG_COLOR,bg_rect)
		if has_switched:
			pygame.draw.rect(self.display_surface,se.UI_BORDER_COLOR_ACTIVE,bg_rect,3)
		else:
			pygame.draw.rect(self.display_surface,se.UI_BORDER_COLOR,bg_rect,3)
		return bg_rect

	def weapon_overlay(self,weapon_index,has_switched):
		bg_rect = self.selection_box(10,630,has_switched)
		weapon_surf = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(weapon_surf,weapon_rect)

	def display(self,player):
		self.show_bar(player.health,player.stats['health'],self.health_bar_rect,se.HEALTH_COLOR)
		self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,se.ENERGY_COLOR)

		self.show_exp(player.exp)

		self.weapon_overlay(player.weapon_index,not player.can_switch_weapon)
		# self.selection_box(80,635) # magic