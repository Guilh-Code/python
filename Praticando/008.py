# Peça 5 números ao usuário (um por vez) e mostre a soma total no final.

soma = 0

for i in range(1, 6):
    n = int(input(f'Digite o {i}º número: '))
    soma += n

print(f'A soma de todos números é {soma}')