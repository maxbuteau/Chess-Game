class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.move_list = []

    def update_move_list(self, board):
        self.move_list = self.get_legal_moves(board)


class Pawn(Piece):
    def get_valid_moves(self, board):
        moves = []

        # White
        if self.color == "white":
            if self.row > 0:
                # Move straight
                if not isinstance(board[self.row - 1][self.col], Piece):
                    moves.append((self.row - 1, self.col))
                # Capture diagonally left
                if self.col > 0:
                    if isinstance(board[self.row - 1][self.col - 1], Piece) and board[self.row - 1][self.col - 1].color != self.color:
                        moves.append((self.row - 1, self.col - 1))
                # Capture diagonally right
                if self.col < 7:
                    if isinstance(board[self.row - 1][self.col + 1], Piece) and board[self.row - 1][self.col + 1].color != self.color:
                        moves.append((self.row - 1, self.col + 1))

            # Starting position
            if self.row == 6:
                # Move straight by 2
                if not isinstance(board[self.row - 1][self.col], Piece) and not isinstance(board[self.row - 2][self.col], Piece):
                    moves.append((self.row - 2, self.col))

        # Black
        else:
            if self.row < 7:
                # Move straight
                if not isinstance(board[self.row + 1][self.col], Piece):
                    moves.append((self.row + 1, self.col))
                # Capture diagonally left
                if self.col > 0:
                    if isinstance(board[self.row + 1][self.col - 1], Piece) and board[self.row + 1][self.col - 1].color != self.color:
                        moves.append((self.row + 1, self.col - 1))
                # Capture diagonally right
                if self.col < 7:
                    if isinstance(board[self.row + 1][self.col + 1], Piece) and board[self.row + 1][self.col + 1].color != self.color:
                        moves.append((self.row + 1, self.col + 1))

            # Starting position
            if self.row == 1:
                if not isinstance(board[self.row + 1][self.col], Piece) and not isinstance(board[self.row + 2][self.col], Piece):
                    moves.append((self.row + 2, self.col))

        return moves


class Rook(Piece):
    def get_valid_moves(self, board):
        moves = []
        # Up
        for row in range(self.row - 1, -1, -1):
            square = board[row][self.col]
            if not isinstance(square, Piece):
                moves.append((row, self.col))
            elif square.color != self.color:
                moves.append((row, self.col))
                break
            else:
                break

        # Down
        for row in range(self.row + 1, 8):
            square = board[row][self.col]
            if not isinstance(square, Piece):
                moves.append((row, self.col))
            elif square.color != self.color:
                moves.append((row, self.col))
                break
            else:
                break

        # Left
        for col in range(self.col - 1, -1, -1):
            square = board[self.row][col]
            if not isinstance(square, Piece):
                moves.append((self.row, col))
            elif square.color != self.color:
                moves.append((self.row, col))
                break
            else:
                break

        # Right
        for col in range(self.col + 1, 8):
            square = board[self.row][col]
            if not isinstance(square, Piece):
                moves.append((self.row, col))
            elif square.color != self.color:
                moves.append((self.row, col))
                break
            else:
                break
        return moves


