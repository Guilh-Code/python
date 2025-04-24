# Crie um programa que mostre na tela TODOS OS NÚMEROS PARES que estão no intervalo entre 1 e 50.


for numero in range(0, 51):  # Cria um loop que vai de 0 até 50 (o 51 não é incluído), um número por vez
    if numero % 2 == 0:  # Verifica se o número é par (ou seja, se o resto da divisão por 2 é zero)
        print(numero, end=" ")  # Imprime o número na mesma linha, separado por espaço (em vez de pular linha)
print('Acabou')  # Depois que o loop termina, imprime "Acabou"
        