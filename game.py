from tkinter import *
from board import Board
from piece import *

TILE_SIZE = 100


class BoardGUI(Frame):

    def __init__(self, parent, game):
        Frame.__init__(self, parent)
        self.parent = parent
        self.game = game
        self.board = game.board
        self.canvas = Canvas(self, width=800, height=800, bg="light grey")
        self.canvas.pack()
        self.draw_board()
        self.display_pieces()
        self.canvas.bind("<Button-1>", lambda event: self.on_click(event))
        self.is_in_check = False
        self.king_pos = None
        self.selected_piece = None

    def draw_board(self):
        for row in range(0, 8):
            for col in range(0, 8):
                x1 = col * TILE_SIZE
                y1 = row * TILE_SIZE
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE
                if (row + col) % 2 != 0:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="", fill="green")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="")

    def display_pieces(self):
        for row in range(0, 8):
            for col in range(0, 8):
                x1 = col * TILE_SIZE + 50
                y1 = row * TILE_SIZE + 50
                piece = self.board[row][col]
                if piece != 0:
                    img = PhotoImage(file="images/%s%s.png" % (piece.color[0], type(piece).__name__))
                    label = Label(image=img)
                    label.image = img  # keep a reference so that image is not garbage collected
                    self.canvas.create_image(x1, y1, image=img, anchor=CENTER, tags="img")

    def get_square(self, row, col):
        # canvas grid coords are inversed
        return self.canvas.find_overlapping(col * TILE_SIZE, row * TILE_SIZE, (col * TILE_SIZE) + TILE_SIZE, (row * TILE_SIZE) + 1)

    def show_available_moves(self, piece):
        for move in self.game.get_legal_moves(piece):
            square = self.get_square(move[0], move[1])
            self.canvas.itemconfig(square, fill="blue")

    def reset_highlights(self):
        for row in range(0, 8):
            for col in range(0, 8):
                square = self.get_square(row, col)
                if (row + col) % 2 != 0:
                    self.canvas.itemconfig(square, fill="green")
                else:
                    self.canvas.itemconfig(square, fill="")
        if self.is_in_check:
            square = self.get_square(self.king_pos[0], self.king_pos[1])
            self.canvas.itemconfig(square, fill="red")

    def move(self, row_to, col_to):
        is_promotion = False
        start_row = self.selected_piece.row
        self.selected_piece.move(row_to, col_to)
        self.game.update_board()
        for img in self.canvas.find_withtag("img"):
            self.canvas.delete(img)
        self.reset_highlights()
        self.display_pieces()

        if self.selected_piece.is_pawn:
            # Check for promotion
            if row_to == 0 or row_to == 7:
                is_promotion = True
                self.promote(self.selected_piece)

            # Update en passant possibility
            elif row_to == start_row + 2 or row_to == start_row - 2:
                self.game.en_passant_possibility = self.selected_piece

        # Reset en passant possibility
        if self.game.en_passant_possibility is not None and self.selected_piece.color != self.game.en_passant_possibility.color:
            self.game.en_passant_possibility = None

        self.selected_piece = None
        self.king_check_highlights()
        if self.game.get_game_status() != "Ongoing":
            self.display_end_screen(self.game.get_game_status())
        if not is_promotion:
            self.switch_turn()

    def switch_turn(self):
        if self.game.turn == "white":
            self.game.turn = "black"
        else:
            self.game.turn = "white"

    def king_check_highlights(self):
        if self.game.turn == "white":
            if self.game.is_in_check("black") is not False:
                self.is_in_check = True
                self.king_pos = self.game.is_in_check("black")
            elif self.game.is_in_check("white") is not False:
                self.is_in_check = True
                self.king_pos = self.game.is_in_check("white")
            else:
                self.is_in_check = False
                self.king_pos = None
        else:
            if self.game.is_in_check("white") is not False:
                self.is_in_check = True
                self.king_pos = self.game.is_in_check("white")
            elif self.game.is_in_check("black") is not False:
                self.is_in_check = True
                self.king_pos = self.game.is_in_check("black")
            else:
                self.is_in_check = False
                self.king_pos = None
        self.reset_highlights()

    def promote(self, pawn):

        self.canvas.unbind("<Button-1>")

        x1 = pawn.col * TILE_SIZE
        y1 = 0
        x2 = x1 + TILE_SIZE
        y2 = 0

        if self.selected_piece.color == "white":
            y2 = 4 * TILE_SIZE
        else:
            y1 = 4 * TILE_SIZE
            y2 = 8 * TILE_SIZE

        queen_image = PhotoImage(file="images/%sQueen.png" % (pawn.color[0]))
        queen_label = Label(image=queen_image)
        queen_label.image = queen_image  # keep a reference so that image is not garbage collected

        rook_image = PhotoImage(file="images/%sRook.png" % (pawn.color[0]))
        rook_label = Label(image=rook_image)
        rook_label.image = rook_image  # keep a reference so that image is not garbage collected

        knight_image = PhotoImage(file="images/%sKnight.png" % (pawn.color[0]))
        knight_label = Label(image=knight_image)
        knight_label.image = knight_image  # keep a reference so that image is not garbage collected

        bishop_image = PhotoImage(file="images/%sBishop.png" % (pawn.color[0]))
        bishop_label = Label(image=bishop_image)
        bishop_label.image = bishop_image  # keep a reference so that image is not garbage collected

        queen_button = Button(self.canvas, image=queen_image, command=lambda: self.switch_promoted_pawn(pawn, "Queen"))
        self.canvas.create_window(x1 + 50, y1 + 50, window=queen_button, tags="button")

        rook_button = Button(self.canvas, image=rook_image, command=lambda: self.switch_promoted_pawn(pawn, "Rook"))
        self.canvas.create_window(x1 + 50, y1 + TILE_SIZE + 50, window=rook_button, tags="button")

        knight_button = Button(self.canvas, image=knight_image, command=lambda: self.switch_promoted_pawn(pawn, "Knight"))
        self.canvas.create_window(x1 + 50, y1 + 2 * TILE_SIZE + 50, window=knight_button, tags="button")

        bishop_button = Button(self.canvas, image=bishop_image, command=lambda: self.switch_promoted_pawn(pawn, "Bishop"))
        self.canvas.create_window(x1 + 50, y1 + 3 * TILE_SIZE + 50, window=bishop_button, tags="button")

    def switch_promoted_pawn(self, pawn, piece):
        row = pawn.row
        col = pawn.col
        color = pawn.color

        if piece == "Queen":
            self.board[row][col] = Queen(row, col, color)
        elif piece == "Rook":
            self.board[row][col] = Rook(row, col, color)
        elif piece == "Knight":
            self.board[row][col] = Knight(row, col, color)
        else:
            self.board[row][col] = Bishop(row, col, color)

        for img in self.canvas.find_withtag("img"):
            self.canvas.delete(img)
        self.display_pieces()

        for btn in self.canvas.find_withtag("button"):
            self.canvas.delete(btn)

        self.king_check_highlights()
        if self.game.get_game_status() != "Ongoing":
            self.display_end_screen(self.game.get_game_status())
        self.switch_turn()

        self.canvas.bind("<Button-1>", lambda event: self.on_click(event))

    def display_end_screen(self, text):
        self.canvas.create_rectangle(50, 350, 750, 450, fill="white")
        self.canvas.create_text(400, 400, text=text, fill="blue", font=("Times", "46", "bold"))
        self.canvas.unbind("<Button-1>")

    def on_click(self, event):
        # Check click is on the board
        if event.y < 8 * TILE_SIZE and event.x < 8 * TILE_SIZE:
            row = int(event.y / TILE_SIZE)
            col = int(event.x / TILE_SIZE)
            piece = self.board[row][col]
            if self.selected_piece is not None and (row, col) in self.game.get_legal_moves(self.selected_piece):
                # Castling King side
                if self.selected_piece.is_king and col == self.selected_piece.col + 2:
                    turn = self.selected_piece.color
                    self.move(row, col)
                    # Prevent from switching turns even if move 2 pieces
                    self.game.turn = turn
                    self.selected_piece = self.board[row][col + 1]
                    self.move(row, col - 1)

                # Castling Queen side
                elif self.selected_piece.is_king and col == self.selected_piece.col - 2:
                    turn = self.selected_piece.color
                    self.move(row, col)
                    # Prevent from switching turns even if move 2 pieces
                    self.game.turn = turn
                    self.selected_piece = self.board[row][col - 2]
                    self.move(row, col + 1)

                # En passant
                elif self.selected_piece.is_pawn and col != self.selected_piece.col and self.board[row][col] == 0:
                    if self.game.turn == "white":
                        self.board[row + 1][col] = 0
                    else:
                        self.board[row - 1][col] = 0
                    self.move(row, col)

                # Normal move
                else:
                    self.move(row, col)

            else:
                self.reset_highlights()
                self.selected_piece = None
                if isinstance(piece, Piece) and piece.color == self.game.turn:
                    selected_square = self.get_square(piece.row, piece.col)
                    self.canvas.itemconfig(selected_square, fill="orange")
                    self.show_available_moves(piece)
                    self.selected_piece = piece


def start_game():
    root = Tk()
    root.title("Chess")
    game = Board()
    gui = BoardGUI(root, game)
    gui.pack(padx=25, pady=25)
    root.mainloop()


start_game()


