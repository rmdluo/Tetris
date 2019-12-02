#!/usr/bin/env python

import pygame

class Board:
    def __init__(self, screen, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.current_piece = []
        self.piece_type = ""
        self.x = 5
        self.y = 0
        #self.bottom_edge = 0
        self.size = 0

        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.PIECE_SIZE = WINDOW_WIDTH / 10 #* 3 / 40
        
        self.board = []
        for i in range(20):
            new_row = []
            for j in range(10):
                new_row.append(0)
            self.board.append(new_row)

        self.screen = screen
        
    def draw(self):
        for i in range(20):
            for j in range(10):
                if(self.board[i][j] % 10 == 0): #0 for nothing
                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(j*self.PIECE_SIZE, i*self.PIECE_SIZE, self.PIECE_SIZE, self.PIECE_SIZE))
                elif (self.board[i][j] % 10 == 1): #1 for I piece
                    pygame.draw.rect(self.screen, (173, 216, 230), pygame.Rect(j*self.PIECE_SIZE, i*self.PIECE_SIZE, self.PIECE_SIZE, self.PIECE_SIZE))
                elif (self.board[i][j] % 10 == 2): #2 for J piece
                    pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(j*self.PIECE_SIZE, i*self.PIECE_SIZE, self.PIECE_SIZE, self.PIECE_SIZE))
                elif (self.board[i][j] % 10 == 3): #3 for L piece
                    pygame.draw.rect(self.screen, (255,165,0), pygame.Rect(j*self.PIECE_SIZE, i*self.PIECE_SIZE, self.PIECE_SIZE, self.PIECE_SIZE))
                elif (self.board[i][j] % 10 == 4): #4 for O piece
                    pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(j*self.PIECE_SIZE, i*self.PIECE_SIZE, self.PIECE_SIZE, self.PIECE_SIZE))
                elif (self.board[i][j] % 10 == 5): #5 for S piece
                    pygame.draw.rect(self.screen, (144,238,144), pygame.Rect(j*self.PIECE_SIZE, i*self.PIECE_SIZE, self.PIECE_SIZE, self.PIECE_SIZE))
                elif (self.board[i][j] % 10 == 6): #6 for T piece
                    pygame.draw.rect(self.screen, (138,43,226), pygame.Rect(j*self.PIECE_SIZE, i*self.PIECE_SIZE, self.PIECE_SIZE, self.PIECE_SIZE))
                elif (self.board[i][j] % 10 == 7): #7 for Z piece
                    pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(j*self.PIECE_SIZE, i*self.PIECE_SIZE, self.PIECE_SIZE, self.PIECE_SIZE))

    def add_piece(self, piece):
        for row_index in range(20):
                for column_index in range(10):
                    if(self.board[row_index][column_index] > 0 and self.board[row_index][column_index] < 80):
                        self.board[row_index][column_index] += 80
        
        self.y = 0
        self.bottom_edge = 1
        self.size = 3
        self.piece_type = piece

        I_PIECE = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
        J_PIECE = [[2, 0, 0], [2, 2, 2], [0, 0, 0]]
        L_PIECE = [[0, 0, 3], [3, 3, 3], [0, 0, 0]]
        O_PIECE = [[4, 4], [4, 4]]
        S_PIECE = [[0, 5, 5], [5, 5, 0], [0, 0, 0]]
        T_PIECE = [[0, 6, 0], [6, 6, 6], [0, 0, 0]]
        Z_PIECE = [[7, 7, 0], [0, 7, 7], [0, 0, 0]]
        
        if(piece == "I"):
            self.current_piece = I_PIECE
            self.x = 3
            self.size = 4
            self.y -= 1
        elif(piece == "J"):
            self.current_piece = J_PIECE
            self.y -= 1
            self.x = 4
        elif(piece == "L"):
            self.current_piece = L_PIECE
            self.x = 4
            self.y -= 1
        elif(piece == "O"):
            self.current_piece = O_PIECE
            self.x = 4
            self.y -= 1
            self.size = 2
        elif(piece == "S"):
            self.current_piece = S_PIECE
            self.x = 4
            self.y -= 1
        elif(piece == "T"):
            self.current_piece = T_PIECE
            self.x = 4
            self.y -= 1
        elif(piece == "Z"):
            self.current_piece = Z_PIECE
            self.x = 4
            self.y -= 1
        else:
            pass

        self.place_piece()
        
    def is_zero_row(self, row):
        for number in row:
            if (number != 0):
                return False
        return True

    def clear_piece(self):
        for row_index in range(self.size):
            for column_index in range(self.size):
                    if(self.y + row_index >= 0 and self.current_piece[row_index][column_index] != 0):
                        self.board[self.y + row_index][self.x + column_index] = 0

    def place_piece(self):
        current_x = -1
        for row_index in range(self.size):
            current_x += 1
            for column_index in range(self.size):
                if(self.y + current_x >= 0 and self.current_piece[row_index][column_index] != 0):
                    self.board[self.y + current_x][self.x + column_index] = self.current_piece[row_index][column_index]
                    
    def lower_piece(self):
        if(not self.reach_bottom()):
            self.clear_piece()
            self.y += 1
            self.place_piece()

    def rotate_cw(self):
        switch = True
        
        self.clear_piece()

        temp_piece = []

        for row in self.current_piece:
            temp_piece.append(row.copy())

        for i in range(self.size // 2): 
            for j in range(i, self.size - i - 1): 
                temp = temp_piece[i][j] 
                temp_piece[i][j] = temp_piece[self.size - 1 - j][i] 
                temp_piece[self.size - 1 - j][i] = temp_piece[self.size - 1 - i][self.size - 1 - j] 
                temp_piece[self.size - 1 - i][self.size - 1 - j] = temp_piece[j][self.size - 1 - i] 
                temp_piece[j][self.size - 1 - i] = temp 

        temp_x = self.x
        temp_y = self.y
        
        if(temp_x < 0):
            temp_x = 0
        elif(temp_x + self.size > 10):
            temp_x = 10 - self.size
        if(self.y + self.size > 20):
            temp_y = 20 - self.size
        
        for row_index in range(self.size):
            for column_index in range(self.size):
                if(temp_y + row_index < 20 and temp_x >= 0 and temp_x + column_index <= 9):
                    if(self.board[temp_y + row_index][temp_x + column_index] != 0 and self.board[temp_y + row_index][temp_x + column_index] != temp_piece[row_index][column_index] and temp_piece[row_index][column_index] != 0):
                        switch = False
        
        if(switch):
            self.x = temp_x
            self_y = temp_y
            self.current_piece = temp_piece.copy()

        self.place_piece()

    def rotate_ccw(self):
        self.rotate_cw()
        self.rotate_cw()
        self.rotate_cw()

    def right(self):
        if(self.x + self.size + 1 - self.piece_right_side() <= 10 and not self.test_collision_right()):
            self.clear_piece()
            self.x += 1
            self.place_piece()

    def left(self):
        if(self.x + self.piece_left_side() - 1 >= 0 and not self.test_collision_left()):
            self.clear_piece()
            self.x -= 1
            self.place_piece()

    def piece_left_side(self):
        leftmost = 0
        for i in range(self.size // 2): 
            for j in range(i, self.size - i - 1): 
                temp = self.current_piece[i][j] 
                self.current_piece[i][j] = self.current_piece[self.size - 1 - j][i] 
                self.current_piece[self.size - 1 - j][i] = self.current_piece[self.size - 1 - i][self.size - 1 - j] 
                self.current_piece[self.size - 1 - i][self.size - 1 - j] = self.current_piece[j][self.size - 1 - i] 
                self.current_piece[j][self.size - 1 - i] = temp 

        row_index = -1
        for row in self.current_piece:
            row_index += 1
            if(self.is_zero_row(row)):
                leftmost = row_index + 1
            else:
                break
            
        for n in range(3):
            for i in range(self.size // 2): 
                for j in range(i, self.size - i - 1): 
                    temp = self.current_piece[i][j] 
                    self.current_piece[i][j] = self.current_piece[self.size - 1 - j][i] 
                    self.current_piece[self.size - 1 - j][i] = self.current_piece[self.size - 1 - i][self.size - 1 - j] 
                    self.current_piece[self.size - 1 - i][self.size - 1 - j] = self.current_piece[j][self.size - 1 - i] 
                    self.current_piece[j][self.size - 1 - i] = temp
        return leftmost

    def piece_right_side(self):
        rightmost = 0

        for n in range(3):
            for i in range(self.size // 2): 
                for j in range(i, self.size - i - 1): 
                    temp = self.current_piece[i][j] 
                    self.current_piece[i][j] = self.current_piece[self.size - 1 - j][i] 
                    self.current_piece[self.size - 1 - j][i] = self.current_piece[self.size - 1 - i][self.size - 1 - j] 
                    self.current_piece[self.size - 1 - i][self.size - 1 - j] = self.current_piece[j][self.size - 1 - i] 
                    self.current_piece[j][self.size - 1 - i] = temp 

        row_index = -1
        for row in self.current_piece:
            row_index += 1
            if(self.is_zero_row(row)):
                rightmost = row_index + 1
            else:
                break
            
        for i in range(self.size // 2): 
            for j in range(i, self.size - i - 1): 
                temp = self.current_piece[i][j] 
                self.current_piece[i][j] = self.current_piece[self.size - 1 - j][i] 
                self.current_piece[self.size - 1 - j][i] = self.current_piece[self.size - 1 - i][self.size - 1 - j] 
                self.current_piece[self.size - 1 - i][self.size - 1 - j] = self.current_piece[j][self.size - 1 - i] 
                self.current_piece[j][self.size - 1 - i] = temp
        return rightmost

    def last_row(self):
        row_index = 0
        count = -1
        for row in self.current_piece:
            count += 1
            if(not self.is_zero_row(row)):
                row_index = count 
        
        return row_index

    def first_row(self):
        count = -1
        for row in self.current_piece:
            count += 1
            if(not self.is_zero_row(row)):
                return count 
        

    def reach_bottom(self):
        if(self.piece_type == "I"):
            if(self.y + self.last_row() >= 19):
                return True
        
        if(self.y + self.last_row() >= 19):
            return True

        return self.test_collision_below()
        
        return False

    def test_collision_below(self):
        for column_index in range(self.size):
            for row_index in range(self.size):
                try:
                    if(self.current_piece[row_index][column_index] != 0 and self.current_piece[row_index][column_index] != self.board[self.y + row_index + 1][self.x + column_index] and self.board[self.y + row_index + 1][self.x + column_index] != 0):
                        return True
                except:
                    pass
        return False

    def test_collision_left(self):
        for row_index in range(self.size):
            for column_index in range(self.size):
                if(self.current_piece[row_index][column_index] != 0 and self.current_piece[row_index][column_index] != self.board[self.y + row_index][self.x + column_index - 1] and self.board[self.y + row_index][self.x + column_index - 1] != 0):
                    return True
        return False

    def test_collision_right(self):
        for row_index in range(self.size):
            for column_index in range(self.size):
                if(self.current_piece[row_index][column_index] != 0 and self.current_piece[row_index][column_index] != self.board[self.y + row_index][self.x + column_index + 1] and self.board[self.y + row_index][self.x + column_index + 1] != 0):
                    return True
        return False

    def is_row_full(self, row):
        for number in row:
            if(number == 0):
                return False
        return True

    def clear_lines(self):
        for row_index in range(20):
            if(self.is_row_full(self.board[row_index])):
                for index in range(row_index):
                    self.board[row_index - index] = self.board[row_index - index - 1].copy()
        self.board[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def check_loss(self):
        if(self.y < 0):
            return True
        return False      
