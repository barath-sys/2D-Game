import pygame
import main
pygame.init() 
WIDTH, HEIGHT = 900,600
pygame.display.set_caption("First Game " )
IMG = pygame.image.load("assets/blur.png")
BG_IMG = pygame.transform.scale(IMG,(WIDTH,HEIGHT))

START = pygame.image.load("assets/start.png")
START_IMG = pygame.transform.scale(START,(130,130))

USER = pygame.image.load("assets/icon2.png")
USER_IMG  = pygame.transform.scale(USER,(98,98))

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.Font("assets/PixeloidMono.ttf",18)
TEXT_COL = (255,255,255)

def draw_text(img,x,y,text_col,title):
	
	name  = font.render("BARATH",True,"#630000")
	
	WIN.blit(title,(WIDTH-200,HEIGHT-80))
	WIN.blit(name,(WIDTH-120,HEIGHT-50))
	WIN.blit(img,(x,y))
def starting():
	game_start =False 
	done = True 
	while done:
		WIN.blit(BG_IMG,(0,0))
		pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if  event.key == pygame.K_SPACE  :
					game_start = True 
			if event.type == pygame.QUIT:
				done = False 
		if game_start :
			return True
					
		else:
			draw_text(START_IMG,WIDTH//2-60,HEIGHT//2-90,TEXT_COL,USER_IMG)
		
		pygame.display.update()
	pygame.quit()
			
