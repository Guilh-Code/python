# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.


# Pede ao usuário para digitar algo e armazena como uma string
a = input('Diga algo: ')


print('O tipo primitivo desse valor é', type(a)) # Exibe o tipo primitivo do valor digitado
print('Só tem espaços? ', a.isspace()) # Verifica se o valor digitado contém apenas espaços
print('É um número? ', a.isnumeric()) # Verifica se o valor digitado é composto apenas por números
print('É alfabético? ', a.isalpha()) # Verifica se o valor digitado é composto apenas por letras
print('É alfanumérico? ', a.isalnum()) # Verifica se o valor digitado é composto por letras e números (alfanumérico)
print('Está em maiúsculas? ', a.isupper()) # Verifica se o valor digitado está em maiúsculas
print('Está em minúsculas? ', a.islower()) # Verifica se o valor digitado está em minúsculas
print('Está capitalizada? ', a.istitle()) # Verifica se o valor digitado está no formato de título (primeira letra de cada palavra maiúscula)
