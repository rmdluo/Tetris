import pygame
from Board import *



pygame.init()
screen = pygame.display.set_mode((300, 600))
board = Board(screen)
board.draw()

done = False

count = 0
current_x = 5
current_y = 0
current_piece = "I"
board.add_piece(current_piece)
while not done:
    count += 1
    
    if(count == 1000):
        count = 0
        board.lower_piece()
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            board.rotate_cw()
        elif(event.type == pygame.KEYDOWN and event.key == pygame.K_z):
            board.rotate_ccw()
        elif(event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            board.left()
        elif(event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            board.right()
    board.draw()
    pygame.display.flip()
