# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.


viagem = float(input('Qual é a distância da viagem? '))  # Pede ao usuário a distância da viagem em quilômetros e converte para float

print(f'Você está preste a começar uma viagem de {viagem}Km')  # Exibe a distância da viagem para o usuário

# Verifica se a distância é menor ou igual a 200Km
if viagem <= 200:
    preço = viagem * 0.50  # Se for até 200Km, o preço da passagem é R$0,50 por km
else:
    preço = viagem * 0.45  # Se for maior que 200Km, o preço da passagem é R$0,45 por km

# Exibe o preço total da passagem, formatando para duas casas decimais
print(f'E o preço da sua passagem será de R${preço:.2f}')

