# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


# Tupla com os produtos e seus respectivos preços, alternando entre nome (str) e valor (float)
listagem = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 25,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)


print('-' * 40)

# Centraliza o título no meio de 40 espaços
print(f'{"LISTAGEM DE PREÇOS":^40}')

print('-' * 40)


# Loop que percorre a tupla
for pos in range(0, len(listagem)):
    
    if pos % 2 == 0:
        # Se o índice for par, é o nome do produto
        # Usa alinhamento à esquerda com preenchimento de pontos
        print(f'{listagem[pos]:.<30}', end='')
    
    else:
        # Se o índice for ímpar, é o preço
        # Alinha o preço à direita com 2 casas decimais
        print(f'R${listagem[pos]:>7.2f}')
