# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math #from math import hypot
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))

hi = math.hypot(co, ca)

# Passo a passo (sem usar math.hypot, só o básico):
#quadrado_oposto = cateto_oposto ** 2
#quadrado_adjacente = cateto_adjacente ** 2
#soma_dos_quadrados = quadrado_oposto + quadrado_adjacente
#hipotenusa = math.sqrt(soma_dos_quadrados)

print(f'O comprimento da hipotenusa é {hi:.2f}')