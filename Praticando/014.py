# Leia dois números e mostre a soma entre eles.

def soma(a, b):
    s = a + b
    print(f'A soma de {a} e {b} é {s}')

c = 0

while True:
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    soma(n1, n2)

    c += 1

    resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'S':
        continue
    elif resp == 'N':
        print('Programa Encerrado!')
        print(f'Você fez {c} somas ao total!')
        break
    else:
        print('Opção Invalida! Tente novamente.')
        