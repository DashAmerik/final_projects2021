import pygame, ctypes, random
pygame.init()
clock = pygame.time.Clock()
white = (255,255,255)
red = (255,0,0)
user32 = ctypes.windll.user32
SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.FULLSCREEN)
a = 0
lives = 0
images = ['img\\meteor.png',"img\\purple_meteor.png"]
explosions = []
for i in range(8):
    explosions.append('img\\explosions\\regularExplosion0{}.png'.format(i))
background = pygame.image.load("img\\stary_sky.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))



lifebar = []
for i in range(1,6):
    lifebar.append('img\\lifes\\{}.png'.format(i))


life_img = pygame.image.load(lifebar[4])
life_img = pygame.transform.scale(life_img, (200,50))



def drawtext(text, x, y, color, size):
	myfont = pygame.font.SysFont('Comic Sans MS', size)
	textsurface = myfont.render(text,False, color)
	gameDisplay.blit(textsurface,(x, y))

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img\\spaceship.png')
        self.image = pygame.transform.scale(self.image, (70,110))
        self.rect = self.image.get_rect()
        self.size = self.image.get_rect().size
        self.rect.center = (SCREEN_WIDTH / 2,SCREEN_WIDTH / 2)
        self.speed_x = 5
        self.score = 0
        self.lives = 5

    def update(self):
        curr_x = self.rect.center[0]
        curr_y = self.rect.center[1]
        next_x = curr_x + self.speed_x
        self.rect.center = (next_x,curr_y)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, spaceship_center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img\\bullet.png')
        self.image = pygame.transform.scale(self.image, (20,40))
        self.rect = self.image.get_rect()
        self.size = self.image.get_rect().size
        self.rect.center = spaceship_center
        self.speed_y = 5

    def update(self):
        curr_x = self.rect.center[0]
        curr_y = self.rect.center[1]
        next_y = curr_y - self.speed_y
        self.rect.center = (curr_x, next_y)
        if self.rect.center[1] < 0:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(random.choice(images))
        self.image = pygame.transform.scale(self.image, (80,120))
        self.rect = self.image.get_rect()
        self.size = self.image.get_rect().size
        self.rect.center = (random.randint(0+100, SCREEN_WIDTH-100), -100)
        self.speed_y = speed
        pygame.sprite.spritecollide(self,meteor_gp,True, collided = None)
##
    def update(self):
        curr_x = self.rect.center[0]
        curr_y = self.rect.center[1]
        next_y = curr_y + self.speed_y
        self.rect.center = (curr_x, next_y)
        col = pygame.sprite.spritecollide(self,bullet_gp,False,collided = None)
        if col:
            explosion = Explosion(self.rect.center)
            explosion_gp.add(explosion)
            spaceship.score += 1
        if self.rect.center[1] > SCREEN_HEIGHT + 50:
            self.kill()
            spaceship.lives -=1
            global life_img
            life_img = pygame.image.load(lifebar[spaceship.lives - 1])
            life_img = pygame.transform.scale(life_img, (200,50))
        if self.rect.center[1] > SCREEN_HEIGHT + 50:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(explosions[0])
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.size = self.image.get_rect().size
        self.rect.center = location
        self.frame = 0
        self.frame_rate = 60
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.frame += 1
            self.last_update = now
            if self.frame == len(explosions):
                self.kill()
            else:
                center = self.rect.center
                self.image = pygame.image.load(explosions[self.frame])
                self.rect = self.image.get_rect()
                self.rect.center = center

def start():
    pass

spaceship_gp = pygame.sprite.Group()
spaceship = Spaceship()
spaceship_gp.add(spaceship)
bullet_gp = pygame.sprite.Group()
meteor_gp = pygame.sprite.Group()
explosion_gp = pygame.sprite.Group()

while True:
    col = pygame.sprite.groupcollide(meteor_gp,bullet_gp,True,True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_LEFT:
                if spaceship.speed_x > 0:
                    spaceship.speed_x *= -1
            if event.key == pygame.K_RIGHT:
                if spaceship.speed_x < 0:
                    spaceship.speed_x *= -1
            if event.key == pygame.K_SPACE:
                bullet = Bullet(spaceship.rect.center)
                bullet_gp.add(bullet)
    gen = random.randint(1,1000)
    if gen < 10:
        meteor = Meteor(1)
        meteor_gp.add(meteor)
    if gen < 3:
        meteor = Meteor(2)
        meteor_gp.add(meteor)

    gameDisplay.blit(background, (0,0))
    if spaceship.lives == 0:
        drawtext("GAME OVER", SCREEN_WIDTH/2 - 175, SCREEN_HEIGHT/2 - 55, white, 70)
        for meteor in meteor_gp:
            meteor.kill()
        for bullet in bullet_gp:
            bullet.kill()
        spaceship.kill()

    else:
        gameDisplay.blit(life_img, (SCREEN_WIDTH - 200,0))
        spaceship_gp.update()
        bullet_gp.update()
        meteor_gp.update()
        explosion_gp.update()
        drawtext("score: "+ str(spaceship.score), 10, 10, red, 30)
        spaceship_gp.draw(gameDisplay)
        bullet_gp.draw(gameDisplay)
        meteor_gp.draw(gameDisplay)
        explosion_gp.draw(gameDisplay)
    pygame.display.update()
