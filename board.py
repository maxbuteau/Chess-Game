from piece import Rook
from piece import Knight
from piece import Bishop
from piece import Queen
from piece import King
from piece import Pawn
from piece import Piece
import copy

COLS = 8
ROWS = 8


class Board:
    def __init__(self):
        self.cols = COLS
        self.rows = ROWS
        self.captured_piece = None
        self.turn = "white"
        self.board = [[0 for col in range(COLS)] for rows in range(ROWS)]

        # Black pieces
        self.board[0][0] = Rook(0, 0, "black")
        self.board[0][1] = Knight(0, 1, "black")
        self.board[0][2] = Bishop(0, 2, "black")
        self.board[0][3] = Queen(0, 3, "black")
        self.board[0][4] = King(0, 4, "black")
        self.board[0][5] = Bishop(0, 5, "black")
        self.board[0][6] = Knight(0, 6, "black")
        self.board[0][7] = Rook(0, 7, "black")

        # Black pawns
        self.board[1][0] = Pawn(1, 0, "black")
        self.board[1][1] = Pawn(1, 1, "black")
        self.board[1][2] = Pawn(1, 2, "black")
        self.board[1][3] = Pawn(1, 3, "black")
        self.board[1][4] = Pawn(1, 4, "black")
        self.board[1][5] = Pawn(1, 5, "black")
        self.board[1][6] = Pawn(1, 6, "black")
        self.board[1][7] = Pawn(1, 7, "black")

        # White pieces
        self.board[7][0] = Rook(7, 0, "white")
        self.board[7][1] = Knight(7, 1, "white")
        self.board[7][2] = Bishop(7, 2, "white")
        self.board[7][3] = Queen(7, 3, "white")
        self.board[7][4] = King(7, 4, "white")
        self.board[7][5] = Bishop(7, 5, "white")
        self.board[7][6] = Knight(7, 6, "white")
        self.board[7][7] = Rook(7, 7, "white")

        # White pawns
        self.board[6][0] = Pawn(6, 0, "white")
        self.board[6][1] = Pawn(6, 1, "white")
        self.board[6][2] = Pawn(6, 2, "white")
        self.board[6][3] = Pawn(6, 3, "white")
        self.board[6][4] = Pawn(6, 4, "white")
        self.board[6][5] = Pawn(6, 5, "white")
        self.board[6][6] = Pawn(6, 6, "white")
        self.board[6][7] = Pawn(6, 7, "white")

    def get_piece(self, row, col):
        return self.board[row][col]

    def update_board(self):
        for row in range(0, 8):
            for col in range(0, 8):
                piece = self.board[row][col]
                if piece != 0:
                    if piece.row != row or piece.col != col:
                        self.board[piece.row][piece.col] = piece
                        self.board[row][col] = 0

    def is_in_check(self, color):
        king_pos = None
        # Finding the king
        for row in range(0, 8):
            for col in range(0, 8):
                piece = self.board[row][col]
                if piece != 0 and piece.color == color and piece.is_king:
                    king_pos = (piece.row, piece.col)
                    break
        # Check if one of the opposing pieces puts the king in check
        for row in range(0, 8):
            for col in range(0, 8):
                piece = self.board[row][col]
                if piece != 0 and piece.color != color:
                    for move in piece.get_valid_moves(self.board):
                        if move == king_pos:
                            return king_pos
        return False

    def get_legal_moves(self, piece):
        start_row = piece.row
        start_col = piece.col
        moves = piece.get_valid_moves(self.board)
        already_moved = piece.has_moved

        for move in moves[:]:
            if self.board[move[0]][move[1]] != 0:
                self.captured_piece = self.board[move[0]][move[1]]
            piece.move(move[0], move[1])
            self.update_board()
            if self.is_in_check(piece.color) is not False:
                moves.remove(move)
            piece.move(start_row, start_col)
            if not already_moved:
                piece.has_moved = False
            self.update_board()
            if self.captured_piece is not None:
                self.board[self.captured_piece.row][self.captured_piece.col] = self.captured_piece
                self.captured_piece = None
        return moves

    def get_game_status(self):
        turn_to_check = ""
        if self.turn == "white":
            turn_to_check = "black"
        else:
            turn_to_check = "white"

        # Checkmate
        if self.is_in_check(turn_to_check) is not False:
            total_moves = []
            for row in range(0, 8):
                for col in range(0, 8):
                    piece = self.board[row][col]
                    if piece != 0 and piece.color == turn_to_check:
                        total_moves.append(self.get_legal_moves(piece))
            if not any(total_moves):
                print(f"Checkmate, {turn_to_check} lost")

        # Stalemate
        elif not self.is_in_check(turn_to_check):
            total_moves = []
            for row in range(0, 8):
                for col in range(0, 8):
                    piece = self.board[row][col]
                    if piece != 0 and piece.color == turn_to_check:
                        total_moves.append(self.get_legal_moves(piece))
            if not any(total_moves):
                print("Stalemate")





