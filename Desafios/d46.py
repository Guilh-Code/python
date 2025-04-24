# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 SEGUNDO entre eles.

from time import sleep

for r in range(10, 0, -1):
    print(r)
    sleep(1)
print('Feliz Ano Novo!!!')    