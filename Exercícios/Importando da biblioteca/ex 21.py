# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.

import pygame

pygame.init() # inicializa o pygame
pygame.mixer.music.load("ex21.mp3") # carrega a música
pygame.mixer.music.play() # começa a tocar
pygame.event.wait() # mantém o programa aberto enquanto o evento não termina


