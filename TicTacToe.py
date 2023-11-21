import pygame, sys
import numpy as np

pygame.init()

width = 600
height = 600
line_widht = 15
board_rows = 3
board_cols = 3
#cores
red = (255, 0, 0)
bg_color = (250, 250, 250)
linesColor = (230, 230, 230)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(bg_color)

#borda
board = np.zeros((board_rows, board_cols))
#print(board)

#linhas

def draw_lines():
    #linhaHorizontal 1
    pygame.draw.line( screen, linesColor, (0, 200), (600, 200), line_widht)
    #linhaHorizontal 2
    pygame.draw.line( screen, linesColor, (0, 400), (600, 400), line_widht)
    #linhaVertical 1
    pygame.draw.line( screen, linesColor, (200, 0), (200, 600), line_widht)
    #linhaVerticail 2
    pygame.draw.line( screen, linesColor, (400, 0), (400, 600), line_widht)

def mark_square(row, col, player):
    board[row] [col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
            
    return True

print(is_board_full())
for row in range(board_rows):
        for col in range(board_cols):
            mark_square(row, col, 1)

# board is full - true
print(is_board_full())

draw_lines()

#intinity loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()