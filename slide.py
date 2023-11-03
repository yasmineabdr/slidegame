import pygame
import random

# Constants and initialization
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 300, 300
PUZZLE_SIZE = 3
TILE_SIZE = WIDTH // PUZZLE_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sliding Puzzle')

# Load images for the tiles and the transparent empty tile
tile_images = {
    1: pygame.transform.scale(pygame.image.load('image_part_001.jpg'), (TILE_SIZE, TILE_SIZE)),
    2: pygame.transform.scale(pygame.image.load('image_part_002.jpg'), (TILE_SIZE, TILE_SIZE)),
    3: pygame.transform.scale(pygame.image.load('image_part_003.jpg'), (TILE_SIZE, TILE_SIZE)),
    4: pygame.transform.scale(pygame.image.load('image_part_004.jpg'), (TILE_SIZE, TILE_SIZE)),
    5: pygame.transform.scale(pygame.image.load('image_part_005.jpg'), (TILE_SIZE, TILE_SIZE)),
    6: pygame.transform.scale(pygame.image.load('image_part_006.jpg'), (TILE_SIZE, TILE_SIZE)),
    7: pygame.transform.scale(pygame.image.load('image_part_007.jpg'), (TILE_SIZE, TILE_SIZE)),
    8: pygame.transform.scale(pygame.image.load('image_part_008.jpg'), (TILE_SIZE, TILE_SIZE)),
    0: pygame.Surface((TILE_SIZE, TILE_SIZE))  # Image for the empty tile (transparent)
}

# Function to create and shuffle the puzzle
def create_puzzle(size):
    puzzle = [x for x in range(size * size)]
    random.shuffle(puzzle)
    return [puzzle[i:i + size] for i in range(0, size * size, size)]

# Function to draw the puzzle with images
def draw_puzzle(puzzle):
    screen.fill(BLACK)
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            number = puzzle[row][col]
            tile_image = tile_images[number]
            screen.blit(tile_image, (col * TILE_SIZE, row * TILE_SIZE))

def find_empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return (i, j)

def valid_move(puzzle, move):
    empty_pos = find_empty(puzzle)
    if move == 'up' and empty_pos[0] > 0:
        return True
    elif move == 'down' and empty_pos[0] < len(puzzle) - 1:
        return True
    elif move == 'left' and empty_pos[1] > 0:
        return True
    elif move == 'right' and empty_pos[1] < len(puzzle[0]) - 1:
        return True
    else:
        return False

def move(puzzle, direction):
    empty_pos = find_empty(puzzle)
    if direction == 'up' and empty_pos[0] < len(puzzle) - 1:
        puzzle[empty_pos[0]][empty_pos[1]], puzzle[empty_pos[0] + 1][empty_pos[1]] = puzzle[empty_pos[0] + 1][empty_pos[1]], puzzle[empty_pos[0]][empty_pos[1]]
    elif direction == 'down' and empty_pos[0] > 0:
        puzzle[empty_pos[0]][empty_pos[1]], puzzle[empty_pos[0] - 1][empty_pos[1]] = puzzle[empty_pos[0] - 1][empty_pos[1]], puzzle[empty_pos[0]][empty_pos[1]]
    elif direction == 'left' and empty_pos[1] < len(puzzle[0]) - 1:
        puzzle[empty_pos[0]][empty_pos[1]], puzzle[empty_pos[0]][empty_pos[1] + 1] = puzzle[empty_pos[0]][empty_pos[1] + 1], puzzle[empty_pos[0]][empty_pos[1]]
    elif direction == 'right' and empty_pos[1] > 0:
        puzzle[empty_pos[0]][empty_pos[1]], puzzle[empty_pos[0]][empty_pos[1] - 1] = puzzle[empty_pos[0]][empty_pos[1] - 1], puzzle[empty_pos[0]][empty_pos[1]]

# Create the puzzle and game loop
puzzle = create_puzzle(PUZZLE_SIZE)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and valid_move(puzzle, 'down'):
                move(puzzle, 'up')
            elif event.key == pygame.K_DOWN and valid_move(puzzle, 'up'):
                move(puzzle, 'down')
            elif event.key == pygame.K_LEFT and valid_move(puzzle, 'right'):
                move(puzzle, 'left')
            elif event.key == pygame.K_RIGHT and valid_move(puzzle, 'left'):
                move(puzzle, 'right')

    draw_puzzle(puzzle)
    pygame.display.flip()

pygame.quit()

