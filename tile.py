import pygame 
import settings as se

#Tile class
class Tile(pygame.sprite.Sprite):
    #Defines the tilesizes
	def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((se.TILESIZE,se.TILESIZE))):
		
    #gets the sprite typs and then turns it into a colliding object
		super().__init__(groups)
		self.sprite_type = sprite_type
		self.image = surface
		if sprite_type == 'object':
			self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - se.TILESIZE))
		else:
			self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)