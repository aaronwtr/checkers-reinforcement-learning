import pygame
from checkers.actions import Actions
from checkers.board import Board
from utils.constants import *

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def get_pos_from_mouse(pos):
    """
    Returns the position of the mouse on the board
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    """
    Main function of the program
    """
    run = True
    clock = pygame.time.Clock()
    board = Board()
    actions = Actions(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                if actions.turn:
                    actions.select(row, col)

        actions.update()

    pygame.quit()


main()
