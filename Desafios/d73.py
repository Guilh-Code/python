""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""


# Tupla contendo os nomes dos times do Brasileirão 2025
tabela = (
    "Flamengo", "Palmeiras", "Bragantino", "Cruzeiro", "Fluminense", "Internacional",
    "Bahia", "Botafogo", "Ceará SC", "São Paulo", "Vasco da Gama", "Corinthians",
    "Juventude", "Mirassol", "Fortaleza", "EC Vitória", "Atlético-MG", "Grêmio",
    "Santos", "Sport Recife"
)

print("=-=" * 24)

# Exibe todos os times na ordem original
print(f"Lista de Times do Brasileirão 2025 : {tabela}")

print("=-=" * 24)

# Mostra os 5 primeiros colocados da tabela (índices de 0 a 4, mas o [0:6] pega até o 5º índice)
print(f"Os 5 primeiros são {tabela[0:5]}")

print("=-=" * 24)

# Mostra os 4 últimos times da tabela
print(f"Os 4 últimos são {tabela[-4:]}")

print("=-=" * 24)

# Mostra os times em ordem alfabética (a função sorted() não altera a tupla original)
print(f"Times em ordem alfabética : {sorted(tabela)}")

print("=-=" * 24)

# Mostra a posição do time Corinthians na tabela (index() retorna a posição começando do 0, por isso somamos 1)
print(f"O Corinthians está na {tabela.index('Corinthians') + 1}ª posição")
