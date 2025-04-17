# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# 1. o nome com todas as letras maiúsculas
# 2. O nome com todas minúsculas
# 3. Quantas letras ao todo (sem considerar espaços)
# 4. Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculo é {nome.upper()} ')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome tem ao todo {(len(nome)-nome.count(' '))} letras')
#print(f'Seu primeiro nome {(nome.find(' '))} letras')
separa = nome.split()
print(f'Seu primeiro nome é {(separa[0])} e ele tem {len(separa[0])} letras')