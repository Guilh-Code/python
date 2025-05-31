#Lista de compras
#Peça itens ao usuário até ele digitar “sair”. Mostre a lista final.

lista = []
n = 1

print('LISTA DE COMPRAS')
print('O que deseja comprar? (Digite "sair" para encerrar)')

while True:
    compras = input(f'{n}. ').strip()

    if compras.lower() == 'sair':
        break
    else:
        lista.append(compras)
        n += 1


print('\nSua lista de compras:')
for i, item in enumerate(lista, start=1):
    print(f'{i}. {item}')