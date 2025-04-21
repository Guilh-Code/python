# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.  Ex: Digite um número: 6.127 / O número 6.127 tem a parte inteira 6.


from math import trunc  # Importa a função trunc da biblioteca math, que retorna a parte inteira de um número

# Pede ao usuário para digitar um número e o armazena como um número de ponto flutuante
num = float(input('Digite um número: '))  

# A função trunc() retorna apenas a parte inteira do número, descartando a parte decimal
print(f'O número {num} tem a parte inteira {trunc(num)}')

