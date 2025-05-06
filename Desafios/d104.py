# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


# Função que garante a leitura de um número inteiro válido
def leiaInt(msg):
    ok = False     # Flag para controle do loop
    valor = 0      # Variável que armazenará o valor inteiro


    # Loop infinito até receber um valor inteiro válido
    while True:
        n = str(input(msg))  # Recebe a entrada do usuário como string

        # Verifica se o que foi digitado é composto apenas por dígitos
        if n.isnumeric():
            valor = int(n)   # Converte para inteiro
            ok = True        # Marca como entrada válida
        else:
            # Mensagem de erro com cor vermelha (ANSI code)
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


        if ok:
            break  # Sai do loop se a entrada for válida

    return valor  # Retorna o número inteiro lido


# ====== Programa principal ======
# Chamada da função, passando a mensagem desejada
n = leiaInt('Digite um número: ')
# Exibe o número digitado
print(f'Você acabou de digitar o número {n}')
