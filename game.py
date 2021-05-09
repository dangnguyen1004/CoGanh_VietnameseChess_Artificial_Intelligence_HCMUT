import pygame
import math


# =================== Setting size of game ==============
WIDTH = 600
MARGIN = 50
ROWS = 5
COLS = 5
ROWWIDTH = WIDTH // (ROWS - 1)
RADIUS = 20
OUTLINE = 4
FPS = 60
CASEOF4 = [(0,1), (0,3), (1,0), (1,4), (3,0), (3,4), (4,1), (4,3), (1,2), (2,1), (2,3), (3,2)] # Positions which have maximun 4 moves



# ===== Set up display to visualize pathfinding =====
WIN = pygame.display.set_mode((WIDTH + MARGIN * 2, WIDTH + MARGIN * 2))
pygame.display.set_caption("Co ganh")



#  ================== Setting color  =====================
ORANGE = (255, 165, 0)          # 
TURQUOISE = (64, 224, 208)      # 
WHITE = (255, 255, 255)         # 
BLACK = (0, 0, 0)               # 
RED = (255, 0, 0)               # Red piece
PURPLE = (128, 0, 128)          #
GREEN = (0, 255, 0)             # 
GREY = (128, 128, 128)          # Gridline color
YELLOW = (255, 255, 0)          # Legal move
BLUE = (0, 255, 0)              # Blue piece



class Piece():
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.calculatePosition()
        self.selected = False
    
    def calculatePosition(self):
        self.x = MARGIN + self.col * ROWWIDTH
        self.y = MARGIN + self.row * ROWWIDTH

    def draw(self):
        if self.selected:
            pygame.draw.circle(WIN, PURPLE, (self.x, self.y), RADIUS + OUTLINE)
        else:
            pygame.draw.circle(WIN, GREY, (self.x, self.y), RADIUS + OUTLINE)
        pygame.draw.circle(WIN, self.color, (self.x, self.y), RADIUS)  
    
    def changeColor(self):
        self.color = RED if self.color == BLUE else BLUE
        
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculatePosition()

    def __repr__(self):
        return str(self.color)



