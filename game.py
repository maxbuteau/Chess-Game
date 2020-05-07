from board import Board
from piece import Rook

game = Board()
game.display()
piece = game.get_piece(7, 7)
print(piece.get_legal_moves(game.board))
