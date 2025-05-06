# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


# Importa a função sleep do módulo time para pausar a execução entre os prints
from time import sleep


# Define a função 'maior' que aceita uma quantidade variável de argumentos (*num)
def maior(*num):
    
    # Inicializa os contadores de quantidade e maior valor
    cont = maior = 0

    # Imprime uma linha de separação
    print('-=' * 20)
    # Mensagem informando que os valores estão sendo analisados
    print('Analisando os valores passados...')
    

    # Percorre todos os valores passados como argumento
    for valor in num:
        # Mostra cada valor com uma pequena pausa
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        
        # Se for o primeiro valor, define como maior
        if cont == 0:
            maior = valor
        else:
            # Compara e atualiza o maior valor, se necessário
            if valor > maior:
                maior = valor
        
        # Incrementa o contador de valores
        cont += 1
    
    # Exibe o total de valores informados
    print(f'Foram informados {cont} valores ao todo.')
    # Exibe qual foi o maior valor encontrado
    print(f'O maior valor informado foi {maior}.')


# Testes da função com diferentes quantidades de argumentos
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
