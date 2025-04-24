# Crie um programa que leia uma frase qualquer e diga se ela é um PALÍNFROMO, desconsiderando os espaços.
# Exemplos de palíndromos:
#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.


frase = str(input('Digite uma frase: ')).strip().upper()  # Pede uma frase ao usuário, remove espaços extras nas pontas e converte tudo para maiúsculas

palavras = frase.split()  # Divide a frase em palavras (usando os espaços como separador), criando uma lista

junto = ''.join(palavras)  # Junta todas as palavras da lista em uma única string, sem espaços

# inverso = junto[::-1]  # (Comentado) Isso seria uma forma rápida de inverter a string usando fatiamento

inverso = ''  # Inicializa a variável que vai guardar a versão invertida da string

for letra in range(len(junto) - 1, -1, -1):  # Loop que percorre a string de trás pra frente
    inverso += junto[letra]  # Adiciona cada letra (de trás pra frente) à variável 'inverso'

print(f'O inverso de {junto} é {inverso}')  # Mostra a string original sem espaços e a sua inversa

if inverso == junto:  # Verifica se a string invertida é igual à original
    print('Temos um palíndromo!')  # Se forem iguais, é um palíndromo
else: 
    print('A frase digitada não é um palíndromo!')  # Se não forem iguais, não é um palíndromo
        