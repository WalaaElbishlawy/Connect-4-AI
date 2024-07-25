from board import *
import utilities
import StartMenu
import sys
import time
# for generating random values, for example for 1st turn
import random
algorithmToUse,difficulty = StartMenu.StartMenu()

# Customizable UI elements
BACKGROUND_COLOR = (255, 255, 255)
FONT_NAME = "segoe-ui"
FONT_SIZE = 40
FONT_COLOR = (0, 0, 0)
WINDOW_WIDTH = 580
WINDOW_HEIGHT = 600
FONT_POSITION = (40, 10)

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Connect 4 AI -- 20200425-20201120-20201217-20201043-20200442")  # put your ids
board = initBoard()
turn = 1
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
setBoard(board)
pygame.display.update()
# Initialise performance variables
comp_time_sum = 0
comp_moves = 0
ai_time_sum = 0
ai_moves = 0


def computerTurn():
    global col, row, text_surface, text_rect,comp_time_sum, comp_moves
    start_time = time.time()
    move = random.randint(0, 6)
    while not utilities.isEmptyCell(board, move):
        move = random.randint(0, 6)
    col = move
    if utilities.isEmptyCell(board, col):
        pygame.time.wait(1000)
        row = utilities.getUpcomingEmptyRow(board, col)
        board[row][col] = 1
        if utilities.isWinningTurn(board, 1):
            text_surface = font.render("More smarter than AI ... You win!", True, FONT_COLOR)
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, 50))
            screen.blit(text_surface, text_rect)
    setBoard(board)
    comp_time_sum += time.time() - start_time
    comp_moves += 1


def AITurn(algorithmToUse, difficulty):
    global col, row, text_surface, text_rect, ai_time_sum, ai_moves
    start_time = time.time()

    if (algorithmToUse == 2):
        col = utilities.getBestPositionRefined(board, difficulty)
    else:
        col = utilities.getBestPositionNormal(board, difficulty)
    if utilities.isEmptyCell(board, col):
        pygame.time.wait(1000)
        row = utilities.getUpcomingEmptyRow(board, col)
        board[row][col] = 2
        if utilities.isWinningTurn(board, 2):
            text_surface = font.render("AI Agent wins!", True, FONT_COLOR)
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, 50))
            screen.blit(text_surface, text_rect)
    setBoard(board)
    ai_time_sum += time.time() - start_time
    ai_moves += 1


while not utilities.isTerminalState(board):
    if turn % 2 == 0:
        computerTurn()

    else:
        AITurn(algorithmToUse, difficulty)
    turn += 1

pygame.time.wait(2500)
# Calculate performance measure
comp_avg_time = comp_time_sum / comp_moves if comp_moves > 0 else 0
ai_avg_time = ai_time_sum / ai_moves if ai_moves > 0 else 0

print("Computer Turn Average Time: ", comp_avg_time)
print("AI Turn Average Time: ", ai_avg_time)
print("Total Number of Computer Moves: ", comp_moves)
print("Total Number of AI Moves: ", ai_moves)
pygame.quit()