class Board:
    def __init__(self):
        self.board = []
        self.redLeft = 8
        self.blueLeft = 8

        self.createBoard()

    def createBoard(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 0:
                    self.board[row].append(Piece(row, col, RED))
                elif row == 1 and (col == 0 or col == COLS - 1):
                    self.board[row].append(Piece(row, col, RED))
                elif row == 2 and col == COLS - 1:
                    self.board[row].append(Piece(row, col, RED))
                elif row == 2 and col == 0:
                    self.board[row].append(Piece(row, col, BLUE))
                elif row == ROWS - 2 and (col == 0 or col == COLS - 1):
                    self.board[row].append(Piece(row, col, BLUE))
                elif row == ROWS - 1:
                    self.board[row].append(Piece(row, col, BLUE))
                else:
                    self.board[row].append(0)

    def draw(self):
        self.drawGridLine()
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw()
    
    def getPiece(self, row, col):
        return self.board[row][col]
    
    def move(self, piece, row, col):
        # swap data in self.board
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def getValidMoves(self, piece):
        moves = []
        row = piece.row
        col = piece.col

        # check 8 directions
        if row - 1 >= 0:
            if self.board[row - 1][col] == 0:
                moves.append((row - 1, col))
        if row + 1 < ROWS:
            if self.board[row + 1][col] == 0:
                moves.append((row + 1, col))
        if col - 1 >= 0:
            if self.board[row][col -1] == 0:
                moves.append((row, col - 1))
        if col + 1 < COLS:
            if self.board[row][col + 1] == 0:
                moves.append((row, col + 1))
        if (row, col) not in CASEOF4:
            if row - 1 >= 0 and col - 1 >= 0:
                if self.board[row - 1][col - 1] == 0:
                    moves.append((row - 1, col - 1))
            if row - 1 >= 0 and col + 1 < COLS:
                if self.board[row - 1][col + 1] == 0:
                    moves.append((row - 1, col + 1))
            if row + 1 < ROWS and col - 1 >= 0:
                if self.board[row + 1][col - 1] == 0:
                    moves.append((row + 1, col - 1))
            if row + 1 < ROWS and col + 1 < COLS:
                if self.board[row + 1][col + 1] == 0:
                    moves.append((row + 1, col + 1))

        return moves



    def drawGridLine(self):
        # draw vertical and horizontal line
        for i in range(ROWS):
            pygame.draw.line(WIN, GREY, (0 + MARGIN, i * ROWWIDTH + MARGIN), (WIDTH + MARGIN, i * ROWWIDTH + MARGIN))
        for i in range(ROWS):
            pygame.draw.line(WIN, GREY, (i * ROWWIDTH + MARGIN, 0 + MARGIN), (i * ROWWIDTH + MARGIN, WIDTH + MARGIN))    
        # draw diagonal 
        pygame.draw.line(WIN, GREY, (MARGIN, MARGIN), (MARGIN + ROWWIDTH * 2, MARGIN + ROWWIDTH * 2))    
        pygame.draw.line(WIN, GREY, (MARGIN + ROWWIDTH * 2, MARGIN), (MARGIN + ROWWIDTH * 4, MARGIN + ROWWIDTH * 2))    
        pygame.draw.line(WIN, GREY, (MARGIN, MARGIN + ROWWIDTH * 2), (MARGIN + ROWWIDTH * 2, MARGIN))    
        pygame.draw.line(WIN, GREY, (MARGIN + ROWWIDTH * 2, MARGIN + ROWWIDTH * 2), (MARGIN + ROWWIDTH * 4, MARGIN))    

        pygame.draw.line(WIN, GREY, (MARGIN, MARGIN + ROWWIDTH * 2), (MARGIN + ROWWIDTH * 2, MARGIN + ROWWIDTH * 4))    
        pygame.draw.line(WIN, GREY, (MARGIN + ROWWIDTH * 2, MARGIN + ROWWIDTH * 2), (MARGIN + ROWWIDTH * 4, MARGIN + ROWWIDTH * 4))    
        pygame.draw.line(WIN, GREY, (MARGIN, MARGIN + ROWWIDTH * 4), (MARGIN + ROWWIDTH * 2, MARGIN + ROWWIDTH * 2))    
        pygame.draw.line(WIN, GREY, (MARGIN + ROWWIDTH * 2, MARGIN + ROWWIDTH * 4), (MARGIN + ROWWIDTH * 4, MARGIN + ROWWIDTH * 2))    





class Game:
    def _init(self):
        self.board = Board()
        self.selected = None
        self.turn = BLUE
        self.validMoves = []

    def __init__(self):
        self._init()

    def resetGame(self):
        self._init()

    def update(self):
        WIN.fill(WHITE)
        self.board.draw()
        self.drawValidMoves()
        pygame.display.update()

    def changeTurn(self):
        self.turn = RED if self.turn == BLUE else BLUE

    def drawValidMoves(self):
        if not self.validMoves:
            return
        for move in self.validMoves:
            row, col = move
            pygame.draw.circle(WIN, YELLOW, (MARGIN + col * ROWWIDTH, MARGIN + row * ROWWIDTH), 15)

    def select(self, row, col):
        piece = self.board.getPiece(row, col)
        inLstValidMoves = True if (row, col) in self.validMoves else False
        if self.selected:
            if piece == 0 and inLstValidMoves:
                # ============ MOVE ==================
                self.board.move(self.selected, row, col)
                self.selected.selected = False
                self.selected = None
                self.validMoves = []
                self.checkSkip(row, col)                
                self.changeTurn()
                return
            elif piece != 0:
                # =========== SELECT ONTHER PIECE ==========
                self.selected.selected = False
                self.selected = None
                self.select(row, col)
                return
        else:
            # ========= CHOOSE A PIECE =============
            if piece != 0:
                if piece.color == self.turn:
                    piece.selected = True
                    self.selected = piece
                    self.validMoves = self.board.getValidMoves(piece)
                else:
                    return
            else:
                return
            
    def checkSkip(self, row, col):
        opponent = RED if self.turn == BLUE else BLUE

        if col - 1 >= 0 and col + 1 < COLS:
            leftPiece = self.board.getPiece(row, col - 1)
            rightPiece = self.board.getPiece(row, col + 1)
            # ====== Nuoc di ganh ===========
            if leftPiece != 0 and rightPiece != 0 and leftPiece.color == rightPiece.color == opponent:
                self.skip(leftPiece)
                self.skip(rightPiece)
            # ======== Nuoc di vay ===========

                
        if row - 1 >= 0 and row + 1 < ROWS:
            topPiece = self.board.getPiece(row - 1, col)
            botPiece = self.board.getPiece(row + 1, col)
            # ====== Nuoc di ganh ===========
            if topPiece != 0 and botPiece != 0 and topPiece.color == botPiece.color == opponent:
                self.skip(topPiece)
                self.skip(botPiece)
            # ======== Nuoc di vay ===========


        if (row, col) not in CASEOF4:
            if row - 1 >= 0 and col - 1 >= 0 and row + 1 < ROWS and col + 1 < COLS:
                topLeftPiece = self.board.getPiece(row - 1, col -1)
                botRightPiece = self.board.getPiece(row + 1, col + 1)
                # ====== Nuoc di ganh ===========
                if topLeftPiece != 0 and botRightPiece != 0 and topLeftPiece.color == botRightPiece.color == opponent:
                    self.skip(topLeftPiece)
                    self.skip(botRightPiece)
                # ======== Nuoc di vay ===========
   
                
            if row - 1 >= 0 and col + 1 < COLS and row + 1 < ROWS and col - 1 >= 0:
                topRightPiece = self.board.getPiece(row - 1, col + 1)
                botLeftPiece = self.board.getPiece(row + 1, col - 1)
                # ====== Nuoc di ganh ===========
                if topRightPiece != 0 and botLeftPiece != 0 and topRightPiece.color == botLeftPiece.color == opponent:
                    self.skip(topRightPiece)
                    self.skip(botLeftPiece)
                # ======== Nuoc di vay ===========

                
    def skip(self, piece):
        if piece.color == RED:
            self.board.redLeft -= 1
        else:
            self.board.blueLeft -= 1
        piece.changeColor()
        
        



def getRowColFromMouse(pos):
    x, y = pos
    row = (y - MARGIN // 2) // ROWWIDTH
    col = (x - MARGIN // 2) // ROWWIDTH 
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game()


    while run:
        clock.tick(FPS)

        #======================  For debug ===================================== 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = getRowColFromMouse(pos)
                game.select(row, col)
            
        game.update()

    pygame.quit()

main()
    
