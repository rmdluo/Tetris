#!/usr/bin/env python

import pygame

class HoldBox:
    def __init__(self, screen, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.piece = ""
        self.current_piece = []
        self.screen = screen

        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        
        pygame.draw.line(screen, (255, 255, 255), (300, 480), (420, 480))      

    def generate_piece(self, piece):
        self.piece = piece
        
        I_PIECE = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        J_PIECE = [[2, 0, 0], [2, 2, 2], [0, 0, 0]]
        L_PIECE = [[0, 0, 3], [3, 3, 3], [0, 0, 0]]
        O_PIECE = [[4, 4], [4, 4]]
        S_PIECE = [[0, 5, 5], [5, 5, 0], [0, 0, 0]]
        T_PIECE = [[0, 6, 0], [6, 6, 6], [0, 0, 0]]
        Z_PIECE = [[7, 7, 0], [0, 7, 7], [0, 0, 0]]
        
        if(piece == "I"):
            self.current_piece = I_PIECE
        elif(piece == "J"):
            self.current_piece = J_PIECE
        elif(piece == "L"):
            self.current_piece = L_PIECE
        elif(piece == "O"):
            self.current_piece = O_PIECE
        elif(piece == "S"):
            self.current_piece = S_PIECE
        elif(piece == "T"):
            self.current_piece = T_PIECE
        elif(piece == "Z"):
            self.current_piece = Z_PIECE

    def draw(self):
        if(self.piece == "O"):
            pygame.draw.rect(self.screen, (0, 0, 0), (300, 480, 120, 120))
            pygame.draw.rect(self.screen, (255, 255, 0), (330, 510, 60, 60))
        elif(self.piece != ""):
            for i in range(3):
                for j in range(3):
                    if(self.current_piece[i][j] == 0): #0 for nothing
                        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(300 + j*40, 480 + i*40, 40, 40))
                    elif (self.current_piece[i][j] == 1): #1 for I piece
                        pygame.draw.rect(self.screen, (173, 216, 230), pygame.Rect(300 + j*40, 480 + i*40, 40, 40))
                    elif (self.current_piece[i][j] == 2): #2 for J piece
                        pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(300 + j*40, 480 + i*40, 40, 40))
                    elif (self.current_piece[i][j] == 3): #3 for L piece
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect(300 + j*40, 480 + i*40, 40, 40))
                    elif (self.current_piece[i][j] == 5): #5 for S piece
                        pygame.draw.rect(self.screen, (144,238,144), pygame.Rect(300 + j*40, 480 + i*40, 40, 40))
                    elif (self.current_piece[i][j] == 6): #6 for T piece
                        pygame.draw.rect(self.screen, (138,43,226), pygame.Rect(300 + j*40, 480 + i*40, 40, 40))
                    elif (self.current_piece[i][j] == 7): #7 for Z piece
                        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(300 + j*40, 480 + i*40, 40, 40))

        pygame.draw.line(self.screen, (255, 255, 255), (300, 480), (420, 480))      
        pygame.draw.line(self.screen, (255, 255, 255), (300, 0), (300, 600))
