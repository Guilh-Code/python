# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar.  Considere US$1.00 = R$5.90

n = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${n} você pode comprar US${n/5.90:.3f} ')