# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

import math #from math import radians, sin, cos, tan
ang = int(input('Digite um ângulo que você deseja: º'))

seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'O ângulo de º{ang} tem o SENO de {seno:.2}')
print(f'O ângulo de º{ang} tem o COSSENO de {cos:.2}')
print(f'O ângulo de º{ang} tem o TANGENTE de {tan:.2}')