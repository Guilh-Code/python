# Peça 6 números ao usuário.
# No final, diga quantos deles eram pares.


par = 0

for i in range(1, 7):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        par += 1

print(f'Dos números citados, {par} eram pares')