import sys
import pygame
from board import Board
from button import Button


def function_button_choice_lvl():
    global run_start_menu
    run_start_menu = False
    run_lvl_menu = True
    while run_lvl_menu:
        screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for button in buttons_choice_lvl:
                        if button.rect.collidepoint(pos):
                            button.call_back()
        for button in buttons_choice_lvl:
            button.draw(screen)
        pygame.display.flip()


def function_button_quit():
    pygame.quit()
    sys.exit()


def function_button_save_txt():
    convert = open('rating.txt', 'w+')
    convert.close()


def function_button_ok():
    pass


def function_button_lvl1():
    county_balls = 3
    text = font.render(str(county_balls), True, BALL)
    board = Board(3, 3)
    board.set_view(125, 225, 50)
    running = True
    while running:
        screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for button in buttons_lvl:
                        if button.rect.collidepoint(pos):
                            button.call_back()
        for button in buttons_lvl:
            button.draw(screen)
        pygame.draw.rect(screen, GREEN, (300, 0, 100, 50))
        pygame.draw.circle(screen, BALL, (360, 25), 20)
        screen.blit(text, (310, 1))
        pygame.draw.circle(screen, BALL_IN_BOX, (200, 300), 30)
        pygame.draw.rect(screen, BOX, (125, 225, 150, 150))
        board.render(screen)
        pygame.display.flip()


def function_button_lvl2():
    county_balls = 3
    text = font.render(str(county_balls), True, BALL)
    board = Board(4, 4)
    board.set_view(100, 200, 50)
    running = True
    while running:
        screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for button in buttons_lvl:
                        if button.rect.collidepoint(pos):
                            button.call_back()
        for button in buttons_lvl:
            button.draw(screen)
        pygame.draw.rect(screen, GREEN, (300, 0, 100, 50))
        pygame.draw.circle(screen, BALL, (360, 25), 20)
        screen.blit(text, (310, 1))
        pygame.draw.circle(screen, BALL_IN_BOX, (225, 325), 30)
        pygame.draw.circle(screen, BALL_IN_BOX, (225, 225), 30)
        pygame.draw.rect(screen, BOX, (100, 200, 200, 200))
        board.render(screen)
        pygame.display.flip()


def function_button_lvl3():
    county_balls = 4
    text = font.render(str(county_balls), True, BALL)
    board = Board(5, 5)
    board.set_view(75, 175, 50)
    running = True
    while running:
        screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for button in buttons_lvl:
                        if button.rect.collidepoint(pos):
                            button.call_back()
        for button in buttons_lvl:
            button.draw(screen)
        pygame.draw.rect(screen, GREEN, (300, 0, 100, 50))
        pygame.draw.circle(screen, BALL, (360, 25), 20)
        screen.blit(text, (310, 1))
        pygame.draw.circle(screen, BALL_IN_BOX, (250, 300), 30)
        pygame.draw.circle(screen, BALL_IN_BOX, (150, 250), 30)
        pygame.draw.rect(screen, BOX, (75, 175, 250, 250))
        board.render(screen)
        pygame.display.flip()


def back():
    global run_start_menu
    run_start_menu = True
    while run_start_menu:
        screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for button in buttons_start_menu:
                        if button.rect.collidepoint(pos):
                            button.call_back()
        for button in buttons_start_menu:
            button.draw(screen)
        pygame.display.flip()


pygame.init()
size = height, width = 400, 650
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Игра')
BACKGROUND = pygame.Color('#DBD7D2')
BOX = pygame.Color('#B15124')
BALL = pygame.Color('#474A51')
BALL_IN_BOX = pygame.Color('#DBD7D2')
GREEN = pygame.Color('#34C924')
font = pygame.font.SysFont("Segoe Print", 28)
screen.fill(BACKGROUND)
pygame.display.update()

button_choice_lvl = Button(position=(200, 280), size=(215, 50),
                           clr='#34C924',
                           cngclr=(255, 0, 0), func=function_button_choice_lvl,
                           text='Выбрать уроевень')
button_quit = Button(position=(200, 400), size=(215, 50),
                     clr='#34C924',
                     cngclr=(255, 0, 0), func=function_button_quit,
                     text='Выйти из игры')
button_save_txt = Button(position=(200, 340), size=(215, 50),
                         clr='#34C924',
                         cngclr=(255, 0, 0), func=function_button_save_txt,
                         text='Сохранить результаты')
buttons_start_menu = [button_choice_lvl, button_quit, button_save_txt]

button_choice_lvl_1 = Button(position=(110, 110), size=(100, 50),
                             clr='#34C924',
                             cngclr=(255, 0, 0), func=function_button_lvl1,
                             text='Уровень 1')
button_choice_lvl_2 = Button(position=(110, 170), size=(100, 50),
                             clr='#34C924',
                             cngclr=(255, 0, 0), func=function_button_lvl2,
                             text='Уровень 2')
button_choice_lvl_3 = Button(position=(110, 230), size=(100, 50),
                             clr='#34C924',
                             cngclr=(255, 0, 0), func=function_button_lvl3,
                             text='Уровень 3')
button_back = Button(position=(25, 25), size=(50, 50),
                     clr='#34C924',
                     cngclr=(255, 0, 0), func=back,
                     text='<-')
button_ok = Button(position=(360, 626), size=(80, 45),
                   clr='#34C924',
                   cngclr=(255, 0, 0), func=function_button_ok,
                   text='ok')
buttons_choice_lvl = [button_choice_lvl_1, button_choice_lvl_2,
                      button_choice_lvl_3, button_back]
buttons_lvl = [button_back, button_ok]

run_start_menu = True
while run_start_menu:
    screen.fill(BACKGROUND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for button in buttons_start_menu:
                    if button.rect.collidepoint(pos):
                        button.call_back()
    for button in buttons_start_menu:
        button.draw(screen)
    pygame.display.flip()
pygame.quit()
