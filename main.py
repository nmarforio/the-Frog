import pygame


# initialisaton
pygame.init()

# create the window
wn = pygame.display.set_mode((1000, 700))

# background
background = pygame.image.load("background.jpg")

# Icon and Caption
caption = pygame.display.set_caption("The Frog")
icon = pygame.image.load("frog-icon.png")
pygame.display.set_icon(icon)


# Player the Frog

player = pygame.image.load("frog-player.png")
playerX = 64
playerY = 600
player_changeX = 0
player_changeY = 0


def player_moves(x, y):
    wn.blit(player, (x, y))


# Game running
running = True

while running:
    wn.fill((0, 0, 0))
    wn.blit(background, (0, 0))

    # To Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movements
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("HALOOOO")

    player_moves(playerX, playerY)
    pygame.display.update()