class Knight(Piece):
    def get_valid_moves(self, board):
        moves = []

        # Up and right (row - 2) (col + 1)
        if self.row > 1 and self.col < 7:
            if not isinstance(board[self.row - 2][self.col + 1], Piece):
                moves.append((self.row - 2, self.col + 1))
            elif board[self.row - 2][self.col + 1].color != self.color:
                moves.append((self.row - 2, self.col + 1))

        # Up and left (row - 2) (col - 1)
        if self.row > 1 and self.col > 0:
            if not isinstance(board[self.row - 2][self.col - 1], Piece):
                moves.append((self.row - 2, self.col - 1))
            elif board[self.row - 2][self.col - 1].color != self.color:
                moves.append((self.row - 2, self.col - 1))

        # Right and up (row - 1) (col + 2)
        if self.row > 0 and self.col < 6:
            if not isinstance(board[self.row - 1][self.col + 2], Piece):
                moves.append((self.row - 1, self.col + 2))
            elif board[self.row - 1][self.col + 2].color != self.color:
                moves.append((self.row - 1, self.col + 2))

        # Right and down (row + 1) (col + 2)
        if self.row < 7 and self.col < 6:
            if not isinstance(board[self.row + 1][self.col + 2], Piece):
                moves.append((self.row + 1, self.col + 2))
            elif board[self.row + 1][self.col + 2].color != self.color:
                moves.append((self.row + 1, self.col + 2))

        # Down and right (row + 2) (col + 1)
        if self.row < 6 and self.col < 7:
            if not isinstance(board[self.row + 2][self.col + 1], Piece):
                moves.append((self.row + 2, self.col + 1))
            elif board[self.row + 2][self.col + 1].color != self.color:
                moves.append((self.row + 2, self.col + 1))

        # Down and left (row + 2) (col - 1)
        if self.row < 6 and self.col > 0:
            if not isinstance(board[self.row + 2][self.col - 1], Piece):
                moves.append((self.row + 2, self.col - 1))
            elif board[self.row + 2][self.col - 1].color != self.color:
                moves.append((self.row + 2, self.col - 1))

        # Left and up (row - 1) (col - 2)
        if self.row > 0 and self.col > 1:
            if not isinstance(board[self.row - 1][self.col - 2], Piece):
                moves.append((self.row - 1, self.col - 2))
            elif board[self.row - 1][self.col - 2].color != self.color:
                moves.append((self.row - 1, self.col - 2))

        # Left and down (row + 1) (col - 2)
        if self.row < 7 and self.col > 1:
            if not isinstance(board[self.row + 1][self.col - 2], Piece):
                moves.append((self.row + 1, self.col - 2))
            elif board[self.row + 1][self.col - 2].color != self.color:
                moves.append((self.row + 1, self.col - 2))

        return moves


class Bishop(Piece):
    def get_valid_moves(self, board):
        moves = []

        # Diagonally up right
        row = self.row - 1
        col = self.col + 1
        while self.row > -1 and self.col < 8:
            if not isinstance(board[row][col], Piece):
                moves.append((row, col))
            elif board[row][col].color != self.color:
                moves.append((row, col))
                break
            else:
                break
            row -= 1
            col += 1

            # Diagonally down right
            row = self.row + 1
            col = self.col + 1
            while self.row < 8 and self.col < 8:
                if not isinstance(board[row][col], Piece):
                    moves.append((row, col))
                elif board[row][col].color != self.color:
                    moves.append((row, col))
                    break
                else:
                    break
                row += 1
                col += 1

            # Diagonally down left
            row = self.row + 1
            col = self.col - 1
            while self.row < 8 and self.col > -1:
                if not isinstance(board[row][col], Piece):
                    moves.append((row, col))
                elif board[row][col].color != self.color:
                    moves.append((row, col))
                    break
                else:
                    break
                row += 1
                col -= 1

            # Diagonally up left
            row = self.row - 1
            col = self.col + 1
            while self.row > -1 and self.col < 8:
                if not isinstance(board[row][col], Piece):
                    moves.append((row, col))
                elif board[row][col].color != self.color:
                    moves.append((row, col))
                    break
                else:
                    break
        return moves


