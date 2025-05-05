# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média


galera = []  # Lista para armazenar todas as pessoas
pessoa = {}  # Dicionário temporário para cada pessoa
soma = media = 0  # Variáveis para soma e média de idade


while True:
    pessoa.clear()  # Limpa o dicionário antes de adicionar uma nova pessoa
    pessoa['nome'] = str(input('Nome: ')).title()  # Lê e formata o nome

    
    # Validação do sexo
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]  # Lê apenas a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')

    
    pessoa['idade'] = int(input('Idade: '))  # Lê a idade
    soma += pessoa['idade']  # Soma para cálculo da média depois
    galera.append(pessoa.copy())  # Adiciona uma cópia da pessoa na lista

    
    # Validação da resposta para continuar
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if resp == 'N':
        break  # Encerra o loop principal

print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')


media = soma / len(galera)  # Calcula a média de idade
print(f'B) A média de idade é de {media:5.2f} anos.')


# Lista das mulheres
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()


# Lista das pessoas acima da média
print('D) Lista de pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')  # Identação da linha
        for k, v in p.items():  # Mostra os dados da pessoa
            print(f'{k} = {v} ', end='')
        print()

print('<< ENCERRADO >>')
