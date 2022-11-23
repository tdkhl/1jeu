import pygame
from game import Game
import time
pygame.init()


# classe du jeu


# joueur 1


# generer la fenêtre

pygame.display.set_caption("La bagarrrr") # titre + icon
screen = pygame.display.set_mode((1280,720)) # dimensions
backround = pygame.image.load("assets/bg.png")

# lancement du jeu
game = Game()




isRunning = True


while(isRunning):



    screen.blit(backround, (0,0))


    #afficher joueurs
    screen.blit(game.player1.image, game.player1.rect)

    # appliquer les images des projectiles et les faire bouger

    for bullet in game.player1.all_projectiles:
        bullet.move()

    game.player1.all_projectiles.draw(screen)
    game.player2.all_projectiles.draw(screen)



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

            if (event.key == pygame.K_0):
                game.player2.launch_projectile("gauche")

        elif (event.type == pygame.KEYUP):
            game.pressed[event.key] = False

