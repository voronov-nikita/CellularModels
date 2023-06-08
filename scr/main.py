import pygame as pg
from pygame.locals import *

pg.init()


class Window():
    def __init__(self, name:str):
        
        self.name_window:str = name
        self.size_window:tuple = (500, 500)
        self.color_window:tuple = (255, 255, 255)

        self.FPS:int = 30
        self.close:bool = False

        self.InitScreen()

    def InitScreen(self):
        pg.display.set_caption(self.name_window)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.size_window)

    



# инициализация всех обьектов
window = Window("NEW")


# основна работа
while window.close == False:

    window.clock.tick(window.FPS)
        
    # проверка на закрытие экрана
    for event in pg.event.get():
        if event.type == pg.QUIT:
            window.close = True

        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                window.close = True

    window.screen.fill(window.color_window)

    pg.display.update()

#exit()
pg.quit()
