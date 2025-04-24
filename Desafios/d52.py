# Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO.


num = int(input('Digite um número inteiro: '))

if num / num == 0 and num / 1 == 0:
    print(f'O número {num} é um numero primo.')
else:
    print('Não é primo')