# Um professor quer sortear um dos seus quatros alunos para apagar o quadro, Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

al1 = str(input('O primeiro aluno: '))
al2 = str(input('O segundo aluno: '))
al3 = str(input('O terceiro aluno: '))
al4 = str(input('O quarto aluno: '))

lista_alunos = [al1, al2, al3, al4]
escolhido = random.choice(lista_alunos)

print(f'O aluno escolhido foi {escolhido}')