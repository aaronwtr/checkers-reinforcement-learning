import pygame
from checkers.actions import Actions
from checkers.board import Board
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

    TO-DO:
    - BUG: simulate_move messes up the count of pieces which causes the game to abort prematurely. However, we need the
    simulate_move function to remove pieces so that minimax can correctly evaluate the board.
    """
    clock = pygame.time.Clock()
    run = True
    actions = Actions(WIN)
    board = Board()

    while run:
        clock.tick(FPS)

        if actions.turn == RED:
            value, new_board = minimax(actions.get_board(), 3, True, actions)   # Higher depth means AI can look
                                                                                        # further ahead but it will be
                                                                                        # significantly slower.
            actions.minimax_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                if actions.turn:
                    actions.select(row, col)
        actions.check_for_draw()

        actions.update()


main()
