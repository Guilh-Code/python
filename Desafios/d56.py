#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - a MÉDIA DE IDADE do grupo
# - Qual é o NOME do homem MAIS VELHO
# - quantas mulheres têm MENOS DE 20 anos


somaidade = 0  # Inicializa a variável que vai acumular a soma das idades
mediaidade = 0  # Inicializa a variável para calcular a média de idades
maioridadehomem = 0  # Inicializa a variável para armazenar a idade do homem mais velho
nomevelho = ''  # Inicializa a variável para armazenar o nome do homem mais velho
totmulher20 = 0  # Inicializa o contador de mulheres com menos de 20 anos

for p in range(1, 5):  # Loop que vai de 1 até 4, ou seja, repete 4 vezes para 4 pessoas
    print(f'----- {p}º PESSOA -----')  # Exibe um título para cada pessoa no loop
    nome = str(input('Nome: ')).strip()  # Pede o nome da pessoa e remove espaços extras
    idade = int(input('Idade: '))  # Pede a idade da pessoa
    sexo = str(input('Sexo [M/F]: ')).strip()  # Pede o sexo da pessoa e remove espaços extras

    somaidade += idade  # Acumula a idade da pessoa para calcular a soma das idades posteriormente
    
    if p == 1 and sexo in 'Mm':  # Se for a primeira pessoa e for um homem, define as variáveis de maior idade
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:  # Se for homem e tiver idade maior que a do homem mais velho, atualiza
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:  # Se for mulher e tiver menos de 20 anos, aumenta o contador
        totmulher20 += 1

mediaidade = somaidade / 4  # Calcula a média das idades, dividindo a soma pelo número total de pessoas (4)
print('-=-' * 16)  # Exibe uma linha para separar as informações finais
print(f'A média de idade do grupo é de {mediaidade} anos.')  # Exibe a média de idades
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')  # Exibe a idade e o nome do homem mais velho
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')  # Exibe o total de mulheres com menos de 20 anos
