# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²


# Pede ao usuário a largura da parede e armazena como um número de ponto flutuante
l = float(input('Qual a largura da parede em metros: '))  

# Pede ao usuário a altura da parede e armazena como um número de ponto flutuante
a = float(input('Qual a altura da parede em metros: '))  

# Calcula a área da parede (largura * altura)
area = l * a  

# Calcula a quantidade de tinta necessária, sabendo que cada litro de tinta cobre 2m²
litros_tinta = area / 2  

# Exibe as dimensões da parede e a área calculada, com 2 casas decimais
print(f'Sua parede tem a dimensão de {l} x {a} e sua área é de {area:.2f}m².')

# Exibe a quantidade de tinta necessária para pintar a parede, com 2 casas decimais
print(f'Para pintar essa parede, você precisará de {litros_tinta:.2f} litros de tinta.')

