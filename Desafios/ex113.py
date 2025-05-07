# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


# Função para ler um número inteiro com tratamento de erros
def leiaInt(msg):
    while True:  # Loop infinito até o usuário digitar um valor válido
        try:
            n = int(input(msg))  # Tenta converter a entrada para inteiro
        except (ValueError, TypeError):  # Captura erro se digitar algo que não seja inteiro
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue  # Reinicia o loop
        except (KeyboardInterrupt):  # Captura se o usuário interromper com Ctrl+C
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0  # Retorna 0 como valor padrão
        else:
            return n  # Retorna o número válido digitado


# Função para ler um número real (float) com tratamento de erros
def leiaFloat(msg):
    while True:  # Loop infinito até o usuário digitar um valor válido
        try:
            n = float(input(msg))  # Tenta converter a entrada para float
        except (ValueError, TypeError):  # Captura erro se digitar algo inválido
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue  # Reinicia o loop
        except (KeyboardInterrupt):  # Captura se o usuário interromper com Ctrl+C
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0  # Retorna 0 como valor padrão
        else:
            return n  # Retorna o número válido digitado

# Chama a função leiaInt para ler um número inteiro do usuário
n1 = leiaInt('Digite um Inteiro: ')

# Chama a função leiaFloat para ler um número real do usuário
n2 = leiaFloat('Digite um Real: ')

# Exibe os valores lidos
print(f'O valor INTEIRO digitado foi {n1} e o REAL foi {n2}')
