# Calcule o valor a ser pago por um aluguel de carro, considerando dias e quilômetros percorridos.

def calcular_preco(dias, km):
    aluguel_dia = dias * 60
    km_rodado = km * 0.15
    valor_total = aluguel_dia + km_rodado

    print(f'\nResumo do aluguel:')
    print(f'Dias alugados: {dias} x R$60,00 = R${aluguel_dia:.2f}')
    print(f'KM rodados: {km:.2f} x R$0,15 = R${km_rodado:.2f}')
    print(f'Total a pagar: R${valor_total:.2f}')


dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram rodados? '))
calcular_preco(dias, km)