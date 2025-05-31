# Maior número da lista
# Peça 5 números e diga qual é o maior.

maior = int(input('Digite o 1º numero: '))

for i in range(2, 6):
    n = int(input(f'Digite o {i}º numero: '))
    if n > maior:
        maior = n

print(f'O maior numero digitado foi {maior}')