# Faça um programa que leia NOME E MÉDIA de um aluno, guardando também a SITUAÇÃO em um DICIONÁRIO. No final, mostre o conteúdo da estrutura na tela.


aluno = {}  # Cria um dicionário vazio para armazenar os dados do aluno


aluno['nome'] = str(input('Nome: '))  # Lê o nome do aluno e armazena na chave 'nome'
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))  # Lê a média e armazena na chave 'media'


# Verifica a situação do aluno com base na média e adiciona essa informação ao dicionário
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'


print('-=-' * 20)  # Imprime uma linha decorativa

# Mostra todas as informações armazenadas no dicionário
for k, v in aluno.items():  # Percorre as chaves e valores do dicionário
    print(f' - {k} é igual a {v}')  # Exibe cada chave e seu valor correspondente
