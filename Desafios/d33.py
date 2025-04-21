# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


n1 = int(input('Primeiro número: ')) # Lê o primeiro número e converte para inteiro
n2 = int(input('Segundo número: ')) # Lê o segundo número
n3 = int(input('Terceiro número: ')) # Lê o terceiro número

maior = n1 # Começa assumindo que o primeiro número é o maior

# Compara o segundo número com o "maior" atual
if n2 > maior:
    maior = n2 # Se n2 for maior, atualiza o valor de "maior"
if n3 > maior:
    maior = n3 # Se n3 for maior, atualiza o valor de "maior"   


menor = n1 # Começa assumindo que o primeiro número é o menor

# Compara o segundo número com o "menor" atual
if n2 < menor:
    menor = n2 # Se n2 for menor, atualiza o valor de "menor"
if n3 < menor:
    menor = n3 # Se n3 for menor, atualiza o valor de "menor"

print('-=-' * 7)
print(f'O maior número é {maior}') # Mostra o maior número
print(f'O menor número é {menor}') # Mostra o menor número
print('-=-' * 7)    
  