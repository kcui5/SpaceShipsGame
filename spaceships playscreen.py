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