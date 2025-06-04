

s = float(input('Qual é seu salário: R$'))

if s >= 1250:
    aumento = s + (s / 100) * 10
else:
    aumento = s + (s / 100) * 15
print(f'Quem ganhava R${s:.2f} passa a ganhar R${aumento:.2f} agora')

