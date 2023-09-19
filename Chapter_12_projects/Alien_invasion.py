import sys
import pygame

class AlienInvasion:
	""" class to manage """
	def __init__(self):

		""" initializing resources """
		pygame.init()

		self.screen = pygame.display.set_mode((1200,800))
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		""" start the main loop for the game"""
		while True:
			# watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			# make the most recently drawn screen visible
			pygame.display.flip()

