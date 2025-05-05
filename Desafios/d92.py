# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.


from datetime import datetime  # Importa para usar o ano atual automaticamente

dados = {}  # Cria um dicionário vazio para armazenar os dados da pessoa


dados['nome'] = str(input('Nome: '))  # Lê o nome da pessoa
nasc = int(input('Ano de nascimento: '))  # Lê o ano de nascimento
dados['idade'] = datetime.now().year - nasc  # Calcula a idade com base no ano atual

dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))  # Lê o número da CTPS (0 se não tiver)


# Se tiver carteira de trabalho registrada
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))  # Lê o ano em que foi contratado
    dados['salário'] = float(input('Salário: R$'))  # Lê o salário
    # Calcula o ano da aposentadoria com base em 35 anos de contribuição
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('-=' * 30)


# Exibe todos os dados armazenados
for k, v in dados.items():
    print(f'  - {k} tem valor {v}')
