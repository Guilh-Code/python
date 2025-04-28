# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8


# Exibe o título do programa
print('=' * 35)
print('      SEQUÊNCIA DE FIBONACCI')
print('=' * 35)

# Solicita ao usuário quantos termos da sequência de Fibonacci ele quer ver
n = int(input('Quantos termos você quer mostrar? '))

# Define os dois primeiros termos da sequência de Fibonacci
t1 = 0
t2 = 1

# Exibe os dois primeiros termos
print('~' * 70)
print(f' {t1} -> {t2}', end="")

# Inicializa o contador, já que os dois primeiros termos foram exibidos
contador = 3

# Laço para calcular e exibir os próximos termos da sequência
while contador <= n:
    # Calcula o próximo termo da sequência
    t3 = t1 + t2
    
    # Exibe o próximo termo
    print(f' -> {t3}', end="")
    
    # Atualiza os valores de t1 e t2 para o próximo cálculo
    t1 = t2
    t2 = t3
   
    # Incrementa o contador
    contador += 1

# Exibe a mensagem de finalização
print(' -> FIM')
print('~' * 70)

