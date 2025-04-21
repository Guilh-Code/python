# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# 1. o nome com todas as letras maiúsculas
# 2. O nome com todas minúsculas
# 3. Quantas letras ao todo (sem considerar espaços)
# 4. Quantas letras tem o primeiro nome


nome = str(input('Digite seu nome completo: ')).strip()  
# Pede o nome completo do usuário e remove espaços no início e no fim com .strip()

print('Analisando seu nome...')  # Mensagem de início da análise

print(f'Seu nome em maiúsculo é {nome.upper()} ')  
# Mostra o nome todo em letras maiúsculas

print(f'Seu nome em minúsculo é {nome.lower()}')  
# Mostra o nome todo em letras minúsculas

print(f'Seu nome tem ao todo {(len(nome) - nome.count(" "))} letras')  
# Conta todas as letras do nome (remove os espaços com .count(" "))


# Divide o nome em partes (palavras) e guarda numa lista chamada separa
separa = nome.split()

print(f'Seu primeiro nome é {(separa[0])} e ele tem {len(separa[0])} letras')  
# Mostra o primeiro nome (índice 0 da lista) e conta quantas letras ele tem
