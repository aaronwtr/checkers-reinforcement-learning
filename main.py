import pygame
from checkers.actions import Actions
from utils.constants import *
from minimax.minimax_algo import minimax

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
    clock = pygame.time.Clock()
    run = True
    actions = Actions(WIN)

    while run:
        clock.tick(FPS)

        if actions.turn == RED:
            value, new_board = minimax(actions.get_board(), 3, RED, actions)    # Higher depth means AI can look further
                                                                                # ahead but it will be significantly slower.
            actions.minimax_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                if actions.turn:
                    actions.select(row, col)

        actions.update()


main()
