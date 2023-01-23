import pygame
import settings as se
import start as s

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

#Bars for the health and energy
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

#Shows the primary stats such as exp and name
	def show_stats(self,exp, NAME):
		#Names the two surfaces and then sets the variable identities
		Name_surf = self.font.render(("NAME: " + NAME),False,se.TEXT_COLOR)
		Name_rect = Name_surf.get_rect(topright = (1190, 20))
		Exp_surf = self.font.render(("EXP: " + str(exp)), False, se.TEXT_COLOR)
		Exp_rect = Exp_surf.get_rect(topright = (1190, 100))

    #Places all of the surfaces outlines in the created surfaces and rectangle above
		pygame.draw.rect(self.display_surface,se.UI_BG_COLOR,Name_rect.inflate(200,100))
		self.display_surface.blit(Name_surf, Name_rect)
		pygame.draw.rect(self.display_surface,se.UI_BORDER_COLOR,Name_rect.inflate(20,20),3)

		pygame.draw.rect(self.display_surface,se.UI_BG_COLOR,Exp_rect.inflate(180,100))
		self.display_surface.blit(Exp_surf, Exp_rect)
		pygame.draw.rect(self.display_surface,se.UI_BORDER_COLOR,Exp_rect.inflate(20,20),3)

  #Selection for the weapon in the bottom left.
	def selection_box(self,left,top, has_switched):
		#Places the rectangle with the border for the weapon overlay
		bg_rect = pygame.Rect(left,top,se.ITEM_BOX_SIZE,se.ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surface,se.UI_BG_COLOR,bg_rect)
		if has_switched:
			pygame.draw.rect(self.display_surface,se.UI_BORDER_COLOR_ACTIVE,bg_rect,3)
		else:
			pygame.draw.rect(self.display_surface,se.UI_BORDER_COLOR,bg_rect,3)
		return bg_rect

#weapon overlay that places the weapon onto the selectin box
	def weapon_overlay(self,weapon_index,has_switched):

    #Uses the weapon index to see if the weapon changes and then change the graphics based on the weapon
		bg_rect = self.selection_box(10,630,has_switched)
		weapon_surf = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(weapon_surf,weapon_rect)

#Updates the display with all of the variables
	def display(self,player):
		self.show_bar(player.health, 100, self.health_bar_rect,se.HEALTH_COLOR)
		self.show_bar(player.energy, 100, self.energy_bar_rect,se.ENERGY_COLOR)

		self.show_stats(player.exp, s.NAME)

		self.weapon_overlay(player.weapon_index,not player.can_switch_weapon)