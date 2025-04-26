# Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


# Códigos ANSI para cores no terminal
vermelho = '\033[91m'
verde = '\033[92m'
amarelo = '\033[93m'
azul = '\033[94m'
roxo = '\033[95m'
reset = '\033[0m'  # Reseta para cor padrão


# Solicita os dois primeiros valores do usuário
n1 = int(input(f"{azul}Digite o primeiro valor: {reset}"))
n2 = int(input(f"{azul}Digite o segundo valor: {reset}"))

opcao = 0  # Inicializa a variável da opção com 0

# Enquanto o usuário não escolher sair (opção 5), o menu continua aparecendo
while opcao != 5:
    
    # Mostra o menu com opções
    print(f"""
{roxo}----- MENU -----
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
{reset}""")
    
    # Lê a opção escolhida pelo usuário
    opcao = int(input(f"{amarelo}>>>>> Qual é a sua opção? {reset}"))
    
    
    # Opção 1: somar os dois números
    if opcao == 1:
        print(f"{verde}A soma de {n1} + {n2} é {n1 + n2}{reset}")
    
    # Opção 2: multiplicar os dois números
    elif opcao == 2:
        print(f"{verde}A multiplicação de {n1} x {n2} é {n1 * n2}{reset}")
    
    # Opção 3: verificar qual dos dois é maior
    elif opcao == 3:
        maior = n1 if n1 > n2 else n2  # Operador ternário para escolher o maior
        print(f"{verde}O maior valor entre {n1} e {n2} é {maior}{reset}")
    
    # Opção 4: permitir que o usuário digite novos números
    elif opcao == 4:
        n1 = int(input(f"{azul}Digite o novo primeiro valor: {reset}"))
        n2 = int(input(f"{azul}Digite o novo segundo valor: {reset}"))
    
    # Opção 5: sair do programa
    elif opcao == 5:
        print(f"{vermelho}Finalizando o programa... Até logo!{reset}")
    
    # Se a opção digitada for inválida
    else:
        print(f"{vermelho}Opção inválida. Tente novamente.{reset}")

# Mensagem final fora do laço
print(f"{verde}Programa encerrado com sucesso!{reset}")

