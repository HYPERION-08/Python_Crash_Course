import sys
import pygame

class AlienInvasion:
	""" class to manage """
	def __init__(self):

		""" initializing resources """
		pygame.init()

		self.screen = pygame.display.set_mode((1200,800))
		pygame.display.set_caption("Alien Invasion")
