import pygame
import random
from collections import deque

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 10
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
MINE_COUNT = 20

# Colors
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Initialize fonts
font = pygame.font.Font(None, 36)

# Initialize game variables
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
revealed = [[False for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
mines = []

# Functions
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def draw_mines():
    for mine in mines:
        x, y = mine
        pygame.draw.rect(screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_numbers():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if revealed[y][x]:
                num = grid[y][x]
                if num > 0:
                    text = font.render(str(num), True, BLACK)
                    text_rect = text.get_rect()
                    text_rect.center = (x * GRID_SIZE + GRID_SIZE // 2, y * GRID_SIZE + GRID_SIZE // 2)
                    screen.blit(text, text_rect)

def reveal(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        if not (0 <= x < GRID_WIDTH) or not (0 <= y < GRID_HEIGHT) or revealed[y][x]:
            continue

        revealed[y][x] = True

        if grid[y][x] == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    queue.append((x + dx, y + dy))

def count_adjacent_mines(x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if 0 <= x + dx < GRID_WIDTH and 0 <= y + dy < GRID_HEIGHT:
                if grid[y + dy][x + dx] == -1:
                    count += 1
    return count

# Place mines randomly
for _ in range(MINE_COUNT):
    x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
    while grid[y][x] == -1:
        x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
    grid[y][x] = -1
    mines.append((x, y))

# Calculate the numbers
for x in range(GRID_WIDTH):
    for y in range(GRID_HEIGHT):
        if grid[y][x] == -1:
            continue
        grid[y][x] = count_adjacent_mines(x, y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x //= GRID_SIZE
            y //= GRID_SIZE
            if grid[y][x] == -1:
                running = False
            else:
                reveal(x, y)

    screen.fill(WHITE)
    draw_grid()
    draw_mines()
    draw_numbers()
    pygame.display.flip()

pygame.quit()