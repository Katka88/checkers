import pygame
from checkers.constants import BLACK, ROWS, RED, SQUARE_SIZE, WHITE, GREY, COLS

class Board:
    def __init__(self):
        self.board = [[]]
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0

    def draw_squares(self, screen):
        screen.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(screen, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

     #red and black squares

    def create_pieces(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))

class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1 #0;0 is form up to down, left to right raising

        self.x = 0
        self.y = 0

        self.position()

    def position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE / 2
        self.x = SQUARE_SIZE * self.row + SQUARE_SIZE / 2 #the center

    def mk_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE / 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y) radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y) radius)
        #black circle, smaller circle on the black one

    def __repr__(self):
        return (str(self.color))
