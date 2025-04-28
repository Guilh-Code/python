# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles (desconsiderando o flag).

# Inicializa o contador de números e a soma
contador = soma = 0

# Define a flag para controlar o loop
flag = True

# Enquanto a flag for verdadeira, o loop continua
while flag:
    # Solicita um número ao usuário
    num = int(input('Digite um número [999 para parar!]: '))
    
    # Verifica se o número digitado é o valor de parada
    if num == 999:
        flag = False  # Se for 999, altera a flag para sair do loop
    
    else:
        soma += num       # Soma o número digitado à variável soma
        contador += 1     # Incrementa o contador de números digitados

# Exibe o resultado final após o fim do loop
print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')
