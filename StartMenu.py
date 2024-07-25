import pygame
import sys
import random
def StartMenu():

    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    pygame.init()
    screen2 = pygame.display.set_mode((500, 500))
    # global constant variables
    myfont = pygame.font.SysFont("monospace", 30,bold=True)

    start_menu = pygame.Surface((500,500))
    start_menu.fill((250,150,100))
    start_menu_rect = start_menu.get_rect(center=screen2.get_rect().center)

    # Set the dimensions of the game window
    caption_surface = pygame.Surface((500, 50))
    caption_surface.fill((255, 255, 255))
    # Set the game caption to the new surface
    pygame.display.set_caption("My Game")
    #
    start_button = pygame.Rect(140, 420, 200, 50)

    diff_label = myfont.render("Game Difficulty", 1, WHITE)
    diff_label_rect = diff_label.get_rect(center=(250, 20))

    hard_button = pygame.Rect(25, 60, 150, 50)
    hard_text = myfont.render("Hard", 1, BLACK)
    hard_text_rect = hard_text.get_rect(center=hard_button.center)

    medium_button = pygame.Rect(178, 100, 150, 50)
    medium_text = myfont.render("Medium", 1, BLACK)
    medium_text_rect = medium_text.get_rect(center=medium_button.center)

    easy_button = pygame.Rect(335, 150, 150, 50)
    easy_text = myfont.render("Easy", 1, BLACK)
    easy_text_rect = easy_text.get_rect(center=easy_button.center)


    alg_label = myfont.render("Choose Algorithm", 1, WHITE)
    alg_label_rect = alg_label.get_rect(center=(250, 250))
    start_menu.blit(alg_label, alg_label_rect)

    minmax_button = pygame.Rect(25, 300, 150, 50)
    minmax_text = myfont.render("MinMax", 1, BLACK)
    minmax_text_rect = minmax_text.get_rect(center=minmax_button.center)

    ab_button = pygame.Rect(335, 300, 150, 50)
    ab_text = myfont.render("AlBt", 1, BLACK)
    ab_text_rect = ab_text.get_rect(center=ab_button.center)

    def show_start_menu():
        screen2.blit(start_menu, (0, 0))
        # Draw the start button
        pygame.draw.rect(start_menu, BLUE, start_button)
        start_text = myfont.render("Start", 1, BLACK)
        start_menu.blit(start_text, (start_button.x + start_button.width/2 - start_text.get_width()/2, start_button.y + start_button.height/2 - start_text.get_height()/2))
        # Draw the difficulty selection buttons and label
        start_menu.blit(diff_label, diff_label_rect)
        pygame.draw.rect(start_menu, WHITE, easy_button, border_radius=20)
        start_menu.blit(easy_text, easy_text_rect)
        pygame.draw.rect(start_menu, WHITE, medium_button, border_radius=20)
        start_menu.blit(medium_text, medium_text_rect)
        pygame.draw.rect(start_menu, WHITE, hard_button, border_radius=20)
        start_menu.blit(hard_text, hard_text_rect)
        pygame.draw.rect(start_menu, WHITE, ab_button, border_radius=10)
        start_menu.blit(ab_text, ab_text_rect)
        pygame.draw.rect(start_menu, WHITE, minmax_button, border_radius=10)
        start_menu.blit(minmax_text, minmax_text_rect)
        # Update the display
        pygame.display.update()



    difficulty = 2
    algorithmToUse = 1
    labelToCange = 0
    pos = (0, 0)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if easy_button.collidepoint(pos):
                    difficulty = random.randint(3, 4)
                    diff_label = myfont.render("Easy Mode", 1, RED)
                    labelToCange = 1
                elif medium_button.collidepoint(pos):
                    difficulty = random.randint(3,4)
                    diff_label = myfont.render("Medium Mode", 1, RED)
                    labelToCange = 1
                elif hard_button.collidepoint(pos):
                    difficulty = random.randint(5,6)
                    diff_label = myfont.render("Hard Mode!", 1, RED)
                    labelToCange = 1
                elif minmax_button.collidepoint(pos):
                    algorithmToUse = 1
                    alg_label = myfont.render("Ai Use MiniMax!", 1, RED)
                    labelToCange = 2
                elif ab_button.collidepoint(pos):
                    algorithmToUse = 2
                    alg_label = myfont.render("Ai Use AlphaBeta", 1, RED)
                    labelToCange = 2

                if(labelToCange == 1):
                    start_menu.fill((250, 150, 100),diff_label_rect)  # fill the start menu surface with the background color
                    diff_label_rect = diff_label.get_rect(center=(250, 20))
                    start_menu.blit(diff_label, diff_label_rect)
                if(labelToCange == 2):
                    start_menu.fill((250, 150, 100),alg_label_rect)  # fill the start menu surface with the background color
                    alg_label_rect = alg_label.get_rect(center=(250, 250))
                    start_menu.blit(alg_label, alg_label_rect)

            # Check if the start button was clicked
            if start_button.collidepoint(pos):
                return algorithmToUse,difficulty

            show_start_menu()
        pygame.display.update()

