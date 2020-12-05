import numpy as np
import pygame
import math
ROWS = 6
COLUMNS = 7

board = np.zeros((ROWS, COLUMNS))

gameover = False
turn = 0

SLOT = 70
width = COLUMNS * SLOT
height = (ROWS+1)*SLOT
size = (width, height)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
WHITE = ((255, 255, 255))
OFFSET = 70

RADIUS = int(SLOT/2-5)
pygame.init()


def draw(board):

    for c in range(COLUMNS):
        for r in range(ROWS):
            c2 = (int(c*SLOT+SLOT/2), height-int(r*SLOT+SLOT/2))
            if board[r][c] == 1:
                pygame.draw.circle(window, RED, c2, RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(window, GREEN, c2, RADIUS)
            else:
                pygame.draw.circle(window, WHITE, c2, RADIUS)


def valid(board, col):
    return board[ROWS-1][col] == 0


def drop(board, col, piece):

    for r in range(ROWS):
        if board[r][col] == 0:
            board[r][col] = piece
            return


def win(board, piece):
    # horizontal
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # vertical
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # diagonal
    for c in range(COLUMNS-3):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # diagonal.1
    for c in range(COLUMNS-3):
        for r in range(3, ROWS-3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


print(board)


display_winner = False
winner = None

# Font to display winner
font = pygame.font.Font("Pixeboy.ttf", 32)

window = pygame.display.set_mode(size)
pygame.display.set_caption("connect 4")

# draw(board)
while not gameover:

    # Move events to the top of the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        #  need to check if the game is still going on by "not display_winner",
        # This is just to disable user input if we have a winner.
        if event.type == pygame.MOUSEBUTTONDOWN and not display_winner:
            posx = event.pos[0]
            col = math.floor(posx/SLOT)
            if valid(board, col):

                drop(board, col, (turn % 2)+1)
                # Move is played and then change the turn.
                if win(board, (turn % 2)+1):
                    print(f"player {(turn%2) + 1} won")
                    # If we have a winner the  variables are set
                    display_winner = True
                    winner = (turn % 2)+1
                turn = 1 if turn == 0 else 0

            print(np.flip(board, 0))


    pygame.draw.rect(window, (0, 0, 0), (0, 0, width, height))
  
    pygame.draw.rect(window, WHITE, (0, 0, width, SLOT))

    draw(board)

    # If we have a winner, 
    if display_winner:
        text = font.render(f'Player {winner} won!', True, BLUE)
        textRect = text.get_rect()
        textRect.center = (width // 2, SLOT // 2)
        window.blit(text, textRect)
        pygame.display.update()
        continue


 
    mouse_position = pygame.mouse.get_pos()
    # Get x, y position


    posx = SLOT//2 + SLOT * (mouse_position[0] // SLOT)
    # y is  SLOT // 2
    posy = SLOT//2

    # Display the preview
    if turn % 2 == 0:
        pygame.draw.circle(window, RED, (posx, posy), RADIUS)
    else:
        pygame.draw.circle(window, GREEN, (posx, posy), RADIUS)

    pygame.display.update()

pygame.quit()
