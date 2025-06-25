import pygame
import sys

from src.models import Field

pygame.init()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


def check_exit():
    '''
    Проверка сигнала нажатия на кнопку выхода из оконного приложения игры pygame
    '''
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def main():
    '''
    **Основная функция запуска игры.** 
    
    Для удобства запуска всей программы все импорты библиотек проходят в один файл, 
    где уже и 
    '''
    
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    
    field = Field(screen = SCREEN, windows_size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    
    
    while True:
        field.show()
        
        
        
        pygame.display.update()
        
        
if __name__=="__main__":
    main()