# A) Vamos criar um menu em Python, usando modularização.

def leiaInt(msg):  # Função para ler um número inteiro com validação
    while True: 
        try:
            n = int(input(msg))  # Tenta converter a entrada para inteiro
        except (ValueError, TypeError):  # Se der erro de tipo ou valor inválido
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue  # Recomeça o loop
        except (KeyboardInterrupt):  # Se o usuário interromper com Ctrl+C
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0  # Retorna 0 como valor padrão
        else:
            return n  # Retorna o número se tudo correr bem


def linha(tam = 42):  # Gera uma linha com o número de caracteres desejado
    return '-' * tam  # Ex: '----------'


def cabeçalho(txt):  # Exibe um cabeçalho formatado com texto centralizado
    print(linha())  # Linha superior
    print(txt.center(42))  # Texto centralizado
    print(linha())  # Linha inferior


def menu(lista):  # Cria um menu numerado a partir de uma lista de opções
    cabeçalho('MENU PRINCIPAL')  # Mostra o título
    c = 1  # Contador para número da opção
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')  # Exibe item do menu com cores
        c += 1
    print(linha())  # Linha inferior do menu
    opc = leiaInt('\033[32mSua opção: \033[m')  # Pergunta ao usuário qual opção ele quer
    return opc  # Retorna a opção escolhida
