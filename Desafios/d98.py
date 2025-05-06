# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1 
# b) de 10 até 0, de 2 em 2 
# c) uma contagem personalizada


# Importa a função sleep do módulo time para pausar a execução do programa
from time import sleep

# Define a função 'contador' com os parâmetros: início (i), fim (f) e passo (p)
def contador(i, f, p):
    
    # Se o passo for negativo, transforma-o em positivo
    if p < 0:
        p *= -1
    # Se o passo for zero, define como 1 para evitar loop infinito
    if p == 0:
        p = 1
    
    # Imprime uma linha de separação
    print('-=' * 20)
    # Mostra uma mensagem com os dados da contagem
    print(f'Contagem de {i} até {f} de {p} em {p}')
    # Pausa de 2 segundos antes de iniciar a contagem
    sleep(2.0)

    
    # Se o início for menor que o fim, faz uma contagem crescente
    if i < f:
        cont = i
        # Enquanto o contador for menor ou igual ao fim, imprime o valor
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)  # Pausa de 0.5 segundo entre os números
            cont += p
        print('FIM!')  # Indica o fim da contagem

    
    # Caso contrário, faz uma contagem decrescente
    else:
        cont = i
        # Enquanto o contador for maior ou igual ao fim, imprime o valor
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)  # Pausa de 0.5 segundo entre os números
            cont -= p
        print('FIM!')  # Indica o fim da contagem


# Chama a função para fazer uma contagem de 1 até 10 com passo 1
contador(1, 10, 1)

# Chama a função para fazer uma contagem de 10 até 0 com passo 2
contador(10, 0, 2)


# Imprime uma linha e uma mensagem para o usuário personalizar a contagem
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')

# Pede ao usuário os valores de início, fim e passo
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

# Chama a função com os valores fornecidos pelo usuário
contador(ini, fim, pas)
