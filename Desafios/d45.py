# Crie um programa que faça o computador jogar JOKENPÔ com você. ✊(pedra)  🤚(papel)  ✌️(tesoura)


# Importa as funções randint (para gerar número aleatório) e sleep (para pausas entre os prints)
from random import randint
from time import sleep

# Define as opções do jogo
opcoes = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2) # O computador escolhe aleatoriamente um número entre 0 e 2 (correspondente a Pedra, Papel ou Tesoura)

# Mostra o menu para o jogador
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

# Solicita a jogada do jogador
jogador = int(input('Qual é a sua jogada? '))

# Verifica se a jogada é válida
if jogador < 0 or jogador > 2:
    print('\nJOGADA INVÁLIDA! Por favor, escolha entre 0, 1 ou 2.')
else:
    # Animação do "JO-KEN-PO"
    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!\n')
    sleep(0.5)

    # Mostra a jogada do computador e do jogador com base no índice da tupla
    print('-=-' * 12)
    print(f'Computador jogou {opcoes[computador]}')
    print(f'Jogador jogou {opcoes[jogador]}')
    print('-=-' * 12)

    # Lógica para determinar o vencedor com base nas escolhas

    # Se o computador jogou PEDRA
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCE!')
        elif jogador == 2:
            print('COMPUTADOR VENCE!')

    # Se o computador jogou PAPEL
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCE!')

    # Se o computador jogou TESOURA
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCE!')
        elif jogador == 1:
            print('COMPUTADOR VENCE!')
        elif jogador == 2:
            print('EMPATE!')
