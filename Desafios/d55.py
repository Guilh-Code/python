# Faça um programa que leia o PESO de CINCO PESSOAS. No final, mostre qual foi o MAIOR e o MENOR peso lidos.


maior = 0  # Variável para armazenar o maior peso lido
menor = 0  # Variável para armazenar o menor peso lido

for p in range(1, 6):  # Loop que vai de 1 até 5 (inclusive), ou seja, para 5 pessoas
    peso = float(input(f'Peso da {p}º pessoa: '))  # Pede o peso da pessoa e converte para float (número com casas decimais)

    if p == 1:  # Se for a primeira pessoa, define o peso dela como maior e menor ao mesmo tempo
        maior = peso
        menor = peso
    else:
        if peso > maior:  # Se o peso atual for maior do que o maior armazenado, atualiza o maior
            maior = peso
        if peso < menor:  # Se o peso atual for menor do que o menor armazenado, atualiza o menor
            menor = peso

# Após o loop, exibe os resultados
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
            