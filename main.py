import pygame

pygame.init()

# define the screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# define the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# define the starting position and size of the circle
x = WIDTH // 2
y = HEIGHT // 2
radius = 50

# define the animation variables
dx = 5
dy = 5
dr = 1

# run the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the circle position and size
    x += dx
    y += dy
    radius += dr

    # check for collisions with the screen edges
    if x + radius >= WIDTH or x - radius <= 0:
        dx = -dx
    if y + radius >= HEIGHT or y - radius <= 0:
        dy = -dy

    # check for collisions with the maximum and minimum radius
    if radius >= 100 or radius <= 10:
        dr = -dr

    # clear the screen
    screen.fill((0, 0, 0))

    # draw the circle
    pygame.draw.circle(screen, RED, (x, y), radius)

    # update the display
    pygame.display.update()

    # wait for a short time
    pygame.time.wait(10)

# quit pygame
pygame.quit()
