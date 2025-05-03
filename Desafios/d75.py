""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""


# Lendo os números
numeros = (
    int(input('Digite o 1º número: ')),
    int(input('Digite o 2º número: ')),
    int(input('Digite o 3º número: ')),
    int(input('Digite o 4º número: '))
)

# A) Quantas vezes apareceu o 9
print(f'O número 9 apareceu {numeros.count(9)} vez(es).')

# B) Em que posição apareceu o primeiro 3
if 3 in numeros:
    print(f'O número 3 apareceu pela primeira vez na posição {numeros.index(3) + 1}.')
else:
    print('O número 3 não foi digitado.')

# C) Quais são os números pares
print('Números pares digitados:', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ') 
