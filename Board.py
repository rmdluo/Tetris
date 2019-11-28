import pygame

class Board:
    def __init__(self, screen):
        self.current_piece = []
        self.center_x = 5
        self.center_y = 0

        self.I_PIECE =[[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.J_PIECE = [[2, 0, 0], [2, 2, 2], [0, 0, 0]]
        self.L_PIECE = [[0, 0, 3], [3, 3, 3], [0, 0, 0]]
        self.O_PIECE = [[4, 4], [4, 4]]
        self.S_PIECE = [[0, 5, 5], [5, 5, 0], [0, 0, 0]]
        self.T_PIECE = [[0, 6, 0], [6, 6, 6], [0, 0, 0]]
        self.Z_PIECE = [[7, 7, 0], [0, 7, 7], [0, 0, 0]]

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
                if(self.board[i][j] == 0): #0 for nothing
                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(j*30, i*30, 30, 30))
                elif (self.board[i][j] == 1): #1 for I piece
                    pygame.draw.rect(self.screen, (173, 216, 230), pygame.Rect(j*30, i*30, 30, 30))
                elif (self.board[i][j] == 2): #2 for J piece
                    pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(j*30, i*30, 30, 30))
                elif (self.board[i][j] == 3): #3 for L piece
                    pygame.draw.rect(self.screen, (255,165,0), pygame.Rect(j*30, i*30, 30, 30))
                elif (self.board[i][j] == 4): #4 for O piece
                    pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(j*30, i*30, 30, 30))
                elif (self.board[i][j] == 5): #5 for S piece
                    pygame.draw.rect(self.screen, (0, 100, 0), pygame.Rect(j*30, i*30, 30, 30))
                elif (self.board[i][j] == 6): #6 for T piece
                    pygame.draw.rect(self.screen, (50, 0, 100), pygame.Rect(j*30, i*30, 30, 30))
                else:
                    pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(j*30, i*30, 30, 30))
    
    def add_piece(self, piece):
        self.center_x = 5
        self.center_y = 0
            
        if(piece == "I"):
            self.current_piece = self.I_PIECE
        elif(piece == "J"):
            self.current_piece = self.J_PIECE
            self.center_y -= 1
        elif(piece == "L"):
            self.current_piece = self.L_PIECE
            self.center_y -= 1
        elif(piece == "O"):
            self.current_piece = self.O_PIECE
            self.center_y -= 1
        elif(piece == "S"):
            self.current_piece = self.S_PIECE
            self.center_y -= 1
        elif(piece == "T"):
            self.current_piece = self.T_PIECE
            self.center_y -= 1
        elif(piece == "Z"):
            self.current_piece = self.Z_PIECE
            self.center_y -= 1
        else:
            pass

        current_x = -1
        row_index = -1
        for row in self.current_piece:
            row_index += 1
            if(not self.is_zero_row(row)):
                current_x += 1
                column_index = 0
                for column in self.current_piece:
                    if(not self.center_y + current_x == -1):
                        self.board[self.center_y + current_x][self.center_x - len(row) // 2 + column_index] = self.current_piece[row_index][column_index]
                        column_index += 1
        
    def is_zero_row(self, row):
        for number in row:
            if (number != 0):
                return False
        return True

    def clear_piece(self):
        current_x = -1
        size = len(self.current_piece)
        for row_index in range(size):
            if(not self.is_zero_row(self.current_piece[row_index])):
                current_x += 1
                for column_index in range(size):
                    try:
                        self.board[self.center_y + current_x][self.center_x - size // 2 + column_index] = 0
                    except:
                        pass
    def place_piece(self):
        current_x = -1
        size = len(self.current_piece)
        for row_index in range(size):
            if(not self.is_zero_row(self.current_piece[row_index])):
                current_x += 1
                for column_index in range(size):
                    try:
                        self.board[self.center_y + current_x][self.center_x - size // 2 + column_index] = self.current_piece[row_index][column_index]
                    except:
                        pass
    def lower_piece(self):
        self.clear_piece()
        self.center_y += 1
        self.place_piece()

    def check_collision(self):
        pass

    def rotate_cw(self):
        self.clear_piece()

        N = len(self.current_piece[0]) 
        for i in range(N // 2): 
            for j in range(i, N - i - 1): 
                temp = self.current_piece[i][j] 
                self.current_piece[i][j] = self.current_piece[N - 1 - j][i] 
                self.current_piece[N - 1 - j][i] = self.current_piece[N - 1 - i][N - 1 - j] 
                self.current_piece[N - 1 - i][N - 1 - j] = self.current_piece[j][N - 1 - i] 
                self.current_piece[j][N - 1 - i] = temp 

        while(not self.center_x - (len(self.current_piece) - self.piece_left_side()) + 1 >= 0):
            self.right()
        
        self.place_piece()

    def rotate_ccw(self):
        self.rotate_cw()
        self.rotate_cw()
        self.rotate_cw()

    def right(self):
        if(self.center_x + (len(self.current_piece) - self.piece_right_side()) - 1 <= 10):
            self.clear_piece()
            self.center_x += 1
            self.place_piece()

    def left(self):
        if(self.center_x - (len(self.current_piece) - self.piece_left_side()) + 1 >= 0):
            self.clear_piece()
            self.center_x -= 1
            self.place_piece()

    def piece_left_side(self):
        leftmost = 0
        N = len(self.current_piece[0]) 
        for i in range(N // 2): 
            for j in range(i, N - i - 1): 
                temp = self.current_piece[i][j] 
                self.current_piece[i][j] = self.current_piece[N - 1 - j][i] 
                self.current_piece[N - 1 - j][i] = self.current_piece[N - 1 - i][N - 1 - j] 
                self.current_piece[N - 1 - i][N - 1 - j] = self.current_piece[j][N - 1 - i] 
                self.current_piece[j][N - 1 - i] = temp 

        row_index = -1
        for row in self.current_piece:
            row_index += 1
            if(self.is_zero_row(row)):
                leftmost = row_index + 1
            else:
                break
            
        for n in range(3):
            for i in range(N // 2): 
                for j in range(i, N - i - 1): 
                    temp = self.current_piece[i][j] 
                    self.current_piece[i][j] = self.current_piece[N - 1 - j][i] 
                    self.current_piece[N - 1 - j][i] = self.current_piece[N - 1 - i][N - 1 - j] 
                    self.current_piece[N - 1 - i][N - 1 - j] = self.current_piece[j][N - 1 - i] 
                    self.current_piece[j][N - 1 - i] = temp
        return leftmost

    def piece_right_side(self):
        rightmost = 0
        N = len(self.current_piece[0])

        for n in range(3):
            for i in range(N // 2): 
                for j in range(i, N - i - 1): 
                    temp = self.current_piece[i][j] 
                    self.current_piece[i][j] = self.current_piece[N - 1 - j][i] 
                    self.current_piece[N - 1 - j][i] = self.current_piece[N - 1 - i][N - 1 - j] 
                    self.current_piece[N - 1 - i][N - 1 - j] = self.current_piece[j][N - 1 - i] 
                    self.current_piece[j][N - 1 - i] = temp 

        row_index = -1
        for row in self.current_piece:
            row_index += 1
            if(self.is_zero_row(row)):
                rightmost = row_index + 1
            else:
                break
            
        for i in range(N // 2): 
            for j in range(i, N - i - 1): 
                temp = self.current_piece[i][j] 
                self.current_piece[i][j] = self.current_piece[N - 1 - j][i] 
                self.current_piece[N - 1 - j][i] = self.current_piece[N - 1 - i][N - 1 - j] 
                self.current_piece[N - 1 - i][N - 1 - j] = self.current_piece[j][N - 1 - i] 
                self.current_piece[j][N - 1 - i] = temp
        return rightmost

    def piece_bottom():
        pass

    def reach_bottom():
        pass
##        size = len(self.current_piece)
##        if(self.center_y + )
##        for column_index in range(size):
##            if()
            
