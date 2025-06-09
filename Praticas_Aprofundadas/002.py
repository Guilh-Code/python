RESET = "\033[0m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[33m"

print('-=-' * 15)
print(f'{AZUL}{'PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO':^45}\n{'PARA A COMPRA DE UMA CASA':^45}{RESET}')
print('-=-' * 15)

valor_casa = float(input(f'{AMARELO}Valor da casa?{RESET} {VERDE}R$'))
salario = float(input(f'{AMARELO}Salário do comprador?{RESET} {VERDE}R$'))
anos_pagar = int(input(f'{AMARELO}Quantos anos de financiamento? '))
print(f'{RESET}-=-' * 15)

prestação_mensal = valor_casa / (anos_pagar * 12)
exceder_salario = (salario / 100) * 30

if exceder_salario <= prestação_mensal:
    print(f'---------- 🔴 {VERMELHO}PRESTAÇÃO NEGADA!{RESET} ----------')
    print(f'{AZUL}Motivo:{RESET} Para pagar uma casa de R${valor_casa:.2f} em {anos_pagar} anos, a prestação\nserá de R${prestação_mensal:.2f} e não pode exceder {VERMELHO}30%{RESET} do seu salário de {VERMELHO}R${salario:.2f}{RESET}\n30% do seu salário seria R${VERMELHO}{exceder_salario:.2f}{RESET}!, era necessário que você ganhasse {VERDE}R${prestação_mensal - exceder_salario:.2f}{RESET} a mais para que a prestação de {VERDE}R${prestação_mensal:.2f}{RESET} não ultrapassasse os 30%.')

else:
    print(f'---------- 🟢 {VERDE}PRESTAÇÃO APROVADA!{RESET} ----------')
    print(f'{AZUL}Motivo: {RESET}Para pagar uma casa de R${valor_casa:.2f} em {anos_pagar} anos, a prestação\nserá de {VERDE}R${prestação_mensal:.2f}{RESET} que é menos de 30% do seu salário de {VERDE}R${salario:.2f}{RESET}\n30% do seu salário seria {VERDE}R${exceder_salario:.2f}{RESET}!')

print('Até a próxima prestação! :)')