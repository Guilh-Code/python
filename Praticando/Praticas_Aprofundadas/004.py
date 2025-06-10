from time import sleep

RESET = "\033[0m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[33m"
CIANO = "\033[96m"
LARANJA = '\033[38;5;208m'


def mostrar_menu():
    print(f'   {AZUL}╔' + '═' * 44 + f'╗{RESET}')
    print(f'   {AZUL}║{RESET}{AZUL}{"CALCULADORA INTERATIVA DE IMC":^44}{RESET}{AZUL}║{RESET}')
    print(f'   {AZUL}╠' + '═' * 44 + f'╣{RESET}')
    print(f'   {AZUL}║{RESET}{"1 - O que é IMC":<44}{AZUL}║{RESET}')
    print(f'   {AZUL}║{RESET}{"2 - Por que o IMC é importante?":<44}{AZUL}║{RESET}')
    print(f'   {AZUL}║{RESET}{"3 - Calcular meu IMC":<44}{AZUL}║{RESET}')
    print(f'   {AZUL}║{RESET}{"4 - Sair":<44}{AZUL}║{RESET}')
    print(f'   {AZUL}╚' + '═' * 44 + f'╝{RESET}')
    print()

def explicar_o_que_e_imc():
    print(f'   {AZUL}╔' + '═' * 45 + f'╗{RESET}')
    print(f'   {AZUL}║{RESET}{VERDE}{'📘 O que é IMC?':^44}{RESET}{AZUL}║{RESET}')
    print(f'   {AZUL}║{"":45}║{RESET}')
    print(f'   {AZUL}║{RESET}{CIANO}{f'  IMC significa Índice de Massa Corporal.':^44}{RESET}{AZUL} ║{RESET}')
    print(f'   {AZUL}║{"":45}║{RESET}')
    print(f"   {AZUL}║{RESET}{f' {AMARELO}É um cálculo que usa seu peso e altura para{RESET}':^44}{AZUL} ║{RESET}{f'\n   {AZUL}║{RESET}  {AMARELO}estimar se você está dentro do peso ideal.{RESET}{AZUL} ║{RESET}':^44}")
    print(f'   {AZUL}╚' + '═' * 45 + f'╝{RESET}')

def importancia_do_imc():
    print(f'   {AZUL}╔' + '═' * 45 + f'╗{RESET}')
    print(f'   {AZUL}║{RESET}{VERDE}{'📌 Por que o IMC é importante?':^44}{RESET}{AZUL}║{RESET}')
    print(f'   {AZUL}║{"":45}║{RESET}')
    print(f'   {AZUL}║{RESET}{CIANO}{f'  O IMC ajuda a identificar riscos de saúde {AZUL} ║{RESET}'}{f'\n{AZUL}   ║{RESET}{CIANO}{'relacionados ao peso.':^44}'}{RESET}{AZUL} ║{RESET}')
    print(f'   {AZUL}║{"":45}║{RESET}')
    print(f"   {AZUL}║{RESET}{f' {AMARELO}{'Ele pode indicar se você está abaixo,':^44}{RESET}'}{AZUL}║{RESET}{f'\n   {AZUL}║{RESET} {AMARELO}{'no peso ideal ou acima do peso.':^44}{RESET}{AZUL}║{RESET}'}")
    print(f'   {AZUL}╚' + '═' * 45 + f'╝{RESET}')

