import pygame
import random
import time
#
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Standard_Swoosh.wav')
mouse_click = pygame.mixer.Sound('click.mp3')
nope_effect = pygame.mixer.Sound('nope.mp3')
clock = pygame.time.Clock()
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
white = (255,255,255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
last_click = 0
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
images = []
start_game = False
num_card_pairs = 2
grid = 0
f = open('highscore.txt', 'r')
highscore = f.read()
highscore = highscore.strip()
highscore = highscore.split(" ")
easy_highscore = highscore[0]
medium_highscore = highscore[1]
hard_highscore = highscore[2]
write_file = True
show_highscore = False
#pygame.mixer.music.play()

def drawtext(text, x, y, color, size):
	myfont = pygame.font.SysFont('Comic Sans MS', size)
	textsurface = myfont.render(text,False, color)
	gameDisplay.blit(textsurface,(x, y))

class Game():
	def __init__(self):
		self.last_click = 0
		self.open_cards = []
		self.attempts = 0


class Cards(pygame.sprite.Sprite):
	def __init__(self,x,y,photo):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((100,100))
		self.photo = photo
		self.future_image = pygame.image.load(photo)
		self.image.fill((0,255,0))
		self.rect = self.image.get_rect()
		self.size = self.image.get_rect().size
		self.rect.center = (x,y)
		self.time_now = 0
		self.transform = False
		self.untransform = False
		self.width = 100
		self.flag = 1
		self.turned = False

	def update(self,events):
		global cards_gp
		curr_pos = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if len(game.open_cards) < 2 and curr_pos[0] > self.rect.center[0]-50 and curr_pos[1]> self.rect.center[1]-50 and curr_pos[0] < self.rect.center[0]+ 50 and curr_pos[1] < self.rect.center[1] + 50:
					self.turned = True
					self.transform = True
					game.open_cards.append(self.photo)
					game.last_click = pygame.time.get_ticks()
					mouse_click.play()
		if self.width == 0:
			self.image = self.future_image

		if self.transform == True:
			self.width -= 5
			if self.width == 0:
				self.flag = -1
			if self.flag == -1:
				self.image = self.future_image
			self.image = pygame.transform.scale(self.image,(self.width * self.flag,100))
			if self.width == -100:
				self.transform = False
				self.width = 100
				self.flag = 1


		self.time_now = pygame.time.get_ticks()
		if len(game.open_cards) > 1:
			if self.time_now > game.last_click + 4000:
				game.attempts += 1
				if game.open_cards[0] == game.open_cards[1]:
					for i in cards_gp:
						if i.photo == game.open_cards[0]:
							i.kill()
							pygame.mixer.music.play()
					game.open_cards = []

				else:
					nope_effect.play()
					for i in cards_gp:
						if i.turned == True:
							i.untransform = True
							i.transform = False
							i.width = 100
							i.flag = 1
							i.turned = False
					game.open_cards = []

		if self.untransform == True:
			self.width -= 5
			if self.width < 0:
				self.flag = -1
				self.image = pygame.Surface((100,100))
				self.image.fill((0,255,0))

			if self.width < -95:
				self.untransform = False
				self.width = 100
				self.flag = 1

			self.image = pygame.transform.scale(self.image,(self.width * self.flag,100))


cards_gp = pygame.sprite.Group()
game = Game()
#pygame.mouse.set_pos()
#pygame.mouse.get_pressed()
#for events in event:
	#if events.type == pygame.MOUSEBUTTONDOWN:

while True:
	time.sleep(0.09)
	ev = pygame.event.get()
	for event in ev:
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
			if event.key == pygame.K_a:
				cards_gp = pygame.sprite.Group()
	gameDisplay.fill(black)


	if start_game == False or draw_buttons == True:
#		if len(cards_gp) == 0:
#			drawtext("it took you "+str(game.attempts)+" attempts", 280, 200, red, 30)
#			drawtext("GAME OVER", 300, 250, red, 30)
#			drawtext("EXIT", (SCREEN_WIDTH/2)+120,(SCREEN_HEIGHT/2)+160, black, 25)

		###EXIT###
		mouse_x, mouse_y = pygame.mouse.get_pos()
		pygame.draw.rect(gameDisplay,red,((SCREEN_WIDTH/2)+100,(SCREEN_HEIGHT/2)+150,100,50))#x,y,length,height
		drawtext("EXIT", (SCREEN_WIDTH/2)+120,(SCREEN_HEIGHT/2)+160, black, 25)
		if mouse_x > (SCREEN_WIDTH/2)+100 and mouse_x < (SCREEN_WIDTH/2)+200 and mouse_y > (SCREEN_HEIGHT/2)+150 and  mouse_y < (SCREEN_HEIGHT/2)+200:
			pygame.draw.rect(gameDisplay,red,((SCREEN_WIDTH/2)+90,(SCREEN_HEIGHT/2)+140,120,70))
			drawtext("EXIT", (SCREEN_WIDTH/2)+120,(SCREEN_HEIGHT/2)+160, black, 25)
			if pygame.mouse.get_pressed()[0] == 1:

				 pygame.quit()

		###Play###
		pygame.draw.rect(gameDisplay,green,((SCREEN_WIDTH/2)-100,(SCREEN_HEIGHT/2)+150,100,50))
		drawtext("HIGHSCORES",(SCREEN_WIDTH/2)-99,(SCREEN_HEIGHT/2)+160, black, 15)

		if mouse_x > (SCREEN_WIDTH/2)-100 and mouse_x < SCREEN_WIDTH/2 and mouse_y > (SCREEN_HEIGHT/2)+150 and mouse_y < (SCREEN_HEIGHT/2)+200:
			pygame.draw.rect(gameDisplay,green,((SCREEN_WIDTH/2)-110,(SCREEN_HEIGHT/2)+140,120,70))
			drawtext("HIGHSCORES",(SCREEN_WIDTH/2)-99,(SCREEN_HEIGHT/2)+160, black, 15)

			if pygame.mouse.get_pressed()[0] == 1:
				mouse_click.play()
				show_highscore = True
				#time_spent = time_spent + curr_game_ticsa
				#start()

		if show_highscore == True :
			drawtext("easy: "+ str(easy_highscore), SCREEN_WIDTH/2, 50, red, 30)
			drawtext("medium: "+ str(medium_highscore), SCREEN_WIDTH/2, 100, red, 30)
			drawtext("hard: "+ str(hard_highscore), SCREEN_WIDTH/2,150, red, 30)
		##3x4###
		x = int(SCREEN_WIDTH/2)
		y = int( SCREEN_HEIGHT/2)
		x1 = int(SCREEN_WIDTH/2+100)
		y1 = int(SCREEN_HEIGHT/2+50)
		pygame.draw.rect(gameDisplay,white,(x,y,100,50))
		drawtext("3 x 4",(SCREEN_WIDTH/2)+20,(SCREEN_HEIGHT/2)+10, black, 25)
		if mouse_x > x and mouse_x < x1 and mouse_y > y and mouse_y < y1:
			pygame.draw.rect(gameDisplay,white,((SCREEN_WIDTH/2)-10,(SCREEN_HEIGHT/2)-10,120,70))
			drawtext("3 x 4",(SCREEN_WIDTH/2)+20,(SCREEN_HEIGHT/2)+10, black, 25)#
			if pygame.mouse.get_pressed()[0] == 1:
				mouse_click.play()
				grid = 1
				draw_buttons = False
				range1 = 3
				range2 = 4
				for i in range(1, 7):
					images.append('images\\cat{}.png'.format(i))
					images.append('images\\cat{}.png'.format(i))

		x = int(SCREEN_WIDTH/2) - 120
		y = int( SCREEN_HEIGHT/2)
		x1 = int(SCREEN_WIDTH/2 - 20)
		y1 = int(SCREEN_HEIGHT/2+50)
		pygame.draw.rect(gameDisplay,white,(x,y,100,50))
		drawtext("2 x 4",x+20,y+10, black, 25)
		if mouse_x > x and mouse_x < x1 and mouse_y > y and mouse_y < y1:
			pygame.draw.rect(gameDisplay,white,(x-10,y-10,120,70))
			drawtext("2 x 4",x+20,y+10, black, 25)
			if pygame.mouse.get_pressed()[0] == 1:
				mouse_click.play()
				grid = 0
				draw_buttons = False
				range1 = 2
				range2 = 4
				for i in range(1, 5):
					images.append('images\\cat{}.png'.format(i))
					images.append('images\\cat{}.png'.format(i))


		x = int(SCREEN_WIDTH/2 + 120)
		y = int( SCREEN_HEIGHT/2)
		x1 = int(SCREEN_WIDTH/2+220)
		y1 = int(SCREEN_HEIGHT/2+50)
		pygame.draw.rect(gameDisplay,white,(x,y,100,50))
		drawtext("4 x 4",x+20,y+10, black, 25)
		if mouse_x > x and mouse_x < x1 and mouse_y > y and mouse_y < y1:
			pygame.draw.rect(gameDisplay,white,(x-10,y-10,120,70))
			drawtext("4 x 4",x+20,y+10, black, 25)
			if pygame.mouse.get_pressed()[0] == 1:
				mouse_click.play()
				grid = 2
				draw_buttons  = False
				range1 = 4
				range2 = 4
				for i in range(1, 9):
					images.append('images\\cat{}.png'.format(i))
					images.append('images\\cat{}.png'.format(i))

		if len(images) > 0:
			start_game = True
			for i in range(range1):
				for a in range(range2):
					image = random.choice(images)
					cards = Cards(SCREEN_WIDTH/2 - 100 + (110 * a),SCREEN_HEIGHT/2 - 100 + (110 * i), image)
					images.remove(image)
					cards_gp.add(cards)
			game.attempts = 0


	if start_game == True:
		cards_gp.draw(gameDisplay)
		cards_gp.update(ev)
		if len(cards_gp) == 0:
			draw_buttons = True
			drawtext("it took you "+str(game.attempts)+" attempts", 280, 200, red, 30)
			drawtext("GAME OVER", 300, 250, red, 30)
			drawtext("EXIT", (SCREEN_WIDTH/2)+120,(SCREEN_HEIGHT/2)+160, black, 25)

			if write_file== True:
				f = open('highscore.txt', 'r')
				highscore = f.read()
				highscore = highscore.strip()
				highscore = highscore.split(" ")
				easy_highscore = highscore[0]
				medium_highscore = highscore[1]
				hard_highscore = highscore[2]

				if game.attempts < int(highscore[grid]):
					if grid == 0:
						easy_highscore = game.attempts
					if grid == 1:
						medium_highscore = game.attempts
					if grid == 2:
						hard_highscore = game.attempts

					f = open('highscore.txt','w')
					highscore = f.write(str("{} {} {}".format(easy_highscore,medium_highscore,hard_highscore)))
					f.close()

					write_file == False

		#	if game.attempts < int(highscore):
		##		f = open('highscore.txt', 'w')
		#		f.write(str(game.attempts))
		#		f.close()


	pygame.display.update()
