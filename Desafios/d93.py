# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


jogador = {}  # Dicionário para armazenar os dados do jogador
partidas = []  # Lista para armazenar a quantidade de gols por partida

# Coleta o nome do jogador
jogador['nome'] = str(input('Nome do Jogador: '))

# Coleta o número de partidas jogadas
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))


# Loop para registrar os gols de cada partida
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))


# Adiciona as informações ao dicionário
jogador['gols'] = partidas[:]  # Cria uma cópia da lista de gols
jogador['total'] = sum(partidas)  # Soma total de gols

# Impressão do dicionário completo (modo de debug)
print('-=' * 30)
print(jogador)
print('-=' * 30)

# Exibe os campos e seus valores
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)


# Exibe o relatório das partidas
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
