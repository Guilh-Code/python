# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


num = int(input('Digite um número qualquer: '))  # Pede ao usuário um número e converte para inteiro

# Verifica se o número é divisível por 2 (ou seja, se o resto da divisão por 2 é zero)
if num % 2 == 0:
    print(f'O número {num} é PAR!')  # Se for, o número é par
else:
    print(f'O número {num} é IMPAR')  # Caso contrário, é ímpar

    