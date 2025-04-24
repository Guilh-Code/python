# Faça um programa que calcule a SOMA entre todos os NÚMEROS IMPARES que são MÚLTUPLO DE TRÊS e que se encontram no intervalo de 1 até 500.


soma = 0  # Inicializa a variável 'soma' com 0, ela vai acumular a soma dos números desejados
cont = 0  # Inicializa a variável 'cont' com 0, ela vai contar quantos números foram somados

for impar in range(1, 501, 2):  # Cria um loop de 1 até 500 (inclusive), pulando de 2 em 2 — ou seja, só números ímpares
    if impar % 3 == 0:  # Verifica se o número ímpar é múltiplo de 3
        cont = cont + 1  # Se for múltiplo de 3, incrementa o contador
        soma = soma + impar  # E adiciona esse número à soma

print(f"A soma de todos os {cont} valores solicitados é {soma}")  # Mostra quantos números foram somados e o resultado final
