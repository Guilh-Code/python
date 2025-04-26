# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Valor inválido! Tente novamente.')
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    
print(f'Sexo {sexo} registrado com sucesso!')