# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.   O programa deverá escrever na tela se o usuário venceu ou perdeu.


import random, time  # Importa os módulos: 'random' para gerar números aleatórios e 'time' para pausar a execução

print('-=-' * 20)  
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')  # Mensagem para o jogador
print('-=-' * 20)  

num_maquina = random.randint(0, 5)  # Computador escolhe um número aleatório entre 0 e 5
num_humano = int(input('Em que número eu pensei? '))  # Jogador digita um número tentando adivinhar

print('PROCESSANDO...')  # Mensagem para criar suspense
time.sleep(2)  # Espera 2 segundos antes de mostrar o resultado

# Verifica se o jogador acertou o número
if num_maquina == num_humano:
    print('PARABÉNS! Você conseguiu me vencer!')  # Mensagem de vitória
else:
    print(f'GANHEI! Eu pensei no número {num_maquina} e não no {num_humano}!')  # Mensagem de derrota
