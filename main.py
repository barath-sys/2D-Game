import pygame,os,random,sys
import menu
WIDTH, HEIGHT = 900,600
FPS =  60
speed = 3
score = 0
collide = 0
pygame.init()
window = pygame.display.set_mode((WIDTH,HEIGHT))
BG = pygame.transform.scale(pygame.image.load(os.path.join('assets','nature3.png')),(WIDTH,HEIGHT))
#constants
TILESIZE =32
#apple
apple_image = pygame.image.load('assets/apple.png').convert_alpha()
apple_image = pygame.transform.scale(apple_image,(TILESIZE-7,TILESIZE-7))
apple_rect = apple_image.get_rect(center = (window.get_width()//2,19))

#floor
floor_image = pygame.image.load('assets/floor.png').convert_alpha()
floor_image = pygame.transform.scale(floor_image,(WIDTH,TILESIZE*5))
floor_rect = floor_image.get_rect(bottomleft = (0,window.get_height()+132))
#player
player_image = pygame.image.load('assets/player_static.png').convert_alpha()
player_image = pygame.transform.scale(player_image,(TILESIZE,TILESIZE*2))
player_rect = player_image.get_rect(center = (window.get_width()/2,window.get_height()-TILESIZE*2+4))
class apple():
	def __init__(self,image,position,speed):
		self.image =image
		self.rect= self.image.get_rect(topleft = position)
		#self.position = position
		self.speed = speed
	def move(self):
		self.rect.y += self.speed
apples = [apple(apple_image,(random.randint(20,WIDTH-TILESIZE-250),0),3),apple(apple_image,(random.randint(150,WIDTH-TILESIZE-200),0),3)]
font = pygame.font.Font('assets/PixeloidMono.ttf',32)
hit = pygame.mixer.Sound('assets/powerup.mp3')
hit.set_volume(0.5)
def draw_window():
	global done
	window.blit(BG,(0,0))
	#appl.rect.y +=1	
	window.blit(floor_image,floor_rect)
	window.blit(player_image,player_rect)
	for appl in apples:
		window.blit(appl.image,appl.rect)
	score_text = font.render(f'Score: {score}',True,"white")
	window.blit(score_text,(10,10))
	if collide == 10:
		done = False
		sys.exit()
	pygame.display.update()
def update():
	global speed
	global score
	global collide 
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and  0< player_rect.x:
		player_rect.x-=speed+1
	if keys[pygame.K_RIGHT] and WIDTH-TILESIZE> player_rect.x:
		player_rect.x+=speed+1
	for Apple in apples:
		Apple.move()
		if Apple.rect.colliderect(floor_rect):
			apples.remove(Apple)
			apples.append(apple(apple_image,(random.randint(250,WIDTH-TILESIZE-200),0),speed))
			collide +=1 

		elif Apple.rect.colliderect(player_rect):
			apples.remove(Apple)
			apples.append(apple(apple_image,(random.randint(250,WIDTH-TILESIZE-200),0),speed))
			speed += 0.2
			score += 1
			hit.play()
def main():
	clock = pygame.time.Clock()
	done = True
	while done:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = False
		update()
		draw_window()
		#pygame.display.update()
	pygame.quit()
if __name__ == "__main__":
	menu.starting()
	if menu.starting() == True:
		main()
