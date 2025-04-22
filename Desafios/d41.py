# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atetla e mostre sua categoria, de acordo com a idade:
# - Até 9 ANOS: MIRIM
# - Até 14 ANOS: INFANTIL
# - Até 19 ANOS: JUNIOR
# - Até 25 ANOS: SÊNIOR
# - ACIMA: MASTER 


from datetime import date  # Importa a classe 'date' do módulo 'datetime' para lidar com datas

atual = date.today().year  # Pega o ano atual (ex: 2025) usando a data de hoje
nasc = int(input('Ano de nascimento: '))  # Pergunta o ano de nascimento do atleta e converte para inteiro
idade = atual - nasc  # Calcula a idade do atleta com base no ano atual e ano de nascimento

# Mostra a idade calculada
print(f'O atleta tem {idade} anos.')

# Verifica em qual categoria o atleta se encaixa de acordo com a idade
if idade <= 9:
    print('Classificação: MIRIM')  # Menor que 9 anos

elif idade <= 14:
    print('Classificação: INFANTIL')  # Entre 10 e 14 anos 

elif idade <= 19:
    print('Classificação: JUNIOR')  # Entre 15 e 19 anos 

elif idade <= 25:
    print('Classificação: SÊNIOR')  # Entre 20 e 25 anos 

else:
    print('Classificação: MASTER')  # Maior que 26 anos
   