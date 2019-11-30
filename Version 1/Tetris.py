import pygame
from random import randint
from Board import *
import sys

pygame.init()
screen = pygame.display.set_mode((300, 600))
board = Board(screen)
board.draw()

done = False

count = 0
pieces = {1:"I", 2:"J", 3:"L", 4:"O", 5:"S", 6:"T", 7:"Z"}
board.add_piece(pieces[randint(1, 7)])
left_pressed = 0
while not done:
    count += 1

    left_done = False
    right_done = False
    
    if(count >= 10 and not board.reach_bottom()):
        count = 0
        board.lower_piece()   
            
    if(board.reach_bottom() and count >= 20):
        count = 0
        board.clear_lines()
        if(board.check_loss()):
            pygame.quit()
            sys.exit()
        board.add_piece(pieces[randint(1, 7)])
    
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            board.rotate_cw()
        elif(event.type == pygame.KEYDOWN and event.key == pygame.K_z):
            board.rotate_ccw()
        elif(event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            board.left()
            #left_pressed += 1
            left_done = True
        #elif(event.type == pygame.KEYUP and event.key == pygame.K_LEFT):
            #left_pressed = 0
        elif(event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            board.right()
            right_done = True

        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    pygame.key.set_repeat(1000)
    if(keys[pygame.K_DOWN]):
        count += 10
    if(keys[pygame.K_LEFT] and not left_done and count % 5 == 0):
        board.left()
    if(keys[pygame.K_RIGHT] and not right_done and count % 5 == 0):
        board.right()
     
    board.draw()
    pygame.display.flip()
