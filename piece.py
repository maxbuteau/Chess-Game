class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.move_list = []

    def update_move_list(self, board):
        self.move_list = self.get_legal_moves(board)


class Pawn(Piece):
    pass


class Rook(Piece):
    def get_legal_moves(self, board):
        moves = []
        # Up
        for row in range(self.row - 1, -1, -1):
            square = board[row][self.col]
            if square is not Piece:
                moves.append((row, self.col))
            elif square.color != self.color:
                moves.append((row, self.col))
                break
            else:
                break

        # Down
        for row in range(self.row + 1, 8):
            square = board[row][self.col]
            if square is not Piece:
                moves.append((row, self.col))
            elif square.color != self.color:
                moves.append((row, self.col))
                break
            else:
                break

        # Left
        for col in range(self.col - 1, -1, -1):
            square = board[self.row][col]
            if square is not Piece:
                moves.append((self.row, col))
            elif square.color != self.color:
                moves.append((self.row, col))
                break
            else:
                break

        # Right
        for col in range(self.col + 1, 8):
            square = board[self.row][col]
            if square is not Piece:
                moves.append((self.row, col))
            elif square.color != self.color:
                moves.append((self.row, col))
                break
            else:
                break
        return moves


class Knight(Piece):
    def get_legal_moves(self, board):
        moves = []

        # Up and right (row - 2) (col + 1)
        if self.row > 1 and self.col < 7:
            if board[self.row - 2][self.col + 1] is not Piece:
                moves.append((self.row - 2, self.col + 1))
            elif board[self.row - 2][self.col + 1].color != self.color:
                moves.append((self.row - 2, self.col + 1))

        # Up and left (row - 2) (col - 1)
        if self.row > 1 and self.col > 0:
            if board[self.row - 2][self.col - 1] is not Piece:
                moves.append((self.row - 2, self.col - 1))
            elif board[self.row - 2][self.col - 1].color != self.color:
                moves.append((self.row - 2, self.col - 1))

        # Right and up (row - 1) (col + 2)
        if self.row > 0 and self.col < 6:
            if board[self.row - 1][self.col + 2] is not Piece:
                moves.append((self.row - 1, self.col + 2))
            elif board[self.row - 1][self.col + 2].color != self.color:
                moves.append((self.row - 1, self.col + 2))

        # Right and down (row + 1) (col + 2)
        if self.row < 7 and self.col < 6:
            if board[self.row + 1][self.col + 2] is not Piece:
                moves.append((self.row + 1, self.col + 2))
            elif board[self.row + 1][self.col + 2].color != self.color:
                moves.append((self.row + 1, self.col + 2))

        # Down and right (row + 2) (col + 1)
        if self.row < 6 and self.col < 7:
            if board[self.row + 2][self.col + 1] is not Piece:
                moves.append((self.row + 2, self.col + 1))
            elif board[self.row + 2][self.col + 1].color != self.color:
                moves.append((self.row + 2, self.col + 1))

        # Down and left (row + 2) (col - 1)
        if self.row < 6 and self.col > 0:
            if board[self.row + 2][self.col - 1] is not Piece:
                moves.append((self.row + 2, self.col - 1))
            elif board[self.row + 2][self.col - 1].color != self.color:
                moves.append((self.row + 2, self.col - 1))

        # Left and up (row - 1) (col - 2)
        if self.row > 0 and self.col > 1:
            if board[self.row - 1][self.col - 2] is not Piece:
                moves.append((self.row - 1, self.col - 2))
            elif board[self.row - 1][self.col - 2].color != self.color:
                moves.append((self.row - 1, self.col - 2))

        # Left and down (row + 1) (col - 2)
        if self.row < 7 and self.col > 1:
            if board[self.row + 1][self.col - 2] is not Piece:
                moves.append((self.row + 1, self.col - 2))
            elif board[self.row + 1][self.col - 2].color != self.color:
                moves.append((self.row + 1, self.col - 2))


class Bishop(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass


