# Crie um programa que mostre na tela TODOS OS NÚMEROS PARES que estão no intervalo entre 1 e 50.


for numero in range(0,51):
    if numero % 2 == 0:
        print(numero, end=" ")