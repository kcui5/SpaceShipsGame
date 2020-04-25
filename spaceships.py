import pygame
import sys
import random
import time
import sys

pygame.init()

random.seed(time.time())
screen = pygame.display.set_mode((1200, 700))
textColor = (255, 255, 255)
buttonColor = (192, 192, 192)
largeFont = pygame.font.SysFont("leelawadeeuisemilight", 48)
smallFont = pygame.font.SysFont("leelawadeeuisemilight", 36)
shipImg = pygame.image.load('shipimage.png')
blackBkgd = pygame.image.load('blackbackground.png')
wideBlackBkgd = pygame.image.load('wideblackbackground.png')
bulletImg = pygame.image.load('bullet.png')
enemyImg = pygame.image.load('enemy.png')
clock = pygame.time.Clock()

class Bullet():
    def __init__(self, xpos):
        self.xpos = xpos + 20
        self.ypos = 530
        self.firstTimeUpdating = True
    
    def update(self):
        screen.blit(blackBkgd, (self.xpos, self.ypos))
        self.ypos = self.ypos - 15
        if self.ypos > 10:
            screen.blit(bulletImg, (self.xpos, self.ypos))
        if self.firstTimeUpdating:
            drawShip(self.xpos - 20)
            pygame.display.flip()
            self.firstTimeUpdating = False

    def getX(self):
        return self.xpos
    def getY(self):
        return self.ypos

class Enemy():
    def __init__(self, enemyXPos):
        self.enemyXPos = enemyXPos
        self.enemyYPos = 10

    def update(self, bulletsList):
        screen.blit(blackBkgd, (self.enemyXPos, self.enemyYPos))
        self.enemyYPos = self.enemyYPos + 3
        screen.blit(enemyImg, (self.enemyXPos, self.enemyYPos))
        for bullet in bulletsList:
            if bullet.getX() > self.enemyXPos - 20 and bullet.getX() < self.enemyXPos + 30:
                if bullet.getY() > self.enemyYPos - 20 and bullet.getY() < self.enemyYPos + 50:
                    return False
        return True
    
    def getY(self):
        return self.enemyYPos
    def getX(self):
        return self.enemyXPos


def clearScreen(backgroundColor = (0, 0, 0)):
    """Fills entire screen with a single color"""
    screen.fill(backgroundColor)

def drawBackgroundDots():
    numCircles = random.randint(100, 200)
    for i in range(numCircles):
        print(i)
        xCoord = random.randint(0, 1200)
        yCoord = random.randint(0, 700)
        radius = random.randint(1, 6)
        pygame.draw.circle(screen, (255, 255, 255), [xCoord, yCoord], radius)

def drawShip(x):
    """Draws the spaceship to the screen"""
    screen.blit(shipImg, (x, 600))

def play():
    """Plays the game"""
    clearScreen()
    shipXCoord = 600
    drawShip(shipXCoord)
    pygame.display.flip()
    listOfBullets = []
    listOfEnemies = []
    score = 100

    alive = True
    while alive:
        clock.tick(60)

        #Player and Bullets
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and shipXCoord > 30:
            screen.blit(blackBkgd, (shipXCoord, 600))
            shipXCoord = shipXCoord - 5
            drawShip(shipXCoord)
        elif keys[pygame.K_RIGHT] and shipXCoord < 1100:
            screen.blit(blackBkgd, (shipXCoord, 600))
            shipXCoord = shipXCoord + 5
            drawShip(shipXCoord)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    listOfBullets.append(Bullet(shipXCoord))
        for bullet in listOfBullets:
            bullet.update()

        #Enemies
        if random.randint(0, 1000) > 990:
            listOfEnemies.append(Enemy(random.randint(100, 1100)))
        for enemy in listOfEnemies:
            if not enemy.update(listOfBullets):
                listOfEnemies.remove(enemy)
                screen.blit(blackBkgd, (enemy.getX(), enemy.getY()))
                score += 100
            if enemy.getY() > 535:
                alive = False

        #Score
        scoreText = largeFont.render(f"SCORE: {score}", 1, textColor)
        scoreTextPos = scoreText.get_rect(x=480, y = 100)
        screen.blit(wideBlackBkgd, scoreTextPos)
        screen.blit(scoreText, scoreTextPos)

        pygame.display.flip()
    homeScreen()

def homeScreen():
    """Displays Home Screen"""

    clearScreen()
    drawBackgroundDots()

    welcomeText = largeFont.render("SPACESHIPS", 1, textColor)
    playButtonText = smallFont.render("PLAY", 1, textColor)
    welcomeTextPos = welcomeText.get_rect(x = 480, y = 125)
    playButtonTextPos = playButtonText.get_rect(x = 562, y = 400)
    playButtonPos = pygame.Rect(525, 400, 150, 50)
    pygame.draw.rect(screen, buttonColor, playButtonPos)
    screen.blit(welcomeText, welcomeTextPos)
    screen.blit(playButtonText, playButtonTextPos)
    
    pygame.display.flip()
    homeScreenLoop = True
    while homeScreenLoop:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if playButtonPos.collidepoint(e.pos):
                    #Press play button
                    homeScreenLoop = False
                    play()

homeScreen()