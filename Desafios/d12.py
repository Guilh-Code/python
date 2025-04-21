# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


# Pede ao usuário o preço do produto e armazena como um número de ponto flutuante
preço = float(input('Qual é o preço do produto: R$'))  

# Calcula o novo preço aplicando um desconto de 5% (preço * 0.05)
novo = preço - (preço * 5 / 100)  

# Alternativamente, você pode calcular diretamente o novo preço com desconto usando a fórmula: novo = preço * 0.95
# Isso aplica o desconto de 5% de uma forma mais direta.

# Exibe o novo preço após o desconto de 5%, formatando o valor com 2 casas decimais
print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}.')

