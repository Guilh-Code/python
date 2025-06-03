from random import choice, shuffle

lista = []

for i in range(1, 5):
    n = str(input(f'{i}º aluno: '))
    lista.append(n)

nome_sorteado = choice(lista)
shuffle(lista)

print('-' * 20)
print(f'O aluno escolhido foi {nome_sorteado}')
print(f'A ordem de apresentação será:') 
for c in lista:
    print(f'{c} - ', end='')