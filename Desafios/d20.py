# O mesmo professor do desafio anterior quer sortear a ordem de apresentacão de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


import random  # Importa o módulo 'random' para usar funções que geram resultados aleatórios

# Pede o nome de quatro alunos e os armazena em variáveis
al1 = str(input('Primeiro aluno: '))  
al2 = str(input('Segundo aluno: '))  
al3 = str(input('Terceiro aluno: '))  
al4 = str(input('Quarto aluno: '))  

# Cria uma lista com os nomes dos alunos
lista = [al1, al2, al3, al4]

random.shuffle(lista)  # Embaralha (mistura) os nomes na lista de forma aleatória

# Exibe a ordem dos alunos após o embaralhamento
print(f'A ordem de apresentação será\n {lista}')
