#as tutorials: https://www.pygame.org/wiki/tutorials
import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

FPS = 60

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  #WIN, in main() if not used again
pygame.display.set_caption("checkers")

board = Board()

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_squares(SCREEN)
        pygame.display.update()

    pygame.quit()
    #sis.exit()

main()