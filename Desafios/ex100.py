# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior..


# Importa as funções randint (para gerar números aleatórios) e sleep (para pausar a execução)
from random import randint
from time import sleep


# Função que sorteia 5 números aleatórios de 1 a 10 e adiciona na lista
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')

    # Loop para sortear 5 números
    for cont in range(0, 5):
        n = randint(1, 10)  # Gera um número aleatório entre 1 e 10
        lista.append(n)     # Adiciona o número na lista
        
        print(f'{n} ', end='', flush=True)  # Exibe o número
        sleep(0.3)  # Pausa de 0.3 segundo entre cada número
    print('PRONTO!')  # Mensagem ao final do sorteio


# Função que soma apenas os valores pares da lista
def somaPar(lista):
    soma = 0  # Variável acumuladora
    
    for valor in lista:  # Percorre cada número da lista
        
        if valor % 2 == 0:  # Verifica se o número é par
            soma += valor   # Soma se for par
    
    # Exibe a lista e o resultado da soma dos pares
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Cria uma lista vazia para armazenar os números sorteados
numeros = []
# Chama a função para sortear números e armazenar na lista
sorteia(numeros)
# Chama a função para somar os valores pares da lista
somaPar(numeros)

