import pygame
from utils.constants import *
from .piece import Piece


class Board:
    def __init__(self):
        """
        Initializes the board.
        """
        self.board = []
        self.blue_left = self.red_left = 12
        self.blue_kings = self.red_kings = 0
        self.create_board()
        self.run = True

    def draw_grid(self, screen):
        """
        Draws the grid on the screen.
        :param screen: The screen to draw on.
        """
        screen.fill(BLACK)
        for row in range(HEIGHT):
            for col in range(row % 2, NUM_ROWS, 2):
                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        """
        Moves a piece to a new position.
        :param piece: The piece to move.
        :param row: The row to move to.
        :param col: The column to move to.
        """
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == 0 or row == NUM_ROWS - 1:
            if piece.color == RED and not piece.king:
                self.red_kings += 1
                piece.make_king()
            if piece.color == BLUE and not piece.king:
                self.blue_kings += 1
                piece.make_king()

    def evaluate(self):
        """
        Given the current state of the board, return the corresponding score. Note that red is the AI agent. We also
        want to prioritize obtaining kings.
        :return: Evaluation score of the current state.
        """
        return self.red_left - 2 * self.blue_left + (self.red_kings * 0.3 - self.blue_kings * 0.5)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)

        return pieces

    def get_piece(self, row, col):
        """
        Gets the piece at a certain position.
        :param row: The row of the piece.
        :param col: The column of the piece.
        :return: The piece at the position.
        """
        return self.board[row][col]

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

    def remove_piece(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLUE:
                    self.blue_left -= 1
                else:
                    self.red_left -= 1

                if self.winner() is not None:
                    print("The winner is: " + str(self.winner()))
                    pygame.quit()
                    exit()

    def winner(self):
        if self.red_left <= 0:
            return "Blue"
        elif self.blue_left <= 0:
            return "Red"

        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BLUE or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, NUM_ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, NUM_ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            potential_move = self.board[r][left]
            if potential_move == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last  # If checks are passed, add the move to dict of valid moves

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, NUM_ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break

            elif potential_move.color == color:
                break
            else:
                last = [potential_move]  # if after one jump we can still jump, adjust the last list
            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= NUM_COLS:
                break

            potential_move = self.board[r][right]
            if potential_move == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last  # If checks are passed, add the move to dict of valid moves

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, NUM_ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break

            elif potential_move.color == color:
                break
            else:
                last = [potential_move]  # if after one jump we can still jump, adjust the last list
            right += 1

        return moves
