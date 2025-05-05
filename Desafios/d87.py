# Aprimore o DESAFIO ANTERIOR, mostrando no final: 
# A) A SOMA de todos os VALORES PARES digitados.
# B) A SOMA dos valores da TERCEIRA COLUNA.
# C) O MAIOR valor da SEGUNDA LINHA.


matriz = [
    [0, 0, 0],  # Linha 0 da matriz
    [0, 0, 0],  # Linha 1
    [0, 0, 0]   # Linha 2
]
spar = mai = scol = 0  # spar = soma dos pares, mai = maior da segunda linha, scol = soma da 3ª coluna


# Preenchendo a matriz com valores do usuário
for linha in range(0, 3):  # Loop pelas 3 linhas
    for coluna in range(0, 3):  # Loop pelas 3 colunas
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        # Armazena o valor digitado na posição correspondente da matriz


print('-=' * 20)  # Separador visual

# Exibindo a matriz formatada e somando os valores pares
for linha in range(0, 3):  # Para cada linha
    for coluna in range(0, 3):  # Para cada coluna
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # Imprime o valor centralizado
        
        if matriz[linha][coluna] % 2 == 0:  # Se o valor for par
            spar += matriz[linha][coluna]  # Adiciona à soma dos pares
    
    print()  # Pula linha após imprimir uma linha da matriz

print('-=' * 20)  # Separador visual

# Exibindo a soma dos valores pares
print(f'A soma dos valores pares é {spar}')


# Soma dos valores da terceira coluna (índice 2)
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {scol}')


# Encontrando o maior valor da segunda linha (índice 1)
for coluna in range(0, 3):
    if coluna == 0:
        mai = matriz[1][coluna]  # Inicializa com o primeiro valor da segunda linha
    elif matriz[1][coluna] > mai:  # Compara os demais valores da segunda linha
        mai = matriz[1][coluna]
print(f'O maior valor da segunda linha é {mai}')
