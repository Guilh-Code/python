'''Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''


temp = []  # Lista temporária para armazenar nome e peso de uma pessoa
princ = []  # Lista principal que vai armazenar todas as sublistas (cada pessoa)
mai = men = 0  # Variáveis para armazenar maior e menor peso


while True:  # Laço infinito até que o usuário decida parar
    temp.append(str(input('Nome: ')))  # Adiciona o nome digitado na lista temporária
    temp.append(float(input('Peso: ')))  # Adiciona o peso digitado na lista temporária

    
    if len(princ) == 0:  # Se for a primeira pessoa cadastrada
        mai = men = temp[1]  # Define o peso dessa pessoa como maior e menor
    
    else:
        if temp[1] > mai:  # Se o peso atual for maior que o maior já registrado
            mai = temp[1]  # Atualiza o maior peso
        if temp[1] < men:  # Se o peso atual for menor que o menor já registrado
            men = temp[1]  # Atualiza o menor peso       

    
    princ.append(temp[:])  # Adiciona uma cópia da lista temp na lista principal
    temp.clear()  # Limpa a lista temp para a próxima entrada

    resp = str(input('Quer continuar? [S/N] ')).upper()  # Pergunta se o usuário quer continuar e transforma a resposta em maiúscula
    if resp in 'N':  # Se a resposta for 'N', encerra o laço
        break

print('-=' * 25)  # Imprime uma linha de separação
print(f'Ao todo , você cadastrou {len(princ)} pessoas.')  # Mostra o número de pessoas cadastradas


print(f'O maior peso foi de {mai}Kg. Peso de ', end='')  # Mostra o maior peso registrado
for p in princ:  # Percorre todas as pessoas cadastradas
    if p[1] == mai:  # Se o peso da pessoa for igual ao maior peso
        print(f'[{p[0]}] ', end='')  # Imprime o nome da pessoa com maior peso
print()  # Pula linha


print(f'O menor peso foi de {men}Kg. Peso de ', end='')  # Mostra o menor peso registrado
for p in princ:  # Percorre todas as pessoas cadastradas
    if p[1] == men:  # Se o peso da pessoa for igual ao menor peso
        print(f'[{p[0]}] ', end='')  # Imprime o nome da pessoa com menor peso
print()  # Pula linha final
