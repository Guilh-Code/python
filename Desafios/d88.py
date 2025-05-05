# Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES.O programa vai perguntar QUANTOS JOGOS serão gerados e vai sortear 6 NÚMEROS ENTRE 1 E 60 para cada jogo, cadastrando tudo em uma LISTA COMPLETA.


from random import randint  # Importa a função randint para gerar números aleatórios
from time import sleep      # Importa sleep para pausar a execução entre os sorteios

lista = []  # Lista temporária para armazenar os números de cada jogo
jogos = []  # Lista final que armazenará todos os jogos gerados

print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)

quant = int(input('Quantos jogos você quer que eu sorteie? '))  # Pergunta quantos jogos sortear
tot = 1  # Contador para o número de jogos gerados


while tot <= quant:  # Laço para gerar a quantidade de jogos desejada

    cont = 0  # Contador de números únicos sorteados por jogo
    while True:  # Loop até que 6 números únicos sejam gerados
        num = randint(1, 60)  # Gera um número aleatório entre 1 e 60
        
        if num not in lista:  # Garante que o número ainda não foi sorteado neste jogo
            lista.append(num)  # Adiciona o número à lista
            cont += 1  # Incrementa o contador

        if cont >= 6:  # Quando já tiver 6 números no jogo
            break  # Sai do laço interno

    
    lista.sort()  # Ordena os números do jogo atual
    jogos.append(lista[:])  # Adiciona uma cópia do jogo à lista de jogos
    lista.clear()  # Limpa a lista temporária para o próximo jogo
    tot += 1  # Incrementa o contador de jogos


# Exibição dos jogos sorteados
print('-=' * 4, f'SORTEANDO {quant} JOGOS', '-=' * 4)
for i, l in enumerate(jogos):  # Percorre todos os jogos com seus índices
    print(f'Jogo {i+1}: {l}')  # Mostra o jogo atual
    sleep(1)  # Aguarda 1 segundo entre cada exibição (efeito visual)

print('-=' * 5, '< BOA SORTE! >', '-=' * 5)  # Mensagem final
