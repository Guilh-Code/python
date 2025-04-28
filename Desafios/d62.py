# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 TERMOS.


# Exibe o título do programa
print('Gerador de PA')
print('-=-' * 10)  # Linha decorativa

# Solicita ao usuário o primeiro termo e a razão da PA
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

# Inicializa o primeiro termo e o contador
termo = primeiro
cont = 1

# Inicializa o total de termos mostrados e a quantidade inicial de termos a mostrar
total = 0
mais = 10  # Inicia com 10 termos a serem mostrados

# Enquanto a quantidade de termos a mostrar for diferente de 0
while mais != 0:
    total += mais  # Incrementa a quantidade total de termos mostrados
    
    # Exibe os termos da PA até o total solicitado
    while cont <= total:
        print(f'{termo} -> ', end="")  # Exibe o termo atual
        termo += razão  # Calcula o próximo termo da PA
        cont += 1  # Incrementa o contador de termos

    print('PAUSA')  # Indica que a exibição dos termos foi pausada
    
    # Solicita ao usuário quantos termos a mais ele quer ver
    mais = int(input('Quantos termos você quer mostrar a mais? '))

# Exibe a quantidade total de termos mostrados após o término
print(f'Progressão finalizada com {total} termos mostrados')
