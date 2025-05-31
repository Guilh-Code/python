# Peça para o usuário digitar um número entre 1 e 10.
#Se ele digitar algo fora disso, continue pedindo até ele digitar corretamente.


while True:
    n = int(input('Digite um número entre 1 e 10: '))
    if 1 <= n <= 10:
        print('Número valido!')
        break
    else:
        print('Inválido. Tente novamente.')