def calcular_imc():
    print(f'   {AZUL}╔' + '═' * 45 + f'╗{RESET}')
    print(f'   {AZUL}║{RESET}{VERDE}{"🧮 Vamos calcular seu IMC!":^43}{RESET}{AZUL}║{RESET}')
    print(f'   {AZUL}║{'':45}║{RESET}')
    print(f'   {AZUL}║{RESET}{CIANO}{"Digite seu peso (kg)":^45}{RESET}{AZUL}║{RESET}')
    print(f'   {AZUL}║{RESET}{CIANO}{"Digite sua altura (m)":^45}{RESET}{AZUL}║{RESET}')
    print(f'   {AZUL}║{'':45}║{RESET}')
    print(f'   {AZUL}╚' + '═' * 45 + f'╝{RESET}')
    print()

    try:
        peso = float(input(f'{AMARELO}Peso (kg){RESET}: {VERDE}'))
        altura = float(input(f'{AMARELO}Altura (m):{RESET} {VERDE}'))
        if altura <= 0:
            print(f"{VERMELHO}Altura inválida! Deve ser maior que zero.{RESET}")
            return
        imc = peso / (altura ** 2)
        print(f'\n{LARANJA}Calculando...{RESET}')
        sleep(1.5)

        print(f'\nSeu IMC é: {imc:.2f}')
        if imc < 18.5:
            print(f'{AZUL}╔' + '═' * 45 + f'╗{RESET}')
            print(f'{AZUL}║{RESET}{VERMELHO}{"CLASSIFICAÇÃO: ABAIXO DO PESO":^45}{RESET}{AZUL}║{RESET}')
            print(f'{AZUL}╠' + '═' * 45 + f'╣{RESET}')
            print(f'{AZUL}║{RESET}{"Você está abaixo do peso ideal.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"Dica: Consulte um nutricionista para":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"avaliar sua alimentação.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}╚' + '═' * 45 + f'╝{RESET}')

        elif imc < 24.9:
            print(f'{AZUL}╔' + '═' * 45 + f'╗{RESET}')
            print(f'{AZUL}║{RESET}{VERDE}{"CLASSIFICAÇÃO: PESO NORMAL":^45}{RESET}{AZUL}║{RESET}')
            print(f'{AZUL}╠' + '═' * 45 + f'╣{RESET}')
            print(f'{AZUL}║{RESET}{"Seu peso está dentro do ideal.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"Dica: Mantenha hábitos saudáveis":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"e pratique atividades físicas.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}╚' + '═' * 45 + f'╝{RESET}')

        elif imc < 29.9:
            print(f'{AZUL}╔' + '═' * 45 + f'╗{RESET}')
            print(f'{AZUL}║{RESET}{AMARELO}{"CLASSIFICAÇÃO: SOBREPESO":^45}{RESET}{AZUL}║{RESET}')
            print(f'{AZUL}╠' + '═' * 45 + f'╣{RESET}')
            print(f'{AZUL}║{RESET}{"Você está acima do peso ideal.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"Dica: Reduza açúcares e se":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"mexa mais no dia a dia.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}╚' + '═' * 45 + f'╝{RESET}')

        elif imc < 34.9:
            print(f'{AZUL}╔' + '═' * 45 + f'╗{RESET}')
            print(f'{AZUL}║{RESET}{LARANJA}{"CLASSIFICAÇÃO: OBESIDADE GRAU 1":^45}{RESET}{AZUL}║{RESET}')
            print(f'{AZUL}╠' + '═' * 45 + f'╣{RESET}')
            print(f'{AZUL}║{RESET}{"Obesidade leve identificada.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"Dica: Mude hábitos com apoio":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"de profissionais de saúde.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}╚' + '═' * 45 + f'╝{RESET}')

        elif imc < 39.9:
            print(f'{AZUL}╔' + '═' * 45 + f'╗{RESET}')
            print(f'{AZUL}║{RESET}{VERMELHO}{"CLASSIFICAÇÃO: OBESIDADE GRAU 2":^45}{RESET}{AZUL}║{RESET}')
            print(f'{AZUL}╠' + '═' * 45 + f'╣{RESET}')
            print(f'{AZUL}║{RESET}{"Obesidade moderada detectada.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"Dica: Acompanhamento médico é":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"essencial para sua saúde.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}╚' + '═' * 45 + f'╝{RESET}')

        else:
            print(f'{AZUL}╔' + '═' * 45 + f'╗{RESET}')
            print(f'{AZUL}║{RESET}{VERMELHO}{"CLASSIFICAÇÃO: OBESIDADE GRAU 3":^45}{RESET}{AZUL}║{RESET}')
            print(f'{AZUL}╠' + '═' * 45 + f'╣{RESET}')
            print(f'{AZUL}║{RESET}{"Obesidade grave (mórbida).":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"Dica: Busque orientação médica":^45}{AZUL}║{RESET}')
            print(f'{AZUL}║{RESET}{"urgente para sua saúde.":^45}{AZUL}║{RESET}')
            print(f'{AZUL}╚' + '═' * 45 + f'╝{RESET}')


    except ValueError:
        print(f"⚠️  {VERMELHO}Entrada inválida! Use apenas números.{RESET}")

def sair_menu():
    r = ''
    while r not in ['S', 'M']:
        print()
        r = str(input(f'{AZUL}Deseja voltar ao menu digite [M] ou para sair [S]:{RESET}{VERDE} ')).upper().strip()
        print()
        if r == 'S':
            print(f'{CIANO}Programa Encerrando... Até a proxima{RESET} :)')
            sleep(1)
            return 'S'  # <-- retorna a decisão
        elif r == 'M':
            return 'M'  # <-- volta para o menu
        else:
            print(f'{VERMELHO}OPÇÃO INVALIDA! Tente novamente.{RESET}')
            sleep(0.3)

while True:
    mostrar_menu()
    opcao = input('Escolha uma opção (1 a 4): ')
    print()

    if opcao == '1':
        explicar_o_que_e_imc()
    elif opcao == '2':
        importancia_do_imc()
    elif opcao == '3':
        calcular_imc()
    elif opcao == '4':
        print(f'{VERDE}Encerrando o programa. Até mais!{RESET} :)')
        break
    else:
        print(f'{VERMELHO}Opção inválida. Tente novamente.{RESET}')

    decisao = sair_menu()
    if decisao == 'S':
        break
    