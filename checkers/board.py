import pygame
from ..utils.constants import *


class Board:
    def __init__(self):
        self.board = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
        self.selected = None
        self.blue_left = self.red_left = 12
        self.blue_kings = self.red_kings = 0
        self.board[3][3] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.board[4][4] = 1
        self.turn = 1
        self.winner = 0

    def draw_board(self, screen):
        for row in range(HEIGHT):
            for col in range(WIDTH):
                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))