# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))

area = l * a #calcule a área da parede
litros_tinta = area / 2 #pois cada litro é 2m²

print(f'Sua parede tem a dimensão de {l} x {a} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {litros_tinta:.2f} de tinta.')