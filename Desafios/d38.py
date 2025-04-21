# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem: 
# - O PRIMEIRO VALOR é MAIOR
# - O SEGUNDO VALOR é MENOR
# - NÃO EXISTE valor maior, os dois são IGUAIS


n1 = int(input('Primeiro número : ')) # Pede o primeiro número e converte para inteiro
n2 = int(input('Segundo número : ')) # Pede o segundo número e converte para inteiro

if n1 > n2: # Verifica se o primeiro número é maior que o segundo
    print('O PRIMEIRO número é o maior!') # Se for, mostra que o primeiro é o maior
elif n2 > n1: # Se não, verifica se o segundo número é maior
    print('O SEGUNDO número é maior') # Se for, mostra que o segundo é o maior
else: # Se nenhum for maior, então são iguais
    print('os dois são IGUAIS') # Mostra que os dois números são iguais
