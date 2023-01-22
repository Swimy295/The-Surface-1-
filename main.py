#Name: Swayem
#Start Date: December 7, 2022
#Program Name: The Surface
#Purpose: Opposite to the ASCII art game "The Cave", it will be a zelda type of game with abilities, save system, enemies, etc.

#Imports all of the start game functions from the start.py file
import start as s
import pygame, sys
import settings as se
from level import Level

#Starts the main startup menu system


class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((1280, 720))
		pygame.display.set_caption('The Surface')
		self.clock = pygame.time.Clock()

		self.level = Level()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(se.FPS)

if __name__ == '__main__':
	game = Game()
	game.run()