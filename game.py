import pygame
import math


# =================== Setting size of game ==============
WIDTH = 600
MARGIN = 50
NUMBEROFROWS = 5

# ===== Set up display to visualize pathfinding =====
WIN = pygame.display.set_mode((WIDTH + MARGIN * 2, WIDTH + MARGIN * 2))
pygame.display.set_caption("Co ganh")

#  ================== Setting color  =====================
ORANGE = (255, 165, 0)          # Start node
TURQUOISE = (64, 224, 208)      # End Node
WHITE = (255, 255, 255)         # Not visited
BLACK = (0, 0, 0)               # Wall, cannot visit
RED = (255, 0, 0)               # Been visited
PURPLE = (128, 0, 128)          # Path node
GREEN = (0, 255, 0)             # Node in open set
GREY = (128, 128, 128)          # Gridline color
YELLOW = (255, 255, 0)
BLUE = (0, 255, 0)


class Position():
    def __init__(self):
        self.color = None
        self.row = None
        self.col = None
        self.x = None
        self.y = None

def drawGridLine():
    widthOfRow = WIDTH // (NUMBEROFROWS - 1)
    # draw vertical and horizontal line
    for i in range(NUMBEROFROWS):
        pygame.draw.line(WIN, GREY, (0 + MARGIN, i * widthOfRow + MARGIN), (WIDTH + MARGIN, i * widthOfRow + MARGIN))
    for i in range(NUMBEROFROWS):
        pygame.draw.line(WIN, GREY, (i * widthOfRow + MARGIN, 0 + MARGIN), (i * widthOfRow + MARGIN, WIDTH + MARGIN))    
    # draw duong cheo
    pygame.draw.line(WIN, GREY, (MARGIN, MARGIN), (MARGIN + widthOfRow * 2, MARGIN + widthOfRow * 2))    
    pygame.draw.line(WIN, GREY, (MARGIN + widthOfRow * 2, MARGIN), (MARGIN + widthOfRow * 4, MARGIN + widthOfRow * 2))    
    pygame.draw.line(WIN, GREY, (MARGIN, MARGIN + widthOfRow * 2), (MARGIN + widthOfRow * 2, MARGIN))    
    pygame.draw.line(WIN, GREY, (MARGIN + widthOfRow * 2, MARGIN + widthOfRow * 2), (MARGIN + widthOfRow * 4, MARGIN))    

    pygame.draw.line(WIN, GREY, (MARGIN, MARGIN + widthOfRow * 2), (MARGIN + widthOfRow * 2, MARGIN + widthOfRow * 4))    
    pygame.draw.line(WIN, GREY, (MARGIN + widthOfRow * 2, MARGIN + widthOfRow * 2), (MARGIN + widthOfRow * 4, MARGIN + widthOfRow * 4))    
    pygame.draw.line(WIN, GREY, (MARGIN, MARGIN + widthOfRow * 4), (MARGIN + widthOfRow * 2, MARGIN + widthOfRow * 2))    
    pygame.draw.line(WIN, GREY, (MARGIN + widthOfRow * 2, MARGIN + widthOfRow * 4), (MARGIN + widthOfRow * 4, MARGIN + widthOfRow * 2))    

def draw():
    WIN.fill(WHITE)
    drawGridLine()
    pygame.display.update()

def main():
    run = True
    while run:
        draw()

main()
