import pygame
pygame.init()
print('Passa o \033[1;33mpix meu nobre!\033[m: \033[4;32molavoribgodario@gmail.com\033[m')
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()