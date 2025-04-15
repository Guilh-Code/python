l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))

area = l * a #calcule a área da parede

litros_tinta = area / 2 #pois cada litro é 2m

print(f'A area da parede é {area:.2}m2.')
print(f'Quantidade de tinta necessária é {litros_tinta:.2}m2.')