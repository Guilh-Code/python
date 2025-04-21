# Escreva um programa que leia a velocidade de um carro.   Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.     A multa vai custar R$7.00 por cada Km acima do limite.


vel = float(input('Qual a velocidade do carro? '))  # Pede a velocidade atual do carro e converte para float

excesso = vel - 80  # Calcula quanto a velocidade passou do limite de 80Km/h
multa = excesso * 7  # Calcula o valor da multa: R$7,00 por cada Km/h acima do limite

# Verifica se o carro passou do limite de velocidade
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h') # Aviso de multa
    print(f'Você foi multado! Excedeu {excesso:.2f}Km/h') # Mostra quanto passou do limite
    print(f'A multa é de R${multa:.2f}') # Mostra o valor da multa
else:
    print("Tudo certo! Dirija com segurança.") # Mensagem caso esteja dentro do limite

