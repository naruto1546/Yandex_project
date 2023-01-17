import sys
import pygame
from board import Board
from button import Button


def function_button_choice_lvl():
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
    text = font.render('Уровень пройден', True, BALL)
    text1 = font.render('Найдены все шарики', True, BALL)
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
                    for button_last_screen in buttons_last_screen:
                        if button_last_screen.rect.collidepoint(pos):
                            button_last_screen.call_back()
        for button_last_screen in buttons_last_screen:
            button_last_screen.draw(screen)
        screen.blit(text, (75, 250))
        screen.blit(text1, (50, 300))
        pygame.display.flip()
    pygame.quit()


def function():
    pass


def function_button_back_start_menu():
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


def function_button_quit_last_screen():
    pygame.quit()
    sys.exit()


def function_button_lvl1():
    county_balls = 3
    text = font.render(str(county_balls), True, BALL)
    board = Board(3, 3)
    board.set_view(125, 225, 50)
    button_left1 = Button(position=(100, 250), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')
    button_left2 = Button(position=(100, 300), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')
    button_left3 = Button(position=(100, 350), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')

    button_right1 = Button(position=(300, 250), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')
    button_right2 = Button(position=(300, 300), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')
    button_right3 = Button(position=(300, 350), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')

    button_up1 = Button(position=(150, 200), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')
    button_up2 = Button(position=(200, 200), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')
    button_up3 = Button(position=(250, 200), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')

    button_down1 = Button(position=(150, 400), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')
    button_down2 = Button(position=(200, 400), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')
    button_down3 = Button(position=(250, 400), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')

    buttons_lvl1_left = [button_left1, button_left2, button_left3]
    buttons_lvl1_right = [button_right1, button_right2, button_right3]
    buttons_lvl1_up = [button_up1, button_up2, button_up3]
    buttons_lvl1_down = [button_down1, button_down2, button_down3]
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
                    for button_left in buttons_lvl1_left:
                        if button_left.rect.collidepoint(pos):
                            button_left.call_back()
                    for button_right in buttons_lvl1_right:
                        if button_right.rect.collidepoint(pos):
                            button_right.call_back()
                    for button_up in buttons_lvl1_up:
                        if button_up.rect.collidepoint(pos):
                            button_up.call_back()
                    for button_down in buttons_lvl1_down:
                        if button_down.rect.collidepoint(pos):
                            button_down.call_back()
        for button in buttons_lvl:
            button.draw(screen)
        for button_left in buttons_lvl1_left:
            button_left.draw(screen)
        for button_right in buttons_lvl1_right:
            button_right.draw(screen)
        for button_up in buttons_lvl1_up:
            button_up.draw(screen)
        for button_down in buttons_lvl1_down:
            button_down.draw(screen)
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
    button_left1 = Button(position=(75, 225), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')
    button_left2 = Button(position=(75, 275), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')
    button_left3 = Button(position=(75, 325), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')
    button_left4 = Button(position=(75, 375), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')

    button_right1 = Button(position=(325, 225), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')
    button_right2 = Button(position=(325, 275), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')
    button_right3 = Button(position=(325, 325), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')
    button_right4 = Button(position=(325, 375), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')

    button_up1 = Button(position=(125, 175), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')
    button_up2 = Button(position=(175, 175), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')
    button_up3 = Button(position=(225, 175), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')
    button_up4 = Button(position=(275, 175), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')

    button_down1 = Button(position=(125, 425), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')
    button_down2 = Button(position=(175, 425), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')
    button_down3 = Button(position=(225, 425), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')
    button_down4 = Button(position=(275, 425), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')

    buttons_lvl2_left = [button_left1, button_left2, button_left3,
                         button_left4]
    buttons_lvl2_right = [button_right1, button_right2, button_right3,
                          button_right4]
    buttons_lvl2_up = [button_up1, button_up2, button_up3, button_up4]
    buttons_lvl2_down = [button_down1, button_down2, button_down3,
                         button_down4]
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
                    for button_left in buttons_lvl2_left:
                        if button_left.rect.collidepoint(pos):
                            button_left.call_back()
                    for button_right in buttons_lvl2_right:
                        if button_right.rect.collidepoint(pos):
                            button_right.call_back()
                    for button_up in buttons_lvl2_up:
                        if button_up.rect.collidepoint(pos):
                            button_up.call_back()
                    for button_down in buttons_lvl2_down:
                        if button_down.rect.collidepoint(pos):
                            button_down.call_back()
        for button in buttons_lvl:
            button.draw(screen)
        for button_left in buttons_lvl2_left:
            button_left.draw(screen)
        for button_right in buttons_lvl2_right:
            button_right.draw(screen)
        for button_up in buttons_lvl2_up:
            button_up.draw(screen)
        for button_down in buttons_lvl2_down:
            button_down.draw(screen)
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
    button_left1 = Button(position=(50, 200), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')
    button_left2 = Button(position=(50, 250), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')
    button_left3 = Button(position=(50, 300), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')
    button_left4 = Button(position=(50, 350), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')
    button_left5 = Button(position=(50, 400), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='→')

    button_right1 = Button(position=(350, 200), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')
    button_right2 = Button(position=(350, 250), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')
    button_right3 = Button(position=(350, 300), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')
    button_right4 = Button(position=(350, 350), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')
    button_right5 = Button(position=(350, 400), size=(50, 50),
                           clr=BACKGROUND,
                           cngclr=BACKGROUND, func=function,
                           text='←')

    button_up1 = Button(position=(100, 150), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')
    button_up2 = Button(position=(150, 150), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')
    button_up3 = Button(position=(200, 150), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')
    button_up4 = Button(position=(250, 150), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')
    button_up5 = Button(position=(300, 150), size=(50, 50),
                        clr=BACKGROUND,
                        cngclr=BACKGROUND, func=function,
                        text='↓')

    button_down1 = Button(position=(100, 450), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')
    button_down2 = Button(position=(150, 450), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')
    button_down3 = Button(position=(200, 450), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')
    button_down4 = Button(position=(250, 450), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')
    button_down5 = Button(position=(300, 450), size=(50, 50),
                          clr=BACKGROUND,
                          cngclr=BACKGROUND, func=function,
                          text='↑')

    buttons_lvl3_left = [button_left1, button_left2, button_left3,
                         button_left4, button_left5]
    buttons_lvl3_right = [button_right1, button_right2, button_right3,
                          button_right4, button_right5]
    buttons_lvl3_up = [button_up1, button_up2, button_up3, button_up4,
                       button_up5]
    buttons_lvl3_down = [button_down1, button_down2, button_down3,
                         button_down4, button_down5]
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
                    for button_left in buttons_lvl3_left:
                        if button_left.rect.collidepoint(pos):
                            button_left.call_back()
                    for button_right in buttons_lvl3_right:
                        if button_right.rect.collidepoint(pos):
                            button_right.call_back()
                    for button_up in buttons_lvl3_up:
                        if button_up.rect.collidepoint(pos):
                            button_up.call_back()
                    for button_down in buttons_lvl3_down:
                        if button_down.rect.collidepoint(pos):
                            button_down.call_back()
        for button in buttons_lvl:
            button.draw(screen)
        for button_left in buttons_lvl3_left:
            button_left.draw(screen)
        for button_right in buttons_lvl3_right:
            button_right.draw(screen)
        for button_up in buttons_lvl3_up:
            button_up.draw(screen)
        for button_down in buttons_lvl3_down:
            button_down.draw(screen)
        pygame.draw.rect(screen, GREEN, (300, 0, 100, 50))
        pygame.draw.circle(screen, BALL, (360, 25), 20)
        screen.blit(text, (310, 1))
        pygame.draw.circle(screen, BALL_IN_BOX, (250, 300), 30)
        pygame.draw.circle(screen, BALL_IN_BOX, (150, 250), 30)
        pygame.draw.rect(screen, BOX, (75, 175, 250, 250))
        board.render(screen)
        pygame.display.flip()


def function_back():
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
RED = pygame.Color((255, 0, 0))
font = pygame.font.SysFont("Segoe Print", 28)
screen.fill(BACKGROUND)
pygame.display.update()

button_choice_lvl = Button(position=(200, 280), size=(215, 50),
                           clr=GREEN,
                           cngclr=RED, func=function_button_choice_lvl,
                           text='Выбрать уроевень')
button_quit = Button(position=(200, 400), size=(215, 50),
                     clr=GREEN,
                     cngclr=RED, func=function_button_quit,
                     text='Выйти из игры')
button_save_txt = Button(position=(200, 340), size=(215, 50),
                         clr=GREEN,
                         cngclr=RED, func=function_button_save_txt,
                         text='Сохранить результаты')
buttons_start_menu = [button_choice_lvl, button_quit, button_save_txt]

button_choice_lvl_1 = Button(position=(110, 110), size=(100, 50),
                             clr=GREEN,
                             cngclr=RED, func=function_button_lvl1,
                             text='Уровень 1')
button_choice_lvl_2 = Button(position=(110, 170), size=(100, 50),
                             clr=GREEN,
                             cngclr=RED, func=function_button_lvl2,
                             text='Уровень 2')
button_choice_lvl_3 = Button(position=(110, 230), size=(100, 50),
                             clr=GREEN,
                             cngclr=RED, func=function_button_lvl3,
                             text='Уровень 3')
button_back = Button(position=(25, 25), size=(50, 50),
                     clr=GREEN,
                     cngclr=RED, func=function_back,
                     text='<-')
button_ok = Button(position=(360, 626), size=(80, 45),
                   clr=GREEN,
                   cngclr=RED, func=function_button_ok,
                   text='ok')
button_back_start_menu = Button(position=(100, 400), size=(175, 50),
                                clr=GREEN,
                                cngclr=RED,
                                func=function_button_back_start_menu,
                                text='Вернуться в меню')
button_quit_last_screen = Button(position=(300, 400), size=(175, 50),
                                 clr=GREEN,
                                 cngclr=RED,
                                 func=function_button_quit_last_screen,
                                 text='Выйти из игры')

buttons_choice_lvl = [button_choice_lvl_1, button_choice_lvl_2,
                      button_choice_lvl_3, button_back]

buttons_lvl = [button_back, button_ok]

buttons_last_screen = [button_quit_last_screen, button_back_start_menu]

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
