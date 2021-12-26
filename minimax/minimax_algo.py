from copy import deepcopy
import pygame

from checkers import board, piece

BLUE = (0, 0, 255)  # Manual user
RED = (255, 0, 0)   # AI agent


def minimax(position, depth, is_maximizing, game):
    """
    Minimax algorithm for the checkers game.
    """
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if is_maximizing:
        best_score = float('-inf')
        best_move = None
        for child in position.get_children(position, RED, game):
            score = minimax(child, depth - 1, False, game)[0]
            best_score = max(best_score, score)
            if best_score == score:
                best_move = child
        return best_score, best_move
    else:
        worst_score = float('inf')
        best_move = None
        for child in position.get_children(position, BLUE, game):
            score = minimax(child, depth - 1, True, game)[0]
            best_score = max(best_score, score)
            if worst_score == score:
                best_move = child
        return best_score, best_move


def simulate_move(piece, move, board, game, skip):
    """
    Simulates a move on the board.
    """
    board.move_piece(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_children(board, player, game):
    """
    Returns a list of all possible moves for the player.
    """
    children = []
    for move in board.get_all_pieces(player):
        valid_moves = board.get_valid_moves(piece)

        for move, skip in valid_moves.items:
            temp_board = deepcopy(board)
            new_board = simulate_move(piece, move, temp_board, game, skip)
            children.append(new_board)
    return children
