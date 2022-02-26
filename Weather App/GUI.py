import pygame
import time

from pygame import display
from weather import location, hum, loc, desc
pygame.init()
WIDTH = 800
HEIGHT = 600
black=(0,0,0)

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))   #setting game display size

background = pygame.image.load('meteo.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  #scale image 
font = pygame.font.Font('comic.ttf', 40)
font_name = pygame.font.match_font('comic.ttf')
game_over = True
game_start = True
machin = "Dakar"
displayword = "Dakar"
score = 0
y_cor = 12
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

def game_front_screen():
    gameDisplay.blit(background, (0,0))
    if not game_over :
        draw_text(gameDisplay, "See you soon!", 90, WIDTH / 2, HEIGHT / 4)
    else:
        draw_text(gameDisplay, "Press any key to begin!", 54, WIDTH / 2, 500)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

while True:
    if game_over:
        if game_start:
            game_front_screen()
        game_start = False
    game_over = False
    background = pygame.image.load('meteo2.jpeg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    gameDisplay.blit(background, (0,0))
    draw_text(gameDisplay, str(desc), 40, WIDTH/2, 50)
    draw_text(gameDisplay, str(loc), 40, WIDTH/2, 5)
    draw_text(gameDisplay, str(hum), 40, WIDTH/2, 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            machin += pygame.key.name(event.key)
            if displayword == machin:
                score += len(displayword)
            else:
                game_front_screen()
                time.sleep(2)
                pygame.quit()
    
    if y_cor < HEIGHT-5:
        pygame.display.update()
    else:
        game_front_screen()