class Queen(Piece):
    def get_valid_moves(self, board):
        moves = []

        # Up
        row = self.row - 1
        col = self.col
        while row > -1:
            if not isinstance(board[row][col], Piece):
                moves.append((row, col))
            elif board[row][col].color != self.color:
                moves.append((row, col))
                break
            else:
                break
            row -= 1

        # Diagonally up and right
        row = self.row - 1
        col = self.col + 1
        while row > -1 and col < 8:
            if not isinstance(board[row][col], Piece):
                moves.append((row, col))
            elif board[row][col].color != self.color:
                moves.append((row, col))
                break
            else:
                break
            row -= 1
            col += 1

        # Right
        row = self.row
        col = self.col + 1
        while col < 8:
            if not isinstance(board[row][col], Piece):
                moves.append((row, col))
            elif board[row][col].color != self.color:
                moves.append((row, col))
                break
            else:
                break
            col += 1

        # Diagonally right and down
        row = self.row + 1
        col = self.col + 1
        while row < 8 and col < 8:
            if not isinstance(board[row][col], Piece):
                moves.append((row, col))
            elif board[row][col].color != self.color:
                moves.append((row, col))
                break
            else:
                break
            row += 1
            col += 1

        # Down
        row = self.row + 1
        col = self.col
        while row < 8:
            if not isinstance(board[row][col], Piece):
                moves.append((row, col))
            elif board[row][col].color != self.color:
                moves.append((row, col))
                break
            else:
                break
            row += 1

        # Diagonally left and down
        row = self.row + 1
        col = self.col - 1
        while row < 8 and col > -1:
            if not isinstance(board[row][col], Piece):
                moves.append((row, col))
            elif board[row][col].color != self.color:
                moves.append((row, col))
                break
            else:
                break
            row += 1
            col -= 1

        # Left
        row = self.row
        col = self.col - 1
        while col > -1:
            if not isinstance(board[row][col], Piece):
                moves.append((row, col))
            elif board[row][col].color != self.color:
                moves.append((row, col))
                break
            else:
                break
            col -= 1

        # Diagonally left and up
        row = self.row - 1
        col = self.col - 1
        while row > -1:
            if not isinstance(board[row][col], Piece):
                moves.append((row, col))
            elif board[row][col].color != self.color:
                moves.append((row, col))
                break
            else:
                break
            row -= 1
            col -= 1

        return moves


class King(Piece):
    def get_valid_moves(self, board):
        moves = []

        # Up (row - 1)
        if self.row > 0:
            if not isinstance(board[self.row - 1][self.col], Piece):
                moves.append((self.row - 1, self.col))
            elif board[self.row - 1][self.col].color != self.color:
                moves.append((self.row - 1, self.col))

        # Diagonally up and right (row - 1) (col + 1)
        if self.row > 0 and self.col < 7:
            if not isinstance(board[self.row - 1][self.col + 1], Piece):
                moves.append((self.row - 1, self.col + 1))
            elif board[self.row - 1][self.col + 1].color != self.color:
                moves.append((self.row - 1, self.col + 1))

        # Right (col + 1)
        if self.col < 7:
            if not isinstance(board[self.row][self.col + 1], Piece):
                moves.append((self.row, self.col + 1))
            elif board[self.row][self.col + 1].color != self.color:
                moves.append((self.row, self.col + 1))

        # Diagonally down and right (row + 1) (col + 1)
        if self.row < 7 and self.col < 7:
            if not isinstance(board[self.row + 1][self.col + 1], Piece):
                moves.append((self.row + 1, self.col + 1))
            elif board[self.row + 1][self.col + 1].color != self.color:
                moves.append((self.row + 1, self.col + 1))

        # Down (row + 1)
        if self.row < 7:
            if not isinstance(board[self.row + 1][self.col], Piece):
                moves.append((self.row + 1, self.col))
            elif board[self.row + 1][self.col].color != self.color:
                moves.append((self.row + 1, self.col))

        # Diagonally down and left (row + 1) (col - 1)
        if self.row < 7 and self.col > 0:
            if not isinstance(board[self.row + 1][self.col - 1], Piece):
                moves.append((self.row + 1, self.col - 1))
            elif board[self.row + 1][self.col - 1].color != self.color:
                moves.append((self.row + 1, self.col - 1))

        # Left (col - 1)
        if self.col > 0:
            if not isinstance(board[self.row][self.col - 1], Piece):
                moves.append((self.row, self.col - 1))
            elif board[self.row][self.col - 1].color != self.color:
                moves.append((self.row, self.col - 1))

        # Diagonally up and left (row - 1) (col - 1)
        if self.row > 0 and self.col > 0:
            if not isinstance(board[self.row - 1][self.col - 1], Piece):
                moves.append((self.row - 1, self.col - 1))
            elif board[self.row - 1][self.col - 1].color != self.color:
                moves.append((self.row - 1, self.col - 1))

        return moves

