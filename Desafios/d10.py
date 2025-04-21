# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar.  Considere US$1.00 = R$5.90


# Pede ao usuário quanto dinheiro ele tem na carteira e armazena como um número de ponto flutuante
n = float(input('Quanto dinheiro você tem na carteira? R$'))  

# Exibe o equivalente em dólares (considerando a taxa de câmbio de R$ 5,90 por US$ 1)
# A conversão é feita dividindo o valor em reais (n) pela taxa de câmbio (5,90)
print(f'Com R${n} você pode comprar US${n/5.90:.2f} ')

