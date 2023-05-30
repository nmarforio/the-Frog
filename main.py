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


# Jump player
isJump = False
jumpCount = 10
vel = 5

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
    keys = pygame.key.get_pressed()
    if not (isJump):
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            playerY -= (jumpCount**2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_changeX -= 1
        elif event.key == pygame.K_RIGHT:
            player_changeX += 1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player_changeX = 0

    # Player boundries
    playerX += player_changeX
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936

    player_moves(playerX, playerY)
    pygame.display.update()
