import pygame
from utils.constants import *
from checkers.board import Board


class Actions:
    def __init__(self, screen):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.valid_moves = {}
        self.screen = screen

    def update(self):
        self.board.draw(self.screen)
        pygame.display.update()