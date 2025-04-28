# Refaça o DESAFIO 51, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.


# Exibe o título do programa
print('Gerador de PA')
print('-=-' * 10)  # Linha decorativa

# Solicita ao usuário o primeiro termo e a razão da PA
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

# Inicializa o primeiro termo da PA
termo = primeiro
# Inicializa o contador
cont = 1

# Laço para mostrar os 10 primeiros termos da PA
while cont <= 10:
    print(f'{termo} -> ', end="")  # Mostra o termo atual e continua na mesma linha
    termo += razão  # Calcula o próximo termo da PA
    cont += 1       # Incrementa o contador

# Após o laço, exibe a mensagem de fim
print('FIM')

