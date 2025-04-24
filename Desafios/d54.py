# Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. 


from datetime import date  # Importa o módulo 'date' da biblioteca datetime para trabalhar com datas

atual = date.today().year  # Pega o ano atual (ex: 2025) a partir da data de hoje
totmaior = 0  # Inicializa o contador de pessoas maiores de idade
totmenor = 0  # Inicializa o contador de pessoas menores de idade

for pess in range(1, 8):  # Loop que vai de 1 a 7 (inclusive), ou seja, repete 7 vezes
    nasc = int(input(f'Em que ano a {pess}º pessoa nasceu? '))  # Pede o ano de nascimento da pessoa
    idade = atual - nasc  # Calcula a idade da pessoa

    if idade >= 21:  # Verifica se a pessoa tem 21 anos ou mais
        totmaior += 1  # Se sim, soma 1 ao total de maiores de idade
    else:
        totmenor += 1  # Se não, soma 1 ao total de menores de idade

# Depois do loop, exibe o resultado final
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade.')
