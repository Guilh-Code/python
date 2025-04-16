# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual é o preço do produto: R$'))
novo = preço - (preço * 5 / 100)
#novo = preço * 0.95 #Mostra o valor digitado com 5% de desconto

print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}.')