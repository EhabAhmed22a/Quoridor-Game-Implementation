import pygame
from Graphic.Board import Board
from Graphic.roundRect import round_rect

colors = {"black": (0, 0, 0), "white": (234, 236, 238)}

def main_menu():
    pygame.init()
    pygame.display.set_caption('Quoridor')
    screen = pygame.display.set_mode((850, 790))
    bg = pygame.image.load("Graphic/bg.jpg").convert()
    bg = pygame.transform.scale(bg, (850, 790))
    screen.blit(bg, (0, 0))

    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    title = myfont.render('Quoridor', False, colors["black"])
    screen.blit(title, (325, 100))

    # Buttons
    button_font = pygame.font.SysFont('Comic Sans MS', 35)
    h_vs_h_button = pygame.Rect(300, 300, 250, 75)
    h_vs_ai_button = pygame.Rect(300, 425, 250, 75)

    round_rect(screen, colors["white"], h_vs_h_button, 10)
    h_vs_h_text = button_font.render('Human vs Human', False, colors["black"])
    text_rect = h_vs_h_text.get_rect(center=h_vs_h_button.center)
    screen.blit(h_vs_h_text, text_rect)

    round_rect(screen, colors["white"], h_vs_ai_button, 10)
    h_vs_ai_text = button_font.render('Human vs AI', False, colors["black"])
    text_rect = h_vs_ai_text.get_rect(center=h_vs_ai_button.center)
    screen.blit(h_vs_ai_text, text_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if h_vs_h_button.collidepoint(event.pos):
                    return 2, 0
                if h_vs_ai_button.collidepoint(event.pos):
                    return 2, 1

if __name__ == '__main__':
    numOfPlayers, numOfAi = main_menu()
    board = Board(numOfPlayers, numOfAi)
    board.play()