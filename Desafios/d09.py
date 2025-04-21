# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.


# Pede ao usuário para digitar um número e o armazena como um número inteiro
n = int(input('Tabuada do número: '))

# Exibe a tabuada do número digitado, formatando as linhas da tabuada
# O formato 'n:2' garante que o número da tabuada tenha ao menos 2 espaços para se alinhar
print('-' * 13) 

# Calcula a tabuada do número n e exibe os resultados de 1 a 10
print(f' 1 x {n:2} = {n*1} \n'  # Exibe a multiplicação de 1
      f' 2 x {n:2} = {n*2} \n'  # Exibe a multiplicação de 2
      f' 3 x {n:2} = {n*3} \n'  # Exibe a multiplicação de 3
      f' 4 x {n:2} = {n*4} \n'  # Exibe a multiplicação de 4
      f' 5 x {n:2} = {n*5} \n'  # Exibe a multiplicação de 5
      f' 6 x {n:2} = {n*6} \n'  # Exibe a multiplicação de 6
      f' 7 x {n:2} = {n*7} \n'  # Exibe a multiplicação de 7
      f' 8 x {n:2} = {n*8} \n'  # Exibe a multiplicação de 8
      f' 9 x {n:2} = {n*9} \n'  # Exibe a multiplicação de 9
      f'10 x {n:2} = {n*10}')   # Exibe a multiplicação de 10


print('-' * 13)  

