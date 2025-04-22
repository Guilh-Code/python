# Crie um programa que faça o computador jogar JOKENPÔ com você. ✊(pedra)  🤚(papel)  ✌️(tesoura)


# Importa as funções randint (para gerar número aleatório) e sleep (para pausas entre os prints)
from random import randint
from time import sleep

# Define as opções possíveis do jogo em uma tupla
itens = ('Pedra', 'Papel', 'Tesoura')

# O computador escolhe aleatoriamente um número entre 0 e 2 (correspondente a Pedra, Papel ou Tesoura)
computador = randint(0, 2)

# Mostra as opções disponíveis para o jogador
print(''' SUAS OPÇÔES:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')

# Recebe a escolha do jogador como um número inteiro
jogador = int(input('Qual é a sua jogada? '))

# Faz a contagem dramática do "JO-KEN-PO"
print('JO')
sleep(1)  # Espera 1 segundo
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

# Imprime uma linha de separação
print('-=-' * 12)

# Mostra a jogada do computador e do jogador com base no índice da tupla
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=-' * 12)

# Lógica para determinar o vencedor com base nas escolhas

# Se o computador jogou PEDRA
if computador == 0:
    if jogador == 0:
        print('EMPATE')  # Ambos jogaram Pedra
    elif jogador == 1:
        print('JOGADOR VENCE')  # Papel vence Pedra
    elif jogador == 2:
        print('COMPUTADOR VENCE')  # Pedra vence Tesoura
    else:
        print('JOGADA INVÁLIDA!')

# Se o computador jogou PAPEL
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')  # Papel vence Pedra
    elif jogador == 1:
        print('EMPATE')  # Ambos jogaram Papel
    elif jogador == 2:
        print('JOGADOR VENCE')  # Tesoura vence Papel
    else:
        print('JOGADA INVÁLIDA!')

# Se o computador jogou TESOURA
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')  # Pedra vence Tesoura
    elif jogador == 1:
        print('COMPUTADOR VENCE')  # Tesoura vence Papel
    elif jogador == 2:
        print('EMPATE')  # Ambos jogaram Tesoura
    else:
        print('JOGADA INVÁLIDA!')
