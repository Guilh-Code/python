# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


# Define uma função chamada 'area' que recebe dois parâmetros: largura e comprimento
def area(larg, comp):
    
    # Calcula a área multiplicando largura por comprimento
    a = larg * comp
    # Exibe o resultado formatado com as dimensões e a área
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Exibe o título do programa
print('Controle de Terrenos')
# Exibe uma linha de separação com 20 hifens
print('-' * 20)


# Solicita ao usuário que digite a largura do terreno e converte para float
l = float(input('LARGURA (m): '))

# Solicita ao usuário que digite o comprimento do terreno e converte para float
c = float(input('COMPRIMENTO (m): '))

# Chama a função 'area' passando os valores de largura e comprimento fornecidos pelo usuário
area(l, c)
