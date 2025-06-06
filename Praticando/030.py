from time import sleep

RESET = "\033[0m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[33m"
CIANO = "\033[96m"

# Funções Principais
def menu(num):
    print(f'{AZUL}-=-' * 13)
    print(f'| {'Escolha uma das bases de conversão:':^30} |')
    print(f'|{f'{VERDE}Número atual:{RESET} {num}':^46}{AZUL}|')
    print(f'-=-' * 13)
    print(f'''{AMARELO}[ 1 ] Converter para BÍNARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
[ 4 ] Trocar número
[ 5 ] Sair
{RESET}''')

def sair_menu():
    r = ''
    while r not in ['S', 'M']:
        r = str(input(f'{AZUL}Deseja voltar ao menu digite [M] ou para sair [S]:{RESET}{VERDE} ')).upper().strip()
        if r == 'S':
            print(f'{CIANO}Programa Encerrando... Até a proxima{RESET} :)')
            sleep(1)
            return 'S'  # <-- retorna a decisão
        elif r == 'M':
            return 'M'  # <-- volta para o menu
        else:
            print(f'{VERMELHO}OPÇÃO INVALIDA! Tente novamente.{RESET}')
            sleep(0.3)

def saida_resultados():
    print(f'{AZUL}-=-' * 20)
    print(f"{VERMELHO}Números digitados:{RESET} {', '.join(map(str, lista_num))}")
    print(f'{CIANO}Você converteu para {VERDE}BÍNARIO {c_bin} vezes.{RESET}')
    print(f'{CIANO}Você converteu para {VERDE}OCTAL {c_oct} vezes.{RESET}')
    print(f'{CIANO}Você converteu para {VERDE}HEXADECIMAL {c_hex} vezes.{RESET}')
    print(f'{AZUL}-=-' * 20 )

# Variáveis e Lista
lista_num = []
c_bin = c_oct = c_hex = 0

# Começo do Terminal
print(f'   {AZUL}╔' + '═' * 44 + '╗')
print(f'   {AZUL}║{RESET}{' CONVERSOR DE NÚMEROS ':^44}{AZUL}║')
print(f'   {AZUL}╠' + '═' * 44 + '╣')
print(f'   {AZUL}║{RESET}{'Este programa converte números para:':^44}{AZUL}║')
print(f'   {AZUL}║{RESET}{'- Binário  - Octal  - Hexadecimal -':^44}{AZUL}║')
print(f'   {AZUL}╚' + '═' * 44 + '╝')
print()
num = int(input(f'{AMARELO}Vamos começar! Qual número você quer converter? {RESET} '))

lista_num.append(num)
print(f'{VERDE}{'Um segundo... Carregando Menu 📝':^50}{RESET}')
sleep(2)
print()
print()

# Loop Principal
while True:

    menu(num)
    while True:
        try:
            opcao = int(input(f'Sua opção: '))
            break # Se chegou aqui, é um número inteiro válido
        except ValueError:
            print(f'{VERMELHO}ERRO!{RESET} Só aceitamos números INTEIROS.')

    print(f'{AZUL}-=-' * 20)

    if opcao == 1:
        print(f'{RESET}O número {AMARELO}{num}{RESET} convertido para {VERDE}BÍNARIO{RESET} é igual a {AMARELO}{bin(num)[2:]}{RESET}.')
        c_bin += 1
    elif opcao == 2:
        print(f'{RESET}O número {AMARELO}{num}{RESET} convertido para {VERDE}OCTAL{RESET} é igual a {AMARELO}{oct(num)[2:]}{RESET}.')
        c_oct += 1
    elif opcao == 3:
        print(f'{RESET}O número {AMARELO}{num}{RESET} convertido para {VERDE}HEXADECIMAL{RESET} é igual a {AMARELO}{hex(num)[2:]}{RESET}.')
        c_hex += 1
    elif opcao == 4:
        num = int(input(f'{AMARELO}Digite outro número inteiro:{RESET} '))
        lista_num.append(num)
    elif opcao == 5:
        print(f'{CIANO}Programa Encerrando... Até a proxima{RESET} :)')
        sleep(1)
        break
    else:
        print(f'{VERMELHO}OPÇÃO INVALIDA!{RESET}')
        sleep(1)

    if opcao != 4:
        decisao = sair_menu()
        if decisao == 'S':
            break # <-- quebra o laço externo corretamente
        
saida_resultados()