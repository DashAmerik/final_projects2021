import pygame, random, time
import win32com.client as wincl


pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()



cannon_sound = pygame.mixer.Sound('sounds\\Heavy Cannon Fire Sound Effect.mp3')
cannon_sound.set_volume(0.1)
pygame.mixer.music.load('sounds\\Bird Singing Sound Effect.mp3')
pygame.mixer.music.set_volume(0.1)
splat_sound = pygame.mixer.Sound('sounds\\Splat Sound.mp3')
splat_sound.set_volume(0.1)

red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
white = (255,255,255)

SCREEN_WIDTH = int(626*1.5)
SCREEN_HEIGHT = int(375*1.5)
say = True
angle = 0
FPS = 100

gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("images\\bg.png")
background = pygame.transform.scale(background,(int(626*1.5),int(375*1.5)))


def drawtext(text, x, y, color, size):
	myfont = pygame.font.SysFont('Comic Sans MS', size)
	textsurface = myfont.render(text,False, color)
	gameDisplay.blit(textsurface,(x, y))



class Clouds(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images\\clouds\\cloud_"+str(random.randint(1,4))+".png")
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.5),int(self.size[1]*0.5)))
		self.rect = self.image.get_rect()
		self.rect.x = -300
		self.rect.y = 50
		pygame.sprite.spritecollide(self,clouds_gp,True, collided = None)


	def update(self):
		self.rect.x += 1
		if self.rect.x > SCREEN_WIDTH + 100:
			self.kill()



class Reload(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images\\reload\\reload0.png")
		self.costume = 0
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.001),int(self.size[1]*0.001)))
		self.rect = self.image.get_rect()
		self.rect.x = SCREEN_WIDTH - 55
		self.rect.y = SCREEN_HEIGHT/2 + 150
		self.angle = 1
		self.frames = 0


	def update(self):
		cannon.shoot_ability = False
		self.frames += 1
		if self.frames < 40:
			self.image = pygame.image.load("images\\reload\\reload"+str(self.costume)+".png")
			self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.05),int(self.size[1]*0.05)))
			if self.costume < 11:
				self.costume += 1
			else:
				self.costume = 0
		else:
			cannon.shoot_ability = True
			self.kill()



class Cannon(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images\\cannon_1.png")
		self.size = self.image.get_rect().size
		self.costume = 0
		self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.7),int(self.size[1]*0.7)))
		self.rect = self.image.get_rect()
		self.rect.x = SCREEN_WIDTH - 125
		self.rect.y = SCREEN_HEIGHT/2 + 40
		self.angle = 0
		self.image = pygame.transform.rotate(self.image, self.angle)
		self.bullets = 20
		self.score = 0
		self.start_animation = False
		self.time1 = pygame.time.get_ticks()
		self.shoot_ability = True


	def update(self, multiplier, change_angle):
		if change_angle == True:
			self.angle += 5 * multiplier
		if self.start_animation == True:
			self.image = pygame.image.load("images\\cannon\\cannon_0"+str(self.costume)+".png")
			self.time2 = pygame.time.get_ticks()
			if self.time2 - self.time1 > 400:
				self.costume += 1
			if self.costume > 9:
				self.start_animation = False
				self.costume = 0
		else:
			self.image = pygame.image.load("images/cannon_1.png")
		self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.7),int(self.size[1]*0.7)))
		self.old_centr = self.rect.center
		self.image = pygame.transform.rotate(self.image, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = self.old_centr




class Bird(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.costume = 1
		self.image = pygame.image.load("images\\birds\\bird_"+str(self.costume)+".png")
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.7),int(self.size[1]*0.7)))
		self.rect = self.image.get_rect()
		self.rect.x = -50
		self.rect.y = random.randint(0,400)
		self.next_pos = -100
		self.direction_change = 1
		self.speed = random.uniform(0.5,2)
		self.time1 = pygame.time.get_ticks()
		self.flip = -1


	def update(self):
		self.time2 = pygame.time.get_ticks()
		if self.time2 - self.time1 > 40:
			self.costume += 1
			if self.costume > 15:
				self.costume = 1
			self.image = pygame.image.load("images\\birds\\bird_"+str(self.costume)+".png")
			self.size = self.image.get_rect().size
			if self.flip == 1:
				self.image = pygame.transform.flip(self.image,True,False)
			self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.7),int(self.size[1]*0.7)))
			self.size = self.image.get_rect()
			self.time1 = self.time2
		self.next_pos = self.next_pos + (self.speed * self.direction_change)
		self.rect.x = self.next_pos
		gen = random.randint(1,1000)
		if gen < 2:
			self.direction_change = self.direction_change * -1
			self.flip *= -1
		col = pygame.sprite.spritecollide(self,core_gp,False,collided = None)
		if col:
			cannon.bullets += random.randint(0,2)
			splat_sound.play()
			self.kill()
			cannon.score +=1



class Core(pygame.sprite.Sprite):
	def __init__(self, gravity, angle):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images\\ball.png")
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.1),int(self.size[1]*0.1)))
		self.rect = self.image.get_rect()
		self.rect.x = SCREEN_WIDTH - 50
		self.rect.y = SCREEN_HEIGHT/2 + 40
		self.angle = angle
		self.gravity = gravity


	def update(self):
		self.rect.x += self.angle
		self.rect.y += self.gravity
		self.gravity += 0.1
		if self.rect.y > SCREEN_HEIGHT:
			self.kill()



clouds_gp = pygame.sprite.Group()
cannon_gp = pygame.sprite.Group()
birds_gp = pygame.sprite.Group()
core_gp = pygame.sprite.Group()
reload_gp = pygame.sprite.Group()

cannon = Cannon()
cannon_gp.add(cannon)
key_release = 0
frame = 0
pygame.mixer.music.play(-1)


while True:
	clock.tick(FPS)
	frame += 1
	gameDisplay.blit(background,(0,0))
	ev = pygame.event.get()
	for event in ev:
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				cannon.update(-1, True)
				angle += 2
			if event.key == pygame.K_DOWN and angle > -18:
				cannon.update(1, True)
				angle -= 2
			if event.key == pygame.K_SPACE:
				if key_release==0:
					when_pressed = frame
					key_release = 1

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				key_release = 0
				when_released = frame
				frames_passed = when_released - when_pressed
				gravity_strength = (frames_passed/3) *-1
				if cannon.shoot_ability == True:
					reload = Reload()
					reload_gp.add(reload)
					cannon.bullets -= 1
					core = Core(gravity_strength, angle)
					core_gp.add(core)
					cannon.start_animation = True
					cannon_sound.play()

	gen = random.randint(1,1000)
	if gen < 3:
		cloud = Clouds()
		clouds_gp.add(cloud)

	if gen < 5:
		birds = Bird()
		birds_gp.add(birds)

	if cannon.bullets < 1:
		if say == True:
			speak = wincl.Dispatch("SAPI.SpVoice")
			speak.Speak("Game Over, you have scored "+str(cannon.score)+ " points")
			say = False
		drawtext("GAME OVER", SCREEN_WIDTH/2 - 175, SCREEN_HEIGHT/2 - 55, white, 70)
		drawtext('score: '+str(cannon.score), SCREEN_WIDTH/2, SCREEN_HEIGHT - 50, red, 30)
		for birds in birds_gp:
			birds.kill()
		for cloud in clouds_gp:
			cloud.kill()
		cannon.kill()
	else:
		clouds_gp.update()
		birds_gp.update()
		core_gp.update()
		reload_gp.update()
		cannon_gp.update(1, False)
		drawtext('score: '+str(cannon.score), 50, SCREEN_HEIGHT - 50, red, 30)
		drawtext('bullets left: '+str(cannon.bullets), 200, SCREEN_HEIGHT - 50, red, 30)
		clouds_gp.draw(gameDisplay)
		core_gp.draw(gameDisplay)
		cannon_gp.draw(gameDisplay)
		birds_gp.draw(gameDisplay)
		reload_gp.draw(gameDisplay)

	pygame.display.update()
