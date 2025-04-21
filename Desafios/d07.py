# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.


# Pede ao usuário para digitar a primeira nota do aluno e armazena como um número de ponto flutuante
n1 = float(input('Primeira nota do aluno: '))

# Pede ao usuário para digitar a segunda nota do aluno e armazena como um número de ponto flutuante
n2 = float(input('Segunda nota do aluno: '))

# Calcula a média das duas notas
m = (n1 + n2) / 2

# Exibe a média das duas notas, formatando o resultado com 1 casa decimal
print(f'A média entre {n1} e {n2} é igual {m:.1f}')

