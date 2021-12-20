import pygame

WIDTH, HEIGHT = 800, 800
NUM_ROWS, NUM_COLS = 8, 8
SQUARE_SIZE = WIDTH // NUM_COLS

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CROWN = pygame.transform.scale(pygame.image.load('utils/assets/crown.png'), (44, 25))
