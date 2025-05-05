# Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA. No final, mostre um BOLETIM contendo a MÉDIA de cada um e permita que o usuário possa mostrar as NOTAS de cada aluno individualmente.


ficha = []  # Lista principal onde serão armazenadas as informações dos alunos

while True:
    nome = str(input('Nome: '))  # Lê o nome do aluno
    nota1 = float(input('Nota 1: '))  # Lê a primeira nota
    nota2 = float(input('Nota 2: '))  # Lê a segunda nota

    media = (nota1 + nota2) / 2  # Calcula a média das duas notas
    ficha.append([nome, [nota1, nota2], media])  # Adiciona os dados na lista: nome, notas, média

    resp = str(input('Quer continuar? [S/N] ')).upper()  # Pergunta se o usuário quer continuar
    if resp == 'N':  # Se digitar N, interrompe o laço
        break


# Impressão do boletim
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')  # Cabeçalho da tabela
print('-' * 26)


for i, a in enumerate(ficha):  # Percorre a lista com índice e dados
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')  # Mostra número do aluno, nome e média com uma casa decimal


# Consulta das notas individuais
while True:
    print('-' * 36)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    
    if opc == 999:  # Condição de parada
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:  # Verifica se o número é válido
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')  # Mostra as duas notas do aluno

print('<<< VOLTE SEMPRE >>>')  # Mensagem final
