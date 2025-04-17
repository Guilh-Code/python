# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.

viagem = float(input('Qual é a distância da viagem? '))

print(f'Você está preste a começar uma viagem de {viagem}Km')

if viagem <= 200:
    preço = viagem * 0.50    
else:
    preço = viagem * 0.45

print(f'E o preço da sua passagem será de R${preço:.2f}')