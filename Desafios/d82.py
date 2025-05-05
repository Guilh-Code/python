# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


valores = []  # Lista geral com todos os números digitados
par = []      # Lista apenas com os pares
impar = []    # Lista apenas com os ímpares

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)  # Adiciona o número à lista geral
    print('Valor adicionado com sucesso...')
    
    if num % 2 == 0:
        par.append(num)  # Se for par, adiciona à lista de pares
    else:
        impar.append(num)  # Senão, adiciona à lista de ímpares

    # Pergunta ao usuário se quer continuar
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
    if resp != 'S':
        break

# Impressão dos resultados, com listas ordenadas
print('-=-' * 13)
print(f'A lista completa é {sorted(valores)}')
print(f'A lista de pares é {sorted(par)}')
print(f'A lista de ímpares é {sorted(impar)}')
