from random import randint
import pygame

pygame.init()

def play():
    curr_dir = "E" # Logs current direction: N S E W
    score = 0 # Logs current score, length of snake will be score + 1
    size_y = size_x = 0

    while size_y < 5:
        size_y = int(input("Height of grid (>= 5): "))

    while size_x < 5:
        size_x = int(input("Width of grid (>= 5): "))

    game_board = [[0 for j in range(size_x)] for i in range(size_y)]
    snake_stack = []
    
    head_square = [0, 0]
    snake_stack.append(head_square)

    game_board[head_square[0]][head_square[1]] = 2

    spawn_loc = randint(1, size_y * size_x - len(snake_stack))

    game_board = spawn(game_board, spawn_loc)

    WIDTH = 60 * size_x
    HEIGHT = 60 * size_y
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    draw(game_board, SCREEN)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    curr_dir = "W"
                elif event.key == pygame.K_RIGHT:
                    curr_dir = "E"
                elif event.key == pygame.K_UP:
                    curr_dir = "N"
                elif event.key == pygame.K_DOWN:
                    curr_dir = "S"

        new_head_square = move(head_square, curr_dir, size_y, size_x)

        if new_head_square == "Death" or game_board[new_head_square[0]][new_head_square[1]] == 1:
            break

        snake_stack.append(new_head_square)
        
        if game_board[new_head_square[0]][new_head_square[1]] == 0:
            game_board[new_head_square[0]][new_head_square[1]] = 2
            if len(snake_stack) > 1:
                second_square = snake_stack[-2]
                game_board[second_square[0]][second_square[1]] = 1
            tail_square = snake_stack.pop(0)
            game_board[tail_square[0]][tail_square[1]] = 0

        elif game_board[new_head_square[0]][new_head_square[1]] == 3:
            score += 1
            game_board[new_head_square[0]][new_head_square[1]] = 2
            if len(snake_stack) > 1:
                second_square = snake_stack[-2]
                game_board[second_square[0]][second_square[1]] = 1

            spawn_loc = randint(1, size_y * size_x - len(snake_stack))

            game_board = spawn(game_board, spawn_loc)
        
        head_square = new_head_square

        draw(game_board, SCREEN)

        pygame.display.update()

        pygame.time.delay(500 - 5 * score)

    print(score)


curr_dir = "N" # Logs current direction: N S E W
score = 0 # Logs current score, length of snake will be score + 1

def show_state(game_board):
    for i in game_board:
        print(' '.join(f"{n}" for n in i))

def spawn(game_board, spawn_loc):
    count = 0

    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 0:
                count += 1
            if count == spawn_loc:
                game_board[i][j] = 3
                return game_board

def move(head_square, curr_dir, size_y, size_x):
    if curr_dir == "N":
        head_square = [head_square[0] - 1, head_square[1]]
    elif curr_dir == "S":
        head_square = [head_square[0] + 1, head_square[1]]
    elif curr_dir == "E":
        head_square = [head_square[0], head_square[1] + 1]
    else: # curr_dir == "W"
        head_square = [head_square[0], head_square[1] - 1]

    if head_square[0] >= size_y or  head_square[1] >= size_x or \
        head_square[0] < 0 or  head_square[1] < 0:
        return "Death"
    else:
        return head_square

def draw(game_board, screen):
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    DARKGREEN = (0, 100, 0)
    BLUE = (0, 0, 255)
    x = 0
    y = 0
    w = 60
    for row in game_board:
        for col in row:
            box = pygame.Rect(x, y, w, w)
            if col == 0:
                pygame.draw.rect(screen, WHITE, box)
            elif col == 1:
                pygame.draw.rect(screen, GREEN, box)
            elif col == 2:
                pygame.draw.rect(screen, DARKGREEN, box)
            else:
                pygame.draw.rect(screen, BLUE, box)
            x = x + w
        y = y + w
        x = 0

play()