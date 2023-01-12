import pygame
from game import Game
import time
import math
pygame.init()


# classe du jeu


# joueur 1

# generer la fenêtre

pygame.display.set_caption("La bagarrrr") # titre + icon
screen = pygame.display.set_mode((1280,720)) # dimensions
background = pygame.image.load("assets/bg.png")

# importer notre bouton pour lancer la partie
play_button = pygame.image.load('assets/buttonplay.png')
play_button = pygame.transform.scale(play_button, (275, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.80)
play_button_rect.y = math.ceil(screen.get_height() / 1.78)

# lancement du jeu
game = Game()




isRunning = True


while isRunning:



    screen.blit(background, (0,0))



    # appliquer les images des projectiles et les faire bouger

    for bullet in game.player1.all_projectiles:
        bullet.move()

    game.player1.all_projectiles.draw(screen)
    game.player2.all_projectiles.draw(screen)

    # verifier si notre jeu a commencé ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)

        # actualiser la barre de vie du joueur
        game.player2.update_health_bar(screen)

        # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)

    #actualisation du display
    pygame.display.flip()

    if game.player1.rect.y != 595 and game.player1.jumpEnd < time.time():

        game.player1.isJump = False
    if game.player1.rect.y != 595 and game.player1.isJump == False:

        game.player1.rect.y += 1

    if game.player1.isJump == True and game.player1.jumpEnd > time.time():
        game.player1.rect.y -= 0.5






    # vérifier les déplacements des joueurs

    if (game.pressed.get(pygame.K_d) and game.player1.rect.x < 1200):
        game.player1.move_right()
    elif (game.pressed.get(pygame.K_q) and game.player1.rect.x > 0):
        game.player1.move_left()


    if (game.pressed.get(pygame.K_RIGHT) and game.player2.rect.x < 1200):
        game.player2.move_right()
    elif (game.pressed.get(pygame.K_LEFT) and game.player2.rect.x > 0):
        game.player2.move_left()

    for event in pygame.event.get():
        # si le joueur close
        if (event.type == pygame.QUIT):
            isRunning = False
            pygame.quit()

        elif (event.type == pygame.KEYDOWN):
            game.pressed[event.key] = True

            #detecter si touche proj est appuyée

            if(event.key == pygame.K_c and game.player1.attack1_last_use < time.time() - game.player1.attack1_cd):
                game.player1.launch_projectile("droite")
                game.player1.attack1_last_use = time.time()
            elif(event.key == pygame.K_x and game.player1.attack1_last_use < time.time() - game.player1.attack1_cd):
                game.player1.launch_projectile("gauche")
                game.player1.attack1_last_use = time.time()
            elif (event.key == pygame.K_w) and game.player1.rect.y == 595:
                game.player1.move_up()
            elif (event.key == pygame.K_f and game.player1.attack3_last_use < time.time() - game.player1.attack3_cd):
                game.player1.launch_attack3()
                game.player1.attack3_last_use = time.time()

            if (event.key == pygame.K_0):
                game.player2.launch_projectile("gauche")

        elif (event.type == pygame.KEYUP):
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
             # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode"lancé"
                game.is_playing = True

