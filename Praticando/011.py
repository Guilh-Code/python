# Use um for para somar apenas os números pares entre 1 e 100 e exiba o resultado.


# Listas 
Pares = []
Impar = []


# Variaveis de SOMA
somaPar = 0
somaImpar = 0

# Contagem para verificar números
for i in range(1, 101):
    if i % 2 == 0:
        Pares.append(f'{i}.. ')
        somaPar += i
    else:
        Impar.append(f'{i}.. ')
        somaImpar += i


# Resultados com números PARES
print(f'Os números pares de 1 a 100 foram: ')
for c in Pares:
    print(f'{c}', end='')
print(f'\nA soma de todos eles foram {somaPar}')

print('=-'*35)

# Resultados com números IMPARES
print(f'Os números impares de 1 a 100 foram: ')
for i in Impar:
    print(f'{i}', end='')
print(f'\nA soma de todos eles foram {somaImpar}')
