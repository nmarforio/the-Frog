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

# score
score = 0
textFont = pygame.font.Font("freesansbold.ttf", 25)


def showScore():
    scoreText = textFont.render("score:" + str(score), True, (255, 255, 255))
    wn.blit(scoreText, (10, 10))


# Player the Frog
player = pygame.image.load("frog-player.png")
playerX = 64
playerY = 600
player_changeX = 1


def player_moves(x, y):
    wn.blit(player, (x, y))


# Jump player
isJump = False
jumpCount = 10
vel = 5

# targets flies
flies = []
fliesX = []
fliesY = []
num_flies = 6

for i in range(num_flies):
    flies.append(pygame.image.load("fly.png"))
    fliesX.append(random.randint(32, 968))
    fliesY.append(random.randint(32, 500))


def flies_targets(x, y, i):
    wn.blit(flies[i], (x, y))


# targets butterflies
butterfly = []
butterflyX = []
butterflyY = []
num_butterflies = 4

for j in range(num_butterflies):
    butterfly.append(pygame.image.load("butterfly.png"))
    butterflyX.append(random.randint(32, 968))
    butterflyY.append(random.randint(32, 500))


def butterflies_targets(x, y, j):
    wn.blit(butterfly[j], (x, y))


# targets leaves
leave = []
leaveX = []
leaveY = []
num_leaves = 8

for h in range(num_leaves):
    leave.append(pygame.image.load("leaves.png"))
    leaveX.append(random.randint(32, 968))
    leaveY.append(random.randint(32, 500))


def leave_targets(x, y, h):
    wn.blit(leave[h], (x, y))


# branch1: Y 0-150
branch = pygame.image.load("branch.png")
branch1X = random.randint(0, 1000)
branch1Y = random.randint(10, 150)
branch1X_change = 1
branch1Y_change = 40


def branch1(x, y):
    wn.blit(branch, (x, y))


# collision branch1
def collisionBranch1(branch1X, branch1Y, playerX, playerY):
    distance = math.sqrt(
        (math.pow(branch1X - playerX, 2)) + (math.pow(branch1Y - playerY, 2))
    )
    if distance < 27:
        return True
    else:
        return False


# branch2: Y 200-350
branch2X = random.randint(0, 1000)
branch2Y = random.randint(200, 350)
branch2X_change = 1
branch2Y_change = 40


def branch2(x, y):
    wn.blit(branch, (x, y))


# Collision branch2
def collisionBranch2(branch2X, branch2Y, playerX, playerY):
    distance = math.sqrt(
        (math.pow(branch2X - playerX, 2)) + (math.pow(branch2Y - playerY, 2))
    )
    if distance < 27:
        return True
    else:
        return False


# branch3: Y 400-550
branch3X = random.randint(0, 1000)
branch3Y = random.randint(400, 550)
branch3X_change = 1
branch3Y_change = 40


def branch3(x, y):
    wn.blit(branch, (x, y))


# collision branch3
def collisionBranch3(branch3X, branch3Y, playerX, playerY):
    distance = math.sqrt(
        (math.pow(branch3X - playerX, 2)) + (math.pow(branch3Y - playerY, 2))
    )
    if distance < 27:
        return True
    else:
        return False


# collision with Flies-targets
def collisionFlies(fliesX, fliesY, playerX, playerY):
    distance = math.sqrt(
        (math.pow(fliesX - playerX, 2)) + (math.pow(fliesY - playerY, 2))
    )
    if distance < 35:
        return True
    else:
        return False


# collision with Butterflies-Targerts
def collisionButterflies(butterfliesX, butterfliesY, playerX, playerY):
    distance = math.sqrt(
        (math.pow(butterfliesX - playerX, 2)) + (math.pow(butterfliesY - playerY, 2))
    )
    if distance < 35:
        return True
    else:
        return False


# collision with Leaves-Targets
def collisionLeaves(leavesX, leavesY, playerX, playerY):
    distance = math.sqrt(
        (math.pow(leavesX - playerX, 2)) + (math.pow(leavesY - playerY, 2))
    )
    if distance < 35:
        return True
    else:
        return False


# Game Over
def game_over():
    fontText = pygame.font.Font("freesansbold.ttf", 64)
    gameOverText = fontText.render("GAME OVER", True, (255, 255, 255))
    wn.blit(gameOverText, (280, 300))


# Game running
running = True

while running:
    wn.fill((0, 0, 0))
    wn.blit(background, (0, 0))

    # To Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #

    # Player movements
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        playerY += vel

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    elif isJump:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            if end_jump3:
                jumpCount = 10
                playerY = branch3Y
                isJump = True
            if end_jump2:
                jumpCount = 10
                playerY = branch2Y
                isJump = True
            if end_jump1:
                jumpCount = 10
                playerY = branch1Y
                isJump = True

            else:
                playerY -= (jumpCount**2) * 0.5 * neg
                jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # GAME-OVER
    if score < 0:
        game_over()
        playerX = 436
        playerY = 600

    # Player boundries
    playerX += player_changeX
    if playerX <= 0:
        player_changeX = 1
        playerX += player_changeX
    if playerX >= 936:
        player_changeX = -1
        playerX += player_changeX

    if playerY >= 600:
        playerY = 600

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
    end_jump3 = collisionBranch3(branch3X, branch3Y, playerX, playerY)
    end_jump2 = collisionBranch2(branch2X, branch2Y, playerX, playerY)
    end_jump1 = collisionBranch1(branch1X, branch1Y, playerX, playerY)

    # flies loop
    for i in range(num_flies):
        fliesCollision = collisionFlies(fliesX[i], fliesY[i], playerX, playerY)
        if fliesCollision:
            score += 6
            fliesX[i] = random.randint(0, 968)
            fliesY[i] = random.randint(0, 500)
            if fliesX[i] and fliesY[i] == butterflyX[j] and butterflyY[j]:
                fliesX[i] = random.randint(0, 968)
            print(score)

        flies_targets(fliesX[i], fliesY[i], i)

    # butteflies loop
    for j in range(num_butterflies):
        butterfliesCollision = collisionButterflies(
            butterflyX[j], butterflyY[j], playerX, playerY
        )
        if butterfliesCollision:
            score += 9
            butterflyX[j] = random.randint(0, 968)
            butterflyY[j] = random.randint(0, 500)
            print(score)
        butterflies_targets(butterflyX[j], butterflyY[j], j)

    # leaves loop
    for h in range(num_leaves):
        leavesCollision = collisionLeaves(leaveX[h], leaveY[h], playerX, playerY)
        if leavesCollision:
            score -= 6
            leaveX[h] = random.randint(0, 968)
            leaveY[h] = random.randint(0, 500)
        leave_targets(leaveX[h], leaveY[h], h)

    # function called
    player_moves(playerX, playerY)
    branch1(branch1X, branch1Y)
    branch2(branch2X, branch2Y)
    branch3(branch3X, branch3Y)
    showScore()

    pygame.display.update()
