# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.


matriz = [
    [0, 0, 0],  # Primeira linha da matriz 3x3
    [0, 0, 0],  # Segunda linha
    [0, 0, 0]   # Terceira linha
]


# Preenchendo a matriz com valores informados pelo usuário
for linha in range(0, 3):  # Percorre as linhas da matriz
    for coluna in range(0, 3):  # Percorre as colunas da matriz
        
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        # Recebe um valor e armazena na posição [linha][coluna] da matriz


print('-=' * 20)  # Imprime uma linha decorativa para separar entrada da saída


# Exibindo a matriz formatada
for linha in range(0, 3):  # Percorre as linhas da matriz
    for coluna in range(0, 3):  # Percorre as colunas
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # Imprime o valor centralizado em 5 espaços
    print()  # Pula para a próxima linha após imprimir uma linha da matriz
