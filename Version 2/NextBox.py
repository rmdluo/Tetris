#!/usr/bin/env python

import pygame

class NextBox:
    def __init__(self, screen, WINDOW_WIDTH, WINDOW_HEIGHT, NUM_PREVIEW):
        self.pieces = []
        self.piece_list = []
        self.screen = screen
        self.NUM_PREVIEW = NUM_PREVIEW
        
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        self.box_width = 120
        self.box_height = 480

    def generate_pieces(self, pieces):
        self.piece_list = []

        I_PIECE = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        J_PIECE = [[2, 0, 0], [2, 2, 2], [0, 0, 0]]
        L_PIECE = [[0, 0, 3], [3, 3, 3], [0, 0, 0]]
        O_PIECE = [[0, 4, 4], [0, 4, 4], [0, 0, 0]]
        S_PIECE = [[0, 5, 5], [5, 5, 0], [0, 0, 0]]
        T_PIECE = [[0, 6, 0], [6, 6, 6], [0, 0, 0]]
        Z_PIECE = [[7, 7, 0], [0, 7, 7], [0, 0, 0]]
        
        for piece_index in range(self.NUM_PREVIEW):
            piece = pieces[piece_index]
            if(piece == "I"):
                self.piece_list.append(I_PIECE)
            elif(piece == "J"):
                self.piece_list.append(J_PIECE)
            elif(piece == "L"):
                self.piece_list.append(L_PIECE)
            elif(piece == "O"):
                self.piece_list.append(O_PIECE)
            elif(piece == "S"):
                self.piece_list.append(S_PIECE)
            elif(piece == "T"):
                self.piece_list.append(T_PIECE)
            elif(piece == "Z"):
                self.piece_list.append(Z_PIECE)

    def draw(self):
        self.x = 315
        self.y = 5

        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 90, 450))
        
        for piece in self.piece_list:
            for i in range(3):
                for j in range(3):
                    if(piece[i][j] == 0): #0 for nothing
                        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.x + j * 30, self.y + i * 30, 30, 30))
                    elif (piece[i][j] == 1): #1 for I piece
                        pygame.draw.rect(self.screen, (173, 216, 230), pygame.Rect(self.x + j * 30, self.y + i * 30, 30, 30))
                    elif (piece[i][j] == 2): #2 for J piece
                        pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(self.x + j * 30, self.y + i * 30, 30, 30))
                    elif (piece[i][j] == 3): #3 for L piece
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect(self.x + j * 30, self.y + i * 30, 30, 30))
                    elif(piece[i][j] == 4):
                        pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(self.x + j * 30, self.y + i * 30, 30, 30))
                    elif (piece[i][j] == 5): #5 for S piece
                        pygame.draw.rect(self.screen, (144,238,144), pygame.Rect(self.x + j * 30, self.y + i * 30, 30, 30))
                    elif (piece[i][j] == 6): #6 for T piece
                        pygame.draw.rect(self.screen, (138,43,226), pygame.Rect(self.x + j * 30, self.y + i * 30, 30, 30))
                    elif (piece[i][j] == 7): #7 for Z piece
                        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x + j * 30, self.y + i * 30, 30, 30))

            self.y += 95
