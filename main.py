import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 368
playerY = 480


def player(x, y):
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:
    # Background
    screen.fill((100, 20, 20))
    playerY -= 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()
