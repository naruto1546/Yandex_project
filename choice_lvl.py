import pygame
from button import Button


class ChoiceLvl:
    def __init__(self):
        def lvl1():
            pass

        def lvl2():
            pass

        def lvl3():
            pass

        button_choice_lvl_1 = Button(position=(100, 100), size=(100, 50),
                                     clr='#34C924',
                                     cngclr=(255, 0, 0), func=lvl1,
                                     text='Уровень 1')
        button_choice_lvl_2 = Button(position=(100, 160), size=(100, 50),
                                     clr='#34C924',
                                     cngclr=(255, 0, 0), func=lvl2,
                                     text='Уровень 2')
        button_choice_lvl_3 = Button(position=(100, 220), size=(100, 50),
                                     clr='#34C924',
                                     cngclr=(255, 0, 0), func=lvl3,
                                     text='Уровень 3')
        self.buttons = [button_choice_lvl_1, button_choice_lvl_2,
                        button_choice_lvl_3]

    def render(self, surface):
        for button in self.buttons:
            button.draw(surface)
