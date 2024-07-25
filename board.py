import numpy
import pygame

BOARD_COLOR = (246, 190, 0)
PLAYER1_COLOR = (139, 0, 0)
PLAYER2_COLOR = (0, 0, 139)
EMPTY_COLOR = (255, 255, 240)
MARGIN = 10
BOARD_WIDTH = 7 * 80
BOARD_HEIGHT = 8 * 80
RECTANGLE_WIDTH = 80
RECTANGLE_HEIGHT = 80
SMALL_CIRCLE_RADIUS = 30
boardSize = (BOARD_WIDTH, BOARD_HEIGHT)
window = pygame.display.set_mode(boardSize)

def setBoard(board):
    for c in range(7):
        for r in range(6):
            x = c * RECTANGLE_WIDTH + MARGIN
            y = r * RECTANGLE_HEIGHT + 80 + MARGIN
            pygame.draw.rect(window, BOARD_COLOR, (x, y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT))
            center_x = x + RECTANGLE_WIDTH // 2
            center_y = y + RECTANGLE_HEIGHT // 2

            if board[r][c] == 0:
                pygame.draw.circle(window, EMPTY_COLOR, (center_x, center_y), SMALL_CIRCLE_RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(window, PLAYER1_COLOR, (center_x, center_y), SMALL_CIRCLE_RADIUS)
            else:
                pygame.draw.circle(window, PLAYER2_COLOR, (center_x, center_y), SMALL_CIRCLE_RADIUS)

    pygame.display.update()

def initBoard():
    return numpy.zeros((6, 7), dtype=int)



