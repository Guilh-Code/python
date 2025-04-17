# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.   O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random, time

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

num_maquina = random.randint(0, 5) # Faz o computador "PENSAR"
num_humano = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar

print('PROCESSANDO...')
time.sleep(2)

if num_maquina == num_humano:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {num_maquina} e não no {num_humano}!')    
    