# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles (desconsiderando o flag).


contador = soma = 0  # Inicializa as variáveis contador e soma com 0

while True:  # Inicia um loop infinito
    num = int(input('Digite um número [999 para sair]: '))  # Pede para o usuário digitar um número

    if num == 999:  # Se o número digitado for 999, interrompe o loop
        break

    soma += num  # Adiciona o número digitado à variável soma
    contador += 1  # Incrementa o contador (conta quantos números válidos foram digitados)

# Após o loop terminar (quando o usuário digitar 999), mostra a quantidade de números e a soma total
print(f'Você digitou {contador} números e a soma entre eles foi {soma}!')
