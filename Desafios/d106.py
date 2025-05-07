# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores..


# Função que mostra a ajuda interativa para um comando Python
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', cor=4)  # Mostra título com fundo azul
    print('\033[7;40m', end='')  # Inverte as cores (branco no fundo preto)
    help(com)  # Mostra a documentação interativa do comando
    print('\033[m', end='')  # Reseta as cores


# Função que imprime um título com uma borda e cor personalizada
def titulo(msg, cor=0):
    # Lista com códigos ANSI para diferentes cores de fundo
    cores = [
        '\033[m',        # 0 - sem cor
        '\033[0;30;41m', # 1 - vermelho
        '\033[0;30;42m', # 2 - verde
        '\033[0;30;43m', # 3 - amarelo
        '\033[0;30;44m', # 4 - azul
        '\033[0;30;45m', # 5 - roxo
    ]
    tam = len(msg) + 4  # Calcula o tamanho da moldura
    print(cores[cor], end='')  # Define a cor
    print('~' * tam)           # Linha superior da moldura
    print(f'  {msg}')          # Mensagem com recuo
    print('~' * tam)           # Linha inferior da moldura
    print('\033[m', end='')    # Reseta cor para padrão


# ====== Programa principal ======
while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor=2)  # Título inicial com fundo verde
    comando = str(input('Função ou Biblioteca > ')).strip()  # Entrada do usuário
    
    if comando.upper() == 'FIM':  # Verifica se o usuário quer sair
        titulo('ATÉ LOGO!', cor=1)  # Mensagem de despedida com fundo vermelho
        break  # Encerra o loop
    
    ajuda(comando)  # Chama a função de ajuda

