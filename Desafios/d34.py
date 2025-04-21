# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.


sal = float(input('Salário do funcionário: R$')) # Pede o salário atual do funcionário e converte para float

# Verifica se o salário é maior ou igual a R$1250
if sal >= 1250:
    novo = sal + (sal * 10 / 100) # Se for, aplica aumento de 10%
else:
    novo = sal + (sal * 15 / 100) # Se for menor que R$1250, aplica aumento de 15%

# Mostra o salário antigo e o novo salário após o reajuste
print(f'Quem ganhava {sal} passa a ganhar R${novo:.2f} agora')
