import pygame
import random
import math


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


def player_moves(x, y):
    wn.blit(player, (x, y))


# Jump player
isJump = False
jumpCount = 10
vel = 5

# branch1: Y 0-150
branch = pygame.image.load("branch.png")
branch1X = random.randint(0, 1000)
branch1Y = random.randint(0, 150)
branch1X_change = 1
branch1Y_change = 40


def branch1(x, y):
    wn.blit(branch, (x, y))


# branch2: Y 200-350
branch2X = random.randint(0, 1000)
branch2Y = random.randint(200, 350)
branch2X_change = 1
branch2Y_change = 40


def branch2(x, y):
    wn.blit(branch, (x, y))


# branch3: Y 400-550
branch3X = random.randint(0, 1000)
branch3Y = random.randint(400, 550)
branch3X_change = 1
branch3Y_change = 40


def branch3(x, y):
    wn.blit(branch, (x, y))


# collision & staying on top of the branch
def collisionBranch3(branch3X, branch3Y, playerX, playerY):
    distance = math.sqrt(
        (math.pow(branch3X - playerX, 2)) + (math.pow(branch3Y - playerY, 2))
    )
    if distance < 27:
        return True
    else:
        return False


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
    if keys[pygame.K_LEFT]:
        playerX -= vel
    if keys[pygame.K_RIGHT]:
        playerX += vel
    if not (isJump):
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            if end_jump:
                playerX = branch3X
                playerY = branch3Y

            else:
                playerY -= (jumpCount**2) * 0.5 * neg
                jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # Player boundries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936

    # Branch1 bundries & movements
    branch1X += branch1X_change
    if branch1X <= 0:
        branch1X_change = 1
        branch1X += branch1X_change
        branch1Y += branch1Y_change

    if branch1X >= 936:
        branch1X_change = -1
        branch1X += branch1X_change
        branch1Y += branch1Y_change

    if branch1Y >= 150:
        branch1Y = random.randint(0, 150)

    # branch2
    branch2X += branch2X_change
    if branch2X <= 0:
        branch2X_change = 2
        branch2X += branch2X_change
        branch2Y += branch2Y_change

    if branch2X >= 936:
        branch2X_change = -2
        branch2X += branch2X_change
        branch2Y += branch2Y_change

    if branch2Y >= 350:
        branch2Y = random.randint(200, 350)

    # branch2
    branch3X += branch3X_change
    if branch3X <= 0:
        branch3X_change = 1.5
        branch3X += branch3X_change
        branch3Y += branch3Y_change

    if branch3X >= 936:
        branch3X_change = -1.5
        branch3X += branch3X_change
        branch3Y += branch3Y_change

    if branch3Y >= 550:
        branch3Y = random.randint(400, 550)

    # jump on the Branch
    end_jump = collisionBranch3(branch3X, branch3Y, playerX, playerY)

    player_moves(playerX, playerY)
    branch1(branch1X, branch1Y)
    branch2(branch2X, branch2Y)
    branch3(branch3X, branch3Y)

    pygame.display.update()
