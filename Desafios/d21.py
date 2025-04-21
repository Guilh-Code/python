# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


import pygame  # Importa a biblioteca pygame, usada para criar jogos e trabalhar com multimídia (como áudio)

pygame.init()  # Inicializa todos os módulos do pygame

pygame.mixer.music.load('des21.mp3')  # Carrega o arquivo de música (precisa estar na mesma pasta ou com caminho correto)
pygame.mixer.music.play()  # Reproduz a música carregada

input()  # Espera o usuário pressionar ENTER (mantém o programa rodando enquanto a música toca)

pygame.event.wait()  # Espera por um evento do pygame (aqui é opcional, já que o input() já pausa)
