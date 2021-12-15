import pygame
from utils.constants import *


class Piece:
    PADDING = 10    # Padding between pieces
    PIECE_RADIUS = SQUARE_SIZE // 2 - PADDING   # Radius of piece

    def __init__(self, row, col, color):
        '''
        Initializes a piece object. Note that every piece is initialized with a row, col, and color.
        :param row: The row of the piece.
        :param col: The column of the piece.
        :param color: The color of the piece.
        '''
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == RED:
            self.direction = 1
        else:
            self.direction = -1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.PIECE_RADIUS)

    def __repr__(selfs):
        """
        Circumvents object pointers in the debugger. Allows of to see what piece is being pointed to.
        :return: A string representation of the piece.
        """
        return "Piece: " + str(selfs.row) + ", " + str(selfs.col) + ", " + str(selfs.color)
