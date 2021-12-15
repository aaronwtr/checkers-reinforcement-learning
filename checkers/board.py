import pygame
from utils.constants import *
from .piece import Piece


class Board:
    def __init__(self):
        """
        Initializes the board.
        """
        self.board = []
        self.selected = None
        self.blue_left = self.red_left = 12
        self.blue_kings = self.red_kings = 0
        self.create_board()
        # self.board[3][3] = 1
        # self.board[3][4] = 2
        # self.board[4][3] = 2
        # self.board[4][4] = 1
        # self.turn = 1
        # self.winner = 0

    def draw_grid(self, screen):
        """
        Draws the grid on the screen.
        :param screen: The screen to draw on.
        """
        screen.fill(BLACK)
        for row in range(HEIGHT):
            for col in range(row % 2, NUM_ROWS, 2):
                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        """
        Creates the board.
        """
        for row in range(NUM_ROWS):
            self.board.append([])
            for col in range(NUM_COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLUE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, screen):
        """
        Draws the pieces and the squares on the screen.
        :param screen: The screen to draw on.
        """
        self.draw_grid(screen)
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)
