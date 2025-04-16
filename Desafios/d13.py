# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual é o salário do Funcionário: R$'))
novo = s + (s * 15 / 100)
#a = s * 1.15 #Aumenta 15% do valor digitado

print(f'Um funcionário que ganhava R${s}, com 15% de aumento, passa a receber R${novo:.2f}')