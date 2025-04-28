# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


from random import randint  # Importa função para gerar números aleatórios
from time import sleep  # Importa função para fazer o programa "dormir" (pausar)

# Variáveis de cores
AZUL = '\033[1;34m'
AMARELO = '\033[1;33m'
VERDE = '\033[1;32m'
VERMELHO = '\033[1;31m'
ROXO = '\033[1;35m'
CIANO = '\033[1;36m'
RESET = '\033[m'  # Código para resetar a cor no terminal

v = 0  # Contador de vitórias do jogador

# Imprime cabeçalho do jogo
print(AZUL + '-=-' * 20 + RESET)  # Linha azul
print(AMARELO + '{:^60}'.format('JOGO DO PAR OU ÍMPAR') + RESET)  # Texto centralizado e amarelo
print(AZUL + '-=-' * 20 + RESET)  # Linha azul

# Começa o jogo
while True:
    
    jogador = int(input(CIANO + 'Diga um valor: ' + RESET))  # Jogador escolhe um número (entrada em ciano)
    
    computador = randint(0, 11)  # Computador gera um número aleatório entre 0 e 11
    total = jogador + computador  # Soma dos dois números

    
    tipo = ' '  # Inicializa a variável tipo vazia
    
    while tipo not in 'PI':  # Enquanto o jogador não digitar P ou I corretamente
        tipo = str(input(ROXO + 'Par ou Ímpar? [P/I]: ' + RESET)).strip().upper()[0]  # Entrada em roxo

    # Mostra que o computador está "pensando"
    print(AZUL + '-' * 52 + RESET)
    print(AMARELO + 'PROCESSANDO...' + RESET)
    sleep(1)  # Espera 1 segundo para dar suspense

    
    # Mostra a escolha do jogador e do computador, e o total
    print(f'{CIANO}Você jogou {jogador}{RESET} e {VERMELHO}computador {computador}{RESET}. Total de {total} ', end='')
    
    # Mostra se deu par ou ímpar
    print(VERDE + 'DEU PAR' + RESET if total % 2 == 0 else VERMELHO + 'DEU ÍMPAR' + RESET)

    
    print(AZUL + '-' * 52 + RESET)

    
    # Verifica o resultado com base na escolha do jogador
    if tipo == 'P':  # Se o jogador escolheu PAR
        
        if total % 2 == 0:  # E o total é PAR
            print(VERDE + 'Você VENCEU!' + RESET)
            v += 1  # Aumenta o contador de vitórias

        else:  # Se o total for ÍMPAR
            print(VERMELHO + 'Você PERDEU!' + RESET)
            break  # Sai do loop (fim do jogo)
    
    
    elif tipo == 'I':  # Se o jogador escolheu ÍMPAR
        
        if total % 2 == 1:  # E o total é ÍMPAR
            print(VERDE + 'Você VENCEU!' + RESET)
            v += 1  # Aumenta o contador de vitórias

        else:  # Se o total for PAR
            print(VERMELHO + 'Você PERDEU!' + RESET)
            break  # Sai do loop (fim do jogo)

   
    # Se ainda estiver jogando, exibe mensagem para continuar
    print(ROXO + 'Vamos jogar novamente...' + RESET)
    print(AZUL + '-=-' * 20 + RESET)

# Depois de perder, pausa 1 segundo e mostra quantas vezes venceu
sleep(1)
print(AMARELO + f'GAME OVER! Você venceu {v} vezes.' + RESET)
