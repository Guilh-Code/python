# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


# Pede ao usuário o número de dias e os quilômetros rodados e os armazena como inteiros e float
dias = int(input('Quantos dias alugados? '))  
Km = float(input('Quantos Km rodados? '))  

# Calcula o total a pagar: 
# 60 reais por dia alugado e 0,15 reais por cada quilômetro rodado
pago = (dias * 60) + (Km * 0.15)  

# Exibe o valor total a pagar, formatando para duas casas decimais
print(f'O total a pagar é de R${pago:.2f}')

