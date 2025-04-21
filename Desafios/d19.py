# Um professor quer sortear um dos seus quatros alunos para apagar o quadro, Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido


import random  # Importa o módulo 'random' para usar funções que geram resultados aleatórios

# Pede o nome dos quatro alunos e armazena em variáveis
al1 = str(input('O primeiro aluno: '))  
al2 = str(input('O segundo aluno: '))  
al3 = str(input('O terceiro aluno: '))  
al4 = str(input('O quarto aluno: '))  

# Cria uma lista com os nomes dos alunos
lista_alunos = [al1, al2, al3, al4]

# Usa o random.choice() para escolher aleatoriamente um aluno da lista
escolhido = random.choice(lista_alunos)

# Exibe o nome do aluno escolhido
print(f'O aluno escolhido foi {escolhido}')
