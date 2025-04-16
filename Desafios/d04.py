# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

a = input('Diga algo: ')
print('O tipo primitivo desse valor é', type(a)) #Mostra o Tipo Primitivo do valor digitado
print('Só tem espaços? ', a.isspace())      #Mostra se foi digitado em espaços
print('É um número? ', a.isnumeric())       #Mostra se foi digitado um número
print('É alfabético? ', a.isalpha())        #Mostra se foi digitado uma palavra/letra
print('É alfanumérico? ', a.isalnum())      #Mostra que foi digitado um número e uma letra
print('Está em maiúsculas? ', a.isupper())  #Mostra que o texto digitado foi em MAIÚSCULO
print('Está em minúsculas? ', a.islower())  #Mostra que o texto digitado foi em MINÚSCULO
print('Está capitalizada? ', a.istitle()) #Mostra que a palavra digitada foi em formato de Título