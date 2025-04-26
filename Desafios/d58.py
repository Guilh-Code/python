# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um NÚMERO ENTRE 0 E 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint

num_jogador = int(input('Tenta adivinhar o número secreto: '))
numero_secreto = randint(1, 10)
tentativas = 0

while num_jogador != numero_secreto:
    print('Errou! Tente novamente.')
    num_jogador = int(input('Tenta adivinhar o número secreto: '))
    tentativas += 1
    
print('ACERTOU!!! Parábens')
print(f'{tentativas} tentativas e 1 acerto')
