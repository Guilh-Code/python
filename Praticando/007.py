# Peça um número ao usuário e mostre a tabuada desse número de 1 a 10.

n = int(input('Qual tabuada você deseja ver? '))
for i in range(1,11):
    print(f'{i} x {n} = {n*i}')