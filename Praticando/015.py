# Leia um número e mostre seu dobro, triplo e raiz quadrada.

from math import sqrt

def mostrar_calculos(n):
    dobro = n * 2
    triplo = n * 3
    raiz = sqrt(n)
    print(f'''
NÚMERO ANALISADO: {n}
Dobro : {dobro}
Triplo : {triplo}
Raiz Quadrada : {raiz:.2f}
''')

num = float(input('Digite um número: '))
mostrar_calculos(num)