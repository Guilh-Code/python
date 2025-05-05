# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


time = []            # Lista que armazena todos os jogadores
jogador = {}         # Dicionário para armazenar dados de um jogador individual
partidas = []        # Lista para armazenar os gols por partida de um jogador


while True:
    
    jogador.clear()  # Limpa o dicionário para reutilizá-lo sem dados anteriores
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    
    partidas.clear()  # Limpa a lista de partidas antes de reutilizar
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))

    
    jogador['gols'] = partidas[:]              # Copia a lista de gols para o dicionário
    jogador['total'] = sum(partidas)          # Soma total de gols marcados
    time.append(jogador.copy())               # Adiciona uma cópia do jogador à lista do time

    
    # Pergunta se o usuário quer continuar
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    
    if resp == 'N':
        break  # Encerra o cadastro se o usuário não quiser continuar



# Exibição do cabeçalho da tabela
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')  # Mostra os campos: nome, gols, total
print()



# Exibição dos dados de todos os jogadores cadastrados
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')           # Código do jogador (posição na lista)
    for d in v.values():
        print(f'{str(d):<15}', end='')  # Mostra nome, lista de gols e total
    print()
print('-' * 40)



# Consulta individual de jogador
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break  # Encerra a consulta
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)

print('<< VOLTE SEMPRE >>')
