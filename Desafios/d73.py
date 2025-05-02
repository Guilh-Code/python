""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""


tabela = (
    "Flamengo", "Palmeiras", "Bragantino", "Cruzeiro", "Fluminense", "Internacional", "Bahia", "Botafogo", "Ceará SC", "São Paulo", "Vasco da Gama", "Corinthians", "Juventude", "Mirassol", "Fortaleza", "EC Vitória", "Atlético-MG", "Grêmio", "Santos", "Sport Recife"
)
print("=-=" * 24)
print(f"Lista de Times do Brasileirão 2025 : {tabela}")
print("=-=" * 24)

print(f"Os 5 primeiros são {tabela[0:6]}")
print("=-=" * 24)

print(f"Os 4 últimos são {tabela[-4:]}")
print("=-=" * 24)

print(f"Times em ordem alfabética : {sorted(tabela)}")
print("=-=" * 24)

print(f"O Corinthians está na {tabela.index("Corinthians")+1}º posição")