import sys
import pygame
from board import Board
from button import Button
from choice_lvl import ChoiceLvl


def function_button_choice_lvl():
    global run_start_menu
    run_start_menu = False


def function_button_quit():
    pygame.quit()
    sys.exit()


def function_button_save_txt():
    convert = open('rating.txt', 'w+')
    convert.close()


pygame.init()
size = height, width = 400, 650
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Игра')
screen.fill('#DBD7D2')
pygame.display.update()
board = Board(5, 7)
board.set_view(50, 50, 50)
BOX = pygame.Color('#B15124')
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
buttons = [button_choice_lvl, button_quit, button_save_txt]

run_start_menu = True
while run_start_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_start_menu = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run_start_menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.rect.collidepoint(pos):
                        button.call_back()
    for button in buttons:
        button.draw(screen)
    pygame.display.flip()

run_lvl_menu = True
while run_lvl_menu:
    screen.fill('#DBD7D2')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_lvl_menu = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run_lvl_menu = False
    surface = ChoiceLvl()
    surface.render(screen)
    pygame.display.flip()
pygame.quit()
