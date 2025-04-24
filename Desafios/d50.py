# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES. Se o valor digitado for ÍMPAR, desconsidere-o.


soma = 0  # Inicializa a variável 'soma' com 0, ela vai acumular a soma dos números pares
cont = 0  # Inicializa a variável 'cont' com 0, para contar quantos números pares foram digitados

for i in range(1, 7):  # Cria um loop que vai de 1 até 6 (inclusive), ou seja, vai repetir 6 vezes
    num = int(input(f'Digite o {i}º: '))  # Pede ao usuário para digitar um número, mostrando o número da vez
    if num % 2 == 0:  # Verifica se o número digitado é par (resto da divisão por 2 é 0)
        soma = soma + num  # Se for par, adiciona esse número à soma
        cont = cont + 1  # E incrementa o contador de números pares

print(f'Você informou {cont} números PARES e a soma foi {soma}')  # Mostra quantos pares foram digitados e a soma deles
      