import pygame
import random

pygame.init()

random.seed()
screen = pygame.display.set_mode((1200, 700))
textColor = (255, 255, 255)
buttonColor = (192, 192, 192)
largeFont = pygame.font.SysFont("leelawadeeuisemilight", 48)
smallFont = pygame.font.SysFont("leelawadeeuisemilight", 36)
clock = pygame.time.Clock()

def clearScreen(backgroundColor = (0, 0, 0)):
    """Fills entire screen with a single color"""
    screen.fill(backgroundColor)

def drawBackgroundDots():
    numCircles = random.randint(100, 200)
    for i in range(numCircles):
        xCoord = random.randint(0, 1200)
        yCoord = random.randint(0, 700)
        radius = random.randint(1, 6)
        pygame.draw.circle(screen, (255, 255, 255), (xCoord, yCoord), radius)

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
                homeScreenLoop = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if playButtonPos.collidepoint(e.pos):
                    #Press play button
                    homeScreenLoop = False
                    print("Play")

homeScreen()