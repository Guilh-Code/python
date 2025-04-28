''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''


tot18 = totH = totM20 = 0  # Inicializa os contadores: maiores de 18, homens e mulheres com menos de 20 anos


while True:  # Loop infinito até que o usuário decida parar
    
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')  # Cabeçalho de cadastro
    print('-' * 25)

    i = int(input('IDADE: '))  # Pergunta a idade da pessoa
    
    s = ' '  # Inicializa a variável sexo
    while s not in 'MF':  # Enquanto o usuário não digitar M ou F corretamente
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]  # Pega apenas a primeira letra em maiúsculo


    # Agora que idade e sexo foram capturados:
    if i >= 18:  # Se a pessoa tem 18 anos ou mais
        tot18 += 1  # Incrementa o contador de maiores de idade

    if s == 'M':  # Se a pessoa é do sexo masculino
        totH += 1  # Incrementa o contador de homens

    if i < 20 and s == 'F':  # Se for mulher e tiver menos de 20 anos
        totM20 += 1  # Incrementa o contador de mulheres com menos de 20 anos

    
    print('-' * 25)
    
    # Pergunta se o usuário quer continuar cadastrando
    resp = ' '
    while resp not in 'SN':  # Enquanto a resposta não for S ou N
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # Pega somente a primeira letra

    if resp == 'N':  # Se o usuário quiser parar
        break  # Sai do loop

# Depois que o loop termina, mostra os resultados finais
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {tot18}')  # Mostra quantas pessoas têm mais de 18 anos
print(f'Ao todo temos {totH} homens cadastrados')  # Mostra quantos homens foram cadastrados
print(f'E temos {totM20} mulheres com menos de 20 anos')  # Mostra quantas mulheres com menos de 20 anos foram cadastradas
