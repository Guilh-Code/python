# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente..


# Define a função 'ficha' com dois parâmetros:
# 'jog' com valor padrão '<desconhecido>' e 'gol' com valor padrão 0
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato.')


# Solicita ao usuário o nome do jogador
n = str(input('Nome do Jogador: '))
# Solicita ao usuário o número de gols (ainda como string)
g = str(input('Número de Gols: '))


# Verifica se o valor digitado para gols é um número
if g.isnumeric():
    g = int(g)  # Converte para inteiro se for número
else:
    g = 0  # Caso contrário, assume 0 como valor padrão


# Verifica se o nome está vazio (apenas espaços ou nada digitado)
if n.strip() == '':
    ficha(gol=g)  # Chama a função só com gols, nome será <desconhecido>
else:
    ficha(n, g)  # Chama a função com nome e gols informados

