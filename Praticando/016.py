# Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

def converter_para_dolar(reais, taxa=5.69):
    dolar = reais / taxa
    print(f'Com R${reais:.2f}, você pode comprar US${dolar:.2f}!')

v = float(input('Quantos reais você tem na carteira? '))
converter_para_dolar(v)