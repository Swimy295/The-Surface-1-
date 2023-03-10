import pygame 
import settings as se
from tile import Tile
from player import Player
import support as su
from weapon import Weapon
from ui import UI

#Level class
class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# attack sprites
		self.current_attack = None

		# sprite setup
		self.create_map()

		# user interface 
		self.ui = UI()

  #Uses support class to us ethe csv files
	def create_map(self):
		layouts = {
			'boundary': su.import_csv_layout('map/map_FloorBlocks.csv'),
			'grass': su.import_csv_layout('map/map_Grass.csv'),
			'object': su.import_csv_layout('map/map_Objects.csv'),
		}
		graphics = {
			'grass': su.import_folder('graphics/Grass'),
			'objects': su.import_folder('graphics/objects')
		}

    #Sets the borders for the collisons. multimples the column and row size by the tilesizes to find the bounderies
		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * se.TILESIZE
						y = row_index * se.TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible')
						if style == 'object':
							surf = graphics['objects'][int(col)]
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)

    #Initiallizes the player
		self.player = Player((2000,1430),[self.visible_sprites],self.obstacle_sprites,self.create_attack,self.destroy_attack)

  #Attacks
	def create_attack(self):
		
		self.current_attack = Weapon(self.player,[self.visible_sprites])

  #kills the attack sprite
	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

  #Runs the functions
	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.ui.display(self.player)

#Camera setup to follow the player
class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup. Gets half of the distance around the player and then offsets it to lock onto the player
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('graphics/tilemap/ground.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

  #Draws the player in the offset
	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
