# Escreva um programa que leia a velocidade de um carro.   Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.     A multa vai custar R$7.00 por cada Km acima do limite.

vel = float(input('Qual a velocidade do carro? '))
excesso = vel - 80 # Calcular o quanto excedeu o limite de velocidade
multa = excesso * 7 # Calcular a multa que vai custar R$7.00 por cada 1Km/h acima do limite

if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você foi multado! Excedeu {excesso:.2f}Km/h')
    print(f'A multa é de R${multa:.2f}')
else:
    print("Tudo certo! Dirija com segurança.")
