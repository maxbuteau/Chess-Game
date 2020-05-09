from piece import Rook
from piece import Knight
from piece import Bishop
from piece import Queen
from piece import King
from piece import Pawn
from piece import Piece

COLS = 8
ROWS = 8

white_piece = {
    Pawn: 'P',
    Rook: 'R',
    Knight: 'N',
    Bishop: 'B',
    King: 'K',
    Queen: 'Q'
}

black_piece = {
    Pawn: 'p',
    Rook: 'r',
    Knight: 'n',
    Bishop: 'b',
    King: 'k',
    Queen: 'q'
}


class Board:
    def __init__(self):
        self.cols = COLS
        self.rows = ROWS

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

        # Black pawns
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

    def display(self):

        row_counter = self.rows
        for row in self.board:
            output = ''
            for piece in row:
                if piece == 0:
                    output += ' - '
                else:
                    if piece.color == "white":
                        output += f' {white_piece.get(type(piece))} '
                    else:
                        output += f' {black_piece.get(type(piece))} '
            print(output + f'   {row_counter}')
            row_counter -= 1
        print()
        print(' a  b  c  d  e  f  g  h ')





