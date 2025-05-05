# Crie um programa onde 4 JOGADORES joguem um DADO e tenham resultados ALEATÓRIOS. Guarde esses resultados em um DICIONÁRIO em Python. No final, coloque esse dicionário em ORDEM, sabendo que o VENCEDOR tirou o MAIOR NÚMERO no dado.


from random import randint  # Importa a função para gerar números aleatórios
from time import sleep      # Importa a função sleep para adicionar pausas
from operator import itemgetter  # Importa itemgetter para usar como chave de ordenação


# Dicionário com os valores sorteados para cada jogador
jogo = {
    'Jogador 1': randint(1, 6),  # Sorteia número entre 1 e 6
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

ranking = []  # Lista que receberá os jogadores ordenados


# Exibe os valores sorteados
print('Valores sorteados: ')
for k, v in jogo.items():  # Percorre o dicionário
    print(f'{k} tirou {v} no dado.')  # Mostra o valor de cada jogador
    sleep(1)  # Pausa de 1 segundo entre os prints

# Ordena os jogadores pelo valor sorteado em ordem decrescente
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)


print('-=' * 20)
print('== RANKING DOS JOGADORES ==')


# Exibe o ranking dos jogadores
for i, v in enumerate(ranking):  # Percorre a lista ordenada
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')  # Mostra posição, nome e valor
    sleep(1)  # Pausa de 1 segundo
