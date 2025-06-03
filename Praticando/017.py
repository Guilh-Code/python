    # Leia a largura e a altura de uma parede e calcule sua área e a quantidade de tinta necessária para pintá-la.

import math

def calcular_parede(l, a):
    area = a * l
    rendimento_por_lata = 2 * 2

    latas_necessarias = math.ceil(area / rendimento_por_lata)

    print(f'A área da parede é de {area:.2f}m².')
    print(f'Você vai precisar de {latas_necessarias} latas de tinta.')


largura = float(input('Qual a largura: '))
altura = float(input('Qual a altura: '))
calcular_parede(largura, altura)