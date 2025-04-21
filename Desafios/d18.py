# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 


import math  # Importa a biblioteca math, que fornece funções matemáticas avançadas, como seno, cosseno, etc.

# Pede ao usuário para inserir um ângulo (em graus) e o armazena como um número inteiro
ang = int(input('Digite um ângulo que você deseja: º'))  

# Calcula o seno, cosseno e tangente do ângulo
# math.radians converte o ângulo de graus para radianos (necessário para as funções trigonométricas)
seno = math.sin(math.radians(ang))  
cos = math.cos(math.radians(ang))  
tan = math.tan(math.radians(ang))  

# Exibe os resultados de seno, cosseno e tangente com 2 casas decimais
print(f'O ângulo de º{ang} tem o SENO de {seno:.2f}')  
print(f'O ângulo de º{ang} tem o COSSENO de {cos:.2f}')  
print(f'O ângulo de º{ang} tem o TANGENTE de {tan:.2f}')  
