import pygame
from button import Button


class ChoiceLvl:
    def __init__(self):
        def fn1():
            pass

        button_choice_lvl_1 = Button(position=(80, 100), size=(100, 50),
                                     clr=(220, 220, 220),
                                     cngclr=(255, 0, 0), func=fn1,
                                     text='Уровень 1')
        button_choice_lvl_2 = Button(position=(80, 100), size=(100, 50),
                                     clr=(220, 220, 220),
                                     cngclr=(255, 0, 0), func=fn1,
                                     text='Уровень 2')
        button_choice_lvl_3 = Button(position=(80, 100), size=(100, 50),
                                     clr=(220, 220, 220),
                                     cngclr=(255, 0, 0), func=fn1,
                                     text='Уровень 3')
        self.buttons = [button_choice_lvl_1, button_choice_lvl_2,
                        button_choice_lvl_3]

    def render(self, surface):
        for button in self.buttons:
            button.draw(surface)
