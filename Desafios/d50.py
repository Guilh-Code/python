# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES. Se o valor digitado for ÍMPAR, desconsidere-o.

soma = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}º: '))
    if num % 2 == 0:
        soma += num
    
print(f'A soma de todos valores pares é {soma}')        