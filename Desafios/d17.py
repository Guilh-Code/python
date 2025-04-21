# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.


import math  # Importa a biblioteca math, que fornece funções matemáticas, como o cálculo de hipotenusa.

# Pede ao usuário o comprimento do cateto oposto e cateto adjacente e os armazena como números float
co = float(input("Digite o comprimento do cateto oposto: "))  
ca = float(input("Digite o comprimento do cateto adjacente: "))  

# Calcula a hipotenusa usando a função hypot, que já faz o cálculo da hipotenusa de forma otimizada
hi = math.hypot(co, ca)  

# Exibe o comprimento da hipotenusa formatado com 2 casas decimais
print(f'O comprimento da hipotenusa é {hi:.2f}')

