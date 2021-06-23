import pygame, ctypes, random
pygame.init()
clock = pygame.time.Clock()
black = (0,0,0) # RGB of the colour black
green = (0,255,0) # RGB of the colour
white = (255,255,255) # RGB of the colour white
red = (255,0,0)
blue = (135, 206, 235)
user32 = ctypes.windll.user32
window_width = user32.GetSystemMetrics(0)
window_height = user32.GetSystemMetrics(1)
gameDisplay = pygame.display.set_mode((window_width,window_height),pygame.FULLSCREEN)
a = 0


def drawtext(text, x, y, color, size): # function that allows us to draw text, takes into account text, position x, position y, color and size
	myfont = pygame.font.SysFont('Comic Sans MS', size)
	textsurface = myfont.render(text,False, color)
	gameDisplay.blit(textsurface,(x, y))


class Brick(pygame.sprite.Sprite):
	def __init__(self, x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((100,50))
		self.image.fill((red))
		self.rect = self.image.get_rect()
		self.size = self.image.get_rect().size
		self.rect.x = x
		self.rect.y = y
		self.colour = green
		pygame.draw.rect(self.image,self.colour, (0,0,100,50))



class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((40,40))
		self.image.fill((white))
		self.rect = self.image.get_rect()
		self.size = self.image.get_rect().size
		self.rect.x = window_width / 2
		self.rect.y = window_height / 2
		self.list = [-1,1]
		self.difficulty = 1
		self.last_diff = -1
		self.speed_x = 1 * random.choice(self.list)
		self.speed_y = -1
		self.colour = black
		self.score = 0
		pygame.draw.circle(self.image, self.colour, (25,25),12)
		self.paddle_created = 0


	def update(self):
		if self.last_diff != self.difficulty:
			if self.speed_x < 0:
				self.speed_x = -self.difficulty
			if self.speed_y < 0:
				self.speed_y = -self.difficulty
			if self.speed_x > 0:
				self.speed_x = self.difficulty
			if self.speed_y > 0:
				self.speed_y = self.difficulty
			self.last_diff = self.difficulty
		self.rect.y += self.speed_y
		self.rect.x += self.speed_x
		if self.rect.x < 0 or self.rect.x > window_width - self.size[0]:
			self.speed_x = self.speed_x * -1
		if self.rect.y < 0:
			self.speed_y = self.speed_y * -1
		col = pygame.sprite.groupcollide(ball_gp, brick_gp, False, True)
		col2 = pygame.sprite.groupcollide(ball_gp, paddle_gp, False, False)
		if col or col2:
			self.speed_y = self.speed_y * -1
		for i,n in col.items():
			for nn in n:
				self.score += 1



class Paddle(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((100,30))
		self.image.fill((white))
		self.rect = self.image.get_rect()
		self.size = self.image.get_rect().size
		self.rect.x = window_width/2
		self.rect.y = window_width/2 -30
		self.list = [-1,1]
		self.speed_x = 1 * random.choice(self.list)
		self.colour = black
		pygame.draw.rect(self.image, self.colour, (0,0,100,30))


	def update(self):
		pass



def gameover(a):
	gameDisplay.fill(black)
	drawtext("game over", window_width / 2 - 60, window_height / 2, white, 30)
	drawtext("score: " + str(ball.score), window_width/2 - 60, window_height/3, white, 30)
	pygame.draw.rect(gameDisplay,red,((window_width/2)+100,(window_height/2)+150,100,50))

### Exit button drawing
	drawtext("EXIT", (window_width/2)+120,(window_height/2)+160, black, 25)
	mouse_x, mouse_y = pygame.mouse.get_pos()
	if mouse_x > (window_width/2)+100 and mouse_x < (window_width/2)+200 and mouse_y > (window_height/2)+150 and  mouse_y < (window_height/2)+200:
		pygame.draw.rect(gameDisplay,red,((window_width/2)+90,(window_height/2)+140,120,70))
		drawtext("EXIT", (window_width/2)+120,(window_height/2)+160, black, 25)
		if pygame.mouse.get_pressed()[0] == 1:
			 pygame.quit()

### Play button drawing
	pygame.draw.rect(gameDisplay,green,((window_width/2)-100,(window_height/2)+150,100,50))
	drawtext("PLAY",(window_width/2)-80,(window_height/2)+160, black, 25)
	if mouse_x > (window_width/2)-100 and mouse_x < window_width/2 and mouse_y > (window_height/2)+150 and mouse_y < (window_height/2)+200:
		pygame.draw.rect(gameDisplay,green,((window_width/2)-110,(window_height/2)+140,120,70))
		drawtext("PLAY",(window_width/2)-80,(window_height/2)+160, black, 25)
		if pygame.mouse.get_pressed()[0] == 1:
			start()

### ending handling
	if a == 2:
		global time
		time = pygame.time.get_ticks()
		a+=1
	elif ball.score == 18:
		drawtext("time to be completed: " + str(int((time - start_game)/1000)) + "sec", window_width/2 - 100, window_height/4, white, 30)
		print(start_game,time)
	return a


def start():
	global start_game
	start_game = pygame.time.get_ticks()
	global ball_gp,brick_gp,paddle_gp
	ball_gp = pygame.sprite.Group()
	brick_gp = pygame.sprite.Group()
	paddle_gp = pygame.sprite.Group()
	global ball
	for a in range(3):
		starting_pos = 0
		gap = 170
		for i in range(6):
			brick = Brick(starting_pos+gap,70*a)
			brick_gp.add(brick)
			starting_pos=starting_pos+gap
	ball = Ball()
	ball_gp.add(ball)
	paddle = Paddle()
	paddle_gp.add(paddle)
	move = 0
	time = 1
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
				if event.key == pygame.K_LEFT:
					move = -1 - ball.difficulty
				if event.key == pygame.K_RIGHT:
					move = 1 + ball.difficulty
				if event.key == pygame.K_EQUALS:
					ball.difficulty += 1
				if event.key == pygame.K_UP:
					ball.score = 18
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					move = 0
				if event.key == pygame.K_RIGHT:
					move = 0
		paddle.rect.x += move
		if paddle.rect.x < 0 - paddle.size[0]:
			paddle.rect.x = window_width
		if paddle.rect.x > window_width:
			paddle.rect.x =  0 - paddle.size[0]
		if ball.rect.y > window_height or ball.score == 18:
			if a == 0:
				a = 1
			else:
				a = gameover(a)
		else:
			gameDisplay.fill(white)
			drawtext("score: " + str(ball.score), 90, window_height-80, black, 30)
			brick_gp.update()
			brick_gp.draw(gameDisplay)
			ball_gp.update()
			ball_gp.draw(gameDisplay)
			paddle_gp.update()
			paddle_gp.draw(gameDisplay)
		pygame.display.update()

start()
