# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


# Importa apenas a função randint da biblioteca random
from random import randint

# Cria uma tupla com 5 números aleatórios entre 1 e 100
numeros = (
    randint(1, 100),
    randint(1, 100),
    randint(1, 100),
    randint(1, 100),
    randint(1, 100)
)

# Exibe os números sorteados
print('Os valores sorteados foram: ', end='')  # Não pula linha ao final
for n in numeros:
    print(f'{n} ', end='')  # Mostra os números um ao lado do outro

# Mostra o maior valor da tupla usando a função max()
print(f"\nO maior valor sorteado foi {max(numeros)}")

# Mostra o menor valor da tupla usando a função min()
print(f"O menor valor sorteado foi {min(numeros)}")
