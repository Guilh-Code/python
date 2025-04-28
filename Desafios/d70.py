''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''


total = prod_1000 = menor = cont = 0  # Inicializa variáveis: total da compra, produtos acima de 1000, preço do mais barato e contador de produtos
barato = ''  # Variável para armazenar o nome do produto mais barato

# Cabeçalho da loja
print('-' * 30)
print('      LOJA SUPER BARATÃO')
print('-' * 30)

while True:  # Loop principal para cadastro de produtos

    prod = str(input('Nome do Produto: '))  # Lê o nome do produto
    preço = float(input('Preço: R$'))  # Lê o preço do produto

    cont += 1  # Incrementa o contador de produtos
    total += preço  # Adiciona o preço ao total da compra

    
    if preço > 1000:  # Se o preço for maior que 1000
        prod_1000 += 1  # Incrementa o contador de produtos caros

    
    if cont == 1 or preço < menor:  # Se for o primeiro produto ou se o preço atual for menor que o menor registrado
        menor = preço  # Atualiza o menor preço
        barato = prod  # Atualiza o nome do produto mais barato

    
    # Pergunta se o usuário quer continuar cadastrando
    resp = ' '
    while resp not in 'SN':  # Garante que o usuário digite apenas S ou N
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resp == 'N':  # Se a resposta for N, termina o loop
        break

# Após sair do loop, mostra o resumo da compra
print('{:-^40}'.format('FIM DO PROGRAMA'))  # Imprime "FIM DO PROGRAMA" centralizado e com traços

print(f'O total da compra foi R${total:.2f}')  # Exibe o valor total da compra
print(f'Temos {prod_1000} produtos custando mais de R$1000.00')  # Exibe a quantidade de produtos acima de 1000
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')  # Exibe o produto mais barato e seu preço
