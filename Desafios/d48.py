# Faça um programa que calcule a SOMA entre todos os NÚMEROS IMPARES que são MÚLTUPLO DE TRÊS e que se encontram no intervalo de 1 até 500.

soma = 0
for impar in range(1, 501):
    if impar % 2 == 1 and impar % 3 == 0:
         soma += impar
print(f"A soma dos números ímpares múltiplos de 3 entre 1 e 500 é: {soma}")        