# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.


print('-=-' * 7)               # Para ser um triãngulo:
print('ANALISANDO TRIÂNGULO')  # A soma de dois lados tem que ser maior que o terceiro lado.
print('-=-' * 7)

# Lê os comprimentos das três retas
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

print('-=-' * 7)

# Verifica se as retas podem formar um triângulo
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Essas retas PODEM FORMAR um triângulo.')
else:
    print('Essas retas NÂO PODEM FORMAR um triângulos.')
