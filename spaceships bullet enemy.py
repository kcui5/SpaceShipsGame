shipImg = pygame.image.load('shipimage.png')
blackBkgd = pygame.image.load('blackbackground.png')
wideBlackBkgd = pygame.image.load('wideblackbackground.png')
bulletImg = pygame.image.load('bullet.png')
enemyImg = pygame.image.load('enemy.png')

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