# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

maior = n1 # Verificando quem é o maior.

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3   

menor = n1 # Verificando quem é o menor.

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('-=-' * 7)
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')  
print('-=-' * 7)      