# Crie um programa onde o usuário possa digitar SETE VALORES NUMÉRICOS e cadastre-os em uma lista única que mantenha separados os valores PARES e ÍMAPRES. No final, mostre os valores pares e ímpares em ordem CRESCENTE.


num = [
    [],  # Lista para os números pares (índice 0)
    []   # Lista para os números ímpares (índice 1)
]
valor = 0  # Variável para armazenar o valor digitado


for c in range(1, 8):  # Laço para ler 7 valores (de 1 a 7)
    valor = int(input(f'Digite um {c}º valor: '))  # Lê um número inteiro do usuário

    
    if valor % 2 == 0:  # Verifica se o número é par
        num[0].append(valor)  # Adiciona o número na lista de pares
    else:
        num[1].append(valor)  # Adiciona o número na lista de ímpares


print('-=' * 30)  # Imprime uma linha de separação


num[0].sort()  # Ordena a lista de pares em ordem crescente
num[1].sort()  # Ordena a lista de ímpares em ordem crescente


print(f'Os valores PARES digitados foram: {num[0]}')  # Exibe a lista de pares
print(f'Os valores ÍMPARES digitados foram: {num[1]}')  # Exibe a lista de ímpares
