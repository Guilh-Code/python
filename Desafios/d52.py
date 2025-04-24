# Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO.


num = int(input('Digite um número: '))  # Pede ao usuário para digitar um número inteiro e armazena em 'num'

tot = 0  # Inicializa a variável 'tot' para contar quantos divisores o número tem

for c in range(1, num + 1):  # Loop que vai de 1 até o número digitado (inclusive)
    if num % c == 0:  # Verifica se 'num' é divisível por 'c' (ou seja, se o resto da divisão é zero)
        print(f'\033[34m{c} ', end='')  # Se for divisível, imprime o número em azul
        tot += 1  # E soma 1 ao contador de divisores
    else:
        print(f'\033[31m{c} ', end='')  # Se NÃO for divisível, imprime o número em vermelho

# Após o loop, imprime o total de divisões feitas com sucesso (em azul) e uma quebra de linha
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')  # \033[m serve para resetar a cor para o padrão

if tot == 2:  # Se o número foi divisível exatamente 2 vezes (por 1 e por ele mesmo)
    print('E por isso ele É PRIMO!')  # Então ele é um número primo
else:
    print('E por isso ele NÃO É PRIMO')  # Caso contrário, ele não é primo
