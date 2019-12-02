#!/usr/bin/env python

"""Main class of Tetris - everything runs from here."""

from random import randint
import sys

import pygame

from Board import *
from HoldBox import *
from NextBox import *

def refill_pieces():
    """
    This method refills the next_pieces list.
    If you want to change the piece generation, this is where to do it.
    
    """
    while(len(next_pieces) < num_pieces * 2): # refill the list until it is 2 times the number of desired pieces
        for piece in range(num_pieces): # loop to make the pieces
            next_pieces.append(pieces[randint(1, 7)]) # add the piece to the list

pieces = {1:"I", 2:"J", 3:"L", 4:"O", 5:"S", 6:"T", 7:"Z"}


# set up the main pygame window
pygame.init()
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH + 120, WINDOW_HEIGHT))
board = Board(screen, WINDOW_WIDTH, WINDOW_HEIGHT)
pygame.draw.line(screen, (255, 255, 255), (300, 0), (300, WINDOW_HEIGHT))
board.draw()

# set up the hold box
hold_box = HoldBox(screen, WINDOW_WIDTH, WINDOW_HEIGHT)
hold_box.draw()

# set up the piece preview
next_box = NextBox(screen, WINDOW_WIDTH, WINDOW_HEIGHT, 5)

# set up the initial pieces
num_pieces = 7
board.add_piece(pieces[randint(1, 7)])
next_pieces = []
refill_pieces()
next_box.generate_pieces(next_pieces)
next_box.draw()

# set up some hold box variables
can_hold = True
hold_piece = ""
held_left = 0

# set up some extra variables
done = False
count = 0

# main game loop
while not done:
    # increment count
    count += 1

    # reset variables
    left_done = False
    right_done = False

    # lower the piece down one level
    if(count >= 10 and not board.reach_bottom()):
        count = 0
        board.lower_piece()   

    # check if the piece has reached the bottom
    if(board.reach_bottom() and count >= 20):
        # reset the count
        count = 0

        # clear any completed lines
        board.clear_lines()

        # close the game if the player has lost the game
        if(board.check_loss()):
            pygame.quit()
            sys.exit()

        
        if(len(next_pieces) == num_pieces):
                    refill_pieces()
        board.add_piece(next_pieces.pop(0))
        next_box.generate_pieces(next_pieces)
        next_box.draw()
          
        can_hold = True
    
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            board.rotate_cw()
        elif(event.type == pygame.KEYDOWN and event.key == pygame.K_z):
            board.rotate_ccw()
        elif(event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            board.left()
            held_left = 0
            left_done = True
        elif(event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            board.right()
            held_right = 0
            right_done = True
        elif(event.type == pygame.KEYDOWN and event.key == pygame.K_c and can_hold):
            if(hold_piece == ""):
                hold_piece = board.piece_type
                board.clear_piece()
                board.add_piece(next_pieces.pop(0))
                    
                hold_box.generate_piece(hold_piece)
                hold_box.draw()
                #draw_hold_box(screen, hold_piece)
            else:
                board.clear_piece()
                temp_piece = hold_piece
                hold_piece = board.piece_type
                board.add_piece(temp_piece)
                hold_box.generate_piece(hold_piece)
                hold_box.draw()

            can_hold = False

    
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_DOWN]):
        count += 10
    if(keys[pygame.K_LEFT] and not left_done):
        held_left += 1
        if(held_left >= 3):
            if(held_left == 6):
                board.left()
                held_left = 5
    if(keys[pygame.K_RIGHT] and not right_done):
        held_right += 1
        if(held_right >= 3):
            if(held_right == 6):
                board.right()
                held_right = 5
     
    board.draw()
    pygame.display.flip()

__author__ = "Raymond Luo"
__credits__ = ["Raymond Luo"]

__version__ = "2.0.0"
__maintainer__ = "Raymond Luo"
__email__ = "rmdluo@gmail.com"
__status__ = "Production"
