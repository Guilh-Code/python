# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um NÚMERO ENTRE 0 E 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint  # Importa a função randint para gerar números aleatórios

# Gera um número aleatório entre 0 e 10 e guarda na variável numero_secreto
numero_secreto = randint(0, 10)

# Mensagens iniciais para o jogador
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10. \nSerá que você consegue adivinhar qual foi?')

acertou = False  # Variável de controle: False enquanto o jogador não acertar

palpites = 0  # Contador de tentativas

# Enquanto o jogador não acertar o número secreto
while not acertou:
    num_jogador = int(input('Qual é seu palpite? '))  # Lê o palpite do jogador
    palpites += 1  # Incrementa o número de tentativas
    
    if num_jogador == numero_secreto:  # Se o palpite for igual ao número secreto
        acertou = True  # Marca que o jogador acertou
    
    else:
        if num_jogador < numero_secreto:  # Se o palpite for menor que o número secreto
            print('Mais... tente mais uma vez.')
        elif num_jogador > numero_secreto:  # Se o palpite for maior que o número secreto
            print('Menos... Tente mais uma vez.')        

# Quando o jogador acertar, mostra quantas tentativas ele precisou
print(f'Acertou com {palpites} tentativas. Parabéns!')
