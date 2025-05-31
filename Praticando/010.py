# Peça um número e use um while para fazer a contagem regressiva até 0.

n = int(input('Digite um número: '))

while True:
    print(f'{n}...')
    if n != 0:
        n -= 1
    else:
        break
