import sys, pygame
from pygame.locals import *
pygame.init()

fenetre = pygame.display.set_mode((500,500), RESIZABLE)
fond = pygame.image.load("assets/img/map.jpg").convert()
fenetre.blit(fond, (0,0))

perso = pygame.image.load("assets/img/human.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

ennemi = pygame.image.load("assets/img/ennemi.png").convert_alpha()
fenetre.blit(ennemi, (250,250))

flecheUp = pygame.image.load("assets/img/arrow-up.png").convert_alpha()
flecheDown = pygame.image.load("assets/img/arrow-down.png").convert_alpha()
flecheRight = pygame.image.load("assets/img/arrow-right.png").convert_alpha()
flecheLeft = pygame.image.load("assets/img/arrow-left.png").convert_alpha()

son = pygame.mixer.Sound("assets/song/forest.wav")
son.play()
pygame.display.flip()

continuer_jeu = 1
pygame.key.set_repeat(400,30)
while continuer_jeu:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer_jeu = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_perso = position_perso.move(0,10)
            if event.key == K_UP:
                position_perso = position_perso.move(0,-10)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-10,0)
            if event.key == K_RIGHT:
                position_perso = position_perso.move(10,0)
            if fenetre.blit(perso, position_perso) == fenetre.blit(perso, (250,250)):
                continuer_jeu = 0
                print("GAME OVER")
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)
    fenetre.blit(ennemi, (250,250))
    pygame.display.flip()