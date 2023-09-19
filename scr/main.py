import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
CUBE_SIZE = 50

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Кубик Рубика')

# Инициализация состояния кубика
cube_state = [
    [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
    [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
    [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
    [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
    [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
    [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
]

# Функция для отрисовки кубика с учетом его текущего состояния
def draw_cube():
    screen.fill(WHITE)
    for face in range(6):
        for row in range(3):
            for col in range(3):
                x = col * CUBE_SIZE + (face % 3) * 4 * CUBE_SIZE
                y = row * CUBE_SIZE + (face // 3) * 4 * CUBE_SIZE
                color = cube_state[face][row][col]
                if color == 'W':
                    pygame.draw.rect(screen, WHITE, (x, y, CUBE_SIZE, CUBE_SIZE))
                elif color == 'R':
                    pygame.draw.rect(screen, RED, (x, y, CUBE_SIZE, CUBE_SIZE))
                elif color == 'G':
                    pygame.draw.rect(screen, GREEN, (x, y, CUBE_SIZE, CUBE_SIZE))
                elif color == 'B':
                    pygame.draw.rect(screen, BLUE, (x, y, CUBE_SIZE, CUBE_SIZE))
                elif color == 'O':
                    pygame.draw.rect(screen, ORANGE, (x, y, CUBE_SIZE, CUBE_SIZE))
                elif color == 'Y':
                    pygame.draw.rect(screen, YELLOW, (x, y, CUBE_SIZE, CUBE_SIZE))
    pygame.display.flip()

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка кубика
    draw_cube()

    # Пример поворота грани (красной) по часовой стрелке
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        cube_state[1] = [
            [cube_state[1][2][0], cube_state[1][1][0], cube_state[1][0][0]],
            [cube_state[1][2][1], cube_state[1][1][1], cube_state[1][0][1]],
            [cube_state[1][2][2], cube_state[1][1][2], cube_state[1][0][2]]
        ]
        cube_state[0] = [
            [cube_state[4][2][2], cube_state[4][1][2], cube_state[4][0][2]],
            [cube_state[4][2][1], cube_state[4][1][1], cube_state[4][0][1]],
            [cube_state[4][2][0], cube_state[4][1][0], cube_state[4][0][0]]
        ]
        cube_state[4] = [
            [cube_state[3][2][0], cube_state[3][1][0], cube_state[3][0][0]],
            [cube_state[3][2][1], cube_state[3][1][1], cube_state[3][0][1]],
            [cube_state[3][2][2], cube_state[3][1][2], cube_state[3][0][2]]
        ]
        cube_state[3] = [
            [cube_state[2][0][2], cube_state[2][1][2], cube_state[2][2][2]],
            [cube_state[2][0][1], cube_state[2][1][1], cube_state[2][2][1]],
            [cube_state[2][0][0], cube_state[2][1][0], cube_state[2][2][0]]
        ]

# Завершение работы Pygame
pygame.quit()
sys.exit()
