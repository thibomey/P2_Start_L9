import pygame
from snake import Snake
from snake import veld_grootte


breedte = 800
hoogte = 600
pygame.init()
kleur_achtergrond = (0,0,0)
spel_snelheid = 5

venster = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Snake')

pygame.time.wait(5000)

def game_lus():
    snake = Snake(breedte/2, hoogte/2)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.x_verandering == 0:
                    snake.x_verandering = -veld_grootte
                    snake.y_verandering = 0
                elif event.key == pygame.K_RIGHT and snake.x_verandering == 0:
                    snake.x_verandering = veld_grootte
                    snake.y_verandering = 0
                elif event.key == pygame.K_UP and snake.y_verandering == 0:
                    snake.y_verandering = -veld_grootte

        snake.beweeg()
        venster.fill(0, 0, 0)
        snake.teken(venster)
        pygame.display.update()
        time.sleep(1/5 )



game_lus()