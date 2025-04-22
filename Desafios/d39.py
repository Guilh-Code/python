# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele AINDA VAI SE ALISTAR ao serviço militar.
# - Se é a HORA DE SE ALISTAR.
# - Se já PASSOU DO TEMPO do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date  # Importa a classe 'date' do módulo 'datetime' para trabalhar com datas

atual = date.today().year  # Pega o ano atual usando a data de hoje (ex: 2025) e guarda em 'atual'

nasc = int(input('Ano de nascimento? '))  # Pergunta o ano de nascimento ao usuário e converte a resposta para inteiro
idade = atual - nasc  # Calcula a idade subtraindo o ano de nascimento do ano atual

# Exibe uma mensagem com o ano de nascimento e a idade atual
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')

# Verifica se a pessoa tem exatamente 18 anos
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!')

# Verifica se a pessoa ainda não completou 18 anos
elif idade < 18:
    saldo = 18 - idade  # Calcula quantos anos faltam para o alistamento
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo  # Determina o ano em que o alistamento ocorrerá
    print(f'Seu alistamento será em {ano}.')

# Caso a idade seja maior que 18, ou seja, o prazo de alistamento já passou
elif idade > 18:
    saldo = idade - 18  # Calcula quantos anos se passaram desde o ano do alistamento
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo  # Determina o ano em que o alistamento deveria ter ocorrido
    print(f'Seu alistamento foi em {ano}.